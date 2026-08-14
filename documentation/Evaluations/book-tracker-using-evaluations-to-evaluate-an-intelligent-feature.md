# Book Tracker: Using Evaluations to evaluate an intelligent feature

**Framework**: Evaluations

Measure and improve the quality of your app’s intelligence-powered features using the Evaluations framework.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Adding an intelligence-powered feature to your app is quick. Knowing whether it’s performing correctly is harder. A model’s output can vary from run to run, and what counts as a good result is often partly subjective. The Evaluations framework helps you measure the quality of your feature, track it as you change a prompt, and catch regressions before they ship. This sample app shows you how to systematically evaluate how well your intelligent feature performs.

Book Tracker is a SwiftUI app for cataloging books and the reviews you write about them. It includes two intelligence-powered features using the on-device language model:

- Descriptive tags from a freeform review, so you can browse and filter your library
- Natural-language search assistant that answers questions about your collection by calling tools

![A side-by-side view of the Book Tracker app. The library screen shows a grid of book covers, and the book details screen shows generated tags above a written review.](/images/com.apple.evaluations/library-and-details@2x.png)

This sample evaluates both of Book Tracker’s intelligent features. It builds a complete evaluation for the book-tagging feature, then assesses the app’s synthetic data generation, model-as-judge calibration, and tool-call evaluation:

- Apply code-based checks to the generated tags to test: number of tags, genre presence, and number of words.
- Use a model as judge to score usefulness and accuracy of the tags.
- Grow the small dataset into a larger one using synthetic data generation.
- Calibrate the model as judge against a human expert so you can trust its scores as you iterate on a prompt.
- Evaluate the search assistant’s tool calls against expected tool-calling trajectories.

For more information about the concepts behind this workflow, see [`Designing effective evaluations`](designing-effective-evaluations.md). This article focuses on the code that puts these concepts to work.

> **Note**: This sample code project is associated with WWDC26 session 298: [`Meet the Evaluations framework`](https://developer.apple.comhttps://developer.apple.com/wwdc26/298/), session 335: [`Improve your prompts by hill-climbing with Evaluations`](https://developer.apple.comhttps://developer.apple.com/wwdc26/335/), and session 299: [`Create robust evaluations for agentic apps`](https://developer.apple.comhttps://developer.apple.com/wwdc26/299/).

The diagram below shows the evaluation pipeline that this sample builds. A dataset of reviews flows through the book-tagging feature, both code-based evaluators and a model as judge score the generated tags, and the combined results produce a pass-or-fail report. The model as judge is calibrated to match a human expert’s scores.

![A flowchart of the sample’s evaluation pipeline. A dataset of reviews and expected tags feeds the book-tagging feature, which produces generated tags. The tags flow in parallel to code-based evaluators and to a model as judge, whose results combine in a metrics aggregator that produces a pass-or-fail report. A dashed loop calibrates the model as judge against expert scores.](/images/com.apple.evaluations/flowchart@2x.png)

#### Configure the Sample Code Project

Before you run the sample code project:

1. Open the sample with the latest version of Xcode.
2. Set the developer team for the project target to let Xcode automatically manage the provisioning profile. For more information, see [`Preparing your app for distribution`](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution) and [`Preparing your app for distribution`](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution).
3. Run the sample on a device or simulator that supports Apple Intelligence and the Foundation Models framework.

#### Generate Tags for a Review

The descriptive-tag feature is in `BookTaggingService`. It asks the on-device model to turn a reader’s review into a small set of descriptive tags. The output type is a [`Generable`](https://developer.apple.com/documentation/foundationmodels/generable) struct, and a [`Guide(description:_:)`](https://developer.apple.com/documentation/foundationmodels/guide(description:_:)) constrains the model to generate between three and eight tags:

```swift
@Generable
struct BookTags: Codable, Equatable {
    @Guide(description: "Descriptive tags capturing themes, genres, moods, and topics from the review", .count(3...8))
    var tags: [String]
}
```

The service builds a [`LanguageModelSession`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession) from a fixed set of instructions, running the on-device [`SystemLanguageModel`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel), and asks for the structured output:

```swift
static func generateTags(for review: String) async throws -> BookTags {
    let session = LanguageModelSession(
        model: SystemLanguageModel(guardrails: .permissiveContentTransformations),
        instructions: instructions
    )
    let response = try await session.respond(to: tagsPrompt(review: review), generating: BookTags.self)
    return response.content
}
```

These instructions are the part of the feature that an evaluation helps improve. The instructions give the model a librarian persona, three formatting rules, and a fixed list of known genres to choose from:

```swift
/// Allowed genres for the required genre tag.
static let knownGenres = [
    // Fiction genres
    "fiction", "literary-fiction", "science fiction", "sci-fi", "fantasy",
    "mystery", "thriller", "horror", "romance", "historical-fiction",
    "magical-realism", "dystopian", "adventure", "crime", "suspense",
    "cozy-mystery", "space-opera", "urban-fantasy", "dark-fantasy",
    "whodunit", "detective-fiction",
    // Nonfiction genres
    "nonfiction", "self-improvement", "self-help", "memoir", "biography",
    "autobiography", "history", "science", "philosophy", "psychology",
    "true-crime", "travel", "business", "economics", "politics",
    // Literary forms
    "poetry", "essays", "short-stories", "graphic-novel", "novella",
    "anthology"
]

/// System instructions describing the persona, formatting rules, and known genres.
static let instructions = """
    You are a librarian and literary analyst. Given a reader's freeform summary of a book
    they read — describing their thoughts, feelings, and what stood out — generate a set
    of descriptive tags reflected in the summary.

        Rules:
        - Return between 3 and 8 tags.
        - Tags should be lowercase, concise (single word or hyphenated), and descriptive.
        - Tags should include the book's genre, chosen from the included list of known genres.

        Known Genres:
        - \(Self.knownGenres.joined(separator: ", "))
    """
```

The sections that follow show how the sample measures how well these instructions perform, so you can change them with confidence. Most of them build up the book-tagging evaluation; the final section turns to the search assistant.

#### Create an Evaluation Dataset

An evaluation runs a feature against a dataset of samples. In the sample, each [`ModelSample`](modelsample.md) pairs a prompt that the feature receives with its expected result and measures the actual output against this expected result. `BookTaggingEvaluation` builds its dataset with an [`ArrayLoader`](arrayloader.md) from the app’s curated `Book.sampleBooks`, using each book’s review as the prompt and the maintainer’s hand-chosen tags as the expected value:

```swift
extension Book {
    /// Curated books used to populate the library and drive evaluations.
    static let sampleBooks: [Book] = [
        Book(
            title: "Little Women",
            author: "Louisa May Alcott",
            review: """
                I have read this book more times than I can count, starting as a child who sobbed through Beth's \
                death and returning as an adult who still does. There is something about Marmee's quiet steadiness \
                and Jo's furious ambition that feels genuinely alive across every single reading. The scene where Jo \
                burns her manuscript is one of the most painful moments in all of American literature, not because \
                of the pages lost but because of what it reveals about how little the world was willing to value her \
                work. And when Laurie asks Jo to marry him and she turns him down, I always hold my breath, even \
                knowing exactly what comes next. Here is my one gripe, offered gently: Professor Bhaer. He is kind \
                and steady, yes. But after Laurie, after everything Jo was and wanted to be, Bhaer feels like a \
                consolation prize dressed up as wisdom. Alcott reportedly wanted Jo to remain unmarried, and you can \
                feel that tension pulling at the prose. It does not ruin the book. Nothing could. But it does leave \
                a small, persistent ache.
                """,
            tags: ["classic", "coming-of-age", "family", "female protagonist", "heartwarming", "19th century"],
            rating: 4,
            coverImage: "little-women-book-cover"
        ),
        // More samples...
    ]
}

var dataset = ArrayLoader(samples:
    Book.sampleBooks.map { book in
        ModelSample(prompt: book.review, expected: BookTags(tags: book.tags))
    }
)
```

Because the sample maintainer wrote both the reviews and the expected tags, this curated set serves as *ground truth*: every sample has a known-good answer to score against. For guidance on categorizing samples and sizing a dataset, see [`Designing datasets to test your feature`](designing-evaluation-datasets.md).

#### Define the Subject Under Test

The *subject* is what an evaluation actually scores. In the sample, `BookTaggingEvaluation` defines the subject by calling the real `BookTaggingService`, so the evaluation tests the same code path that the app ships:

```swift
func subject(from sample: ModelSample<BookTags>) async throws -> ModelSubject<BookTags> {
    let result = try await BookTaggingService.generateTags(for: sample.promptDescription)
    return ModelSubject(value: result)
}
```

Because the production feature is called rather than a copy, improvements or weaknesses you measure here match the performance that people experience with the two intelligent features in the app: book tagging and natural-language search.

#### Score Tags with Code

Some qualities that the sample app tests are objective, so using a code-based evaluation is the fastest, most reproducible way to check whether:

- Tags include the book’s genre, chosen from a known list.
- Tags are concise, a single word or hyphenated, with three to eight tags in all.

The sample’s evaluation declares a [`Metric`](metric.md) for each check, then implements the checks as [`Evaluator`](evaluator.md) closures that report [`passing(rationale:)`](metric/passing(rationale:).md), [`failing(rationale:)`](metric/failing(rationale:).md), or [`scoring(_:rationale:)`](metric/scoring(_:rationale:).md):

```swift
/// Whether the tag count fell in the required 3–8 range.
let tagCount = Metric("Tag Count")
/// Raw tag count, aggregated for variance reporting.
let tagTotal = Metric("Tag Total")
/// Whether at least one tag matched the known-genre list.
let hasGenreTag = Metric("Has Genre Tag")
/// Whether every tag is a single word.
let wordCount = Metric("Word Count")

var evaluators: Evaluators {
    // Tag count is within the required 3–8 range.
    Evaluator { _, subject in
        let count = subject.value.tags.count
        if count >= 3 && count <= 8 {
            return tagCount.passing(rationale: "\(count) tags")
        }
        return tagCount.failing(rationale: "Got \(count) tags, expected 3–8")
    }

    // Records raw tag count.
    Evaluator { _, subject in
        let count = subject.value.tags.count
        return tagTotal.scoring(Double(count))
    }

    // Tags must be single-word or hyphenated.
    Evaluator { _, subject in
        for tag in subject.value.tags where tag.contains(" ") {
            return wordCount.failing(rationale: "Tag \(tag) contains multiple words")
        }
        return wordCount.passing()
    }

    // Pass on the first known-genre match.
    Evaluator { _, subject in
        let tags = subject.value.tags.map { $0.lowercased() }
        let knownGenres = BookTaggingService.knownGenres
        for tag in tags where knownGenres.contains(tag) {
            return hasGenreTag.passing(rationale: "Matched \(tag)")
        }
        return hasGenreTag.failing()
    }
}
```

The evaluation above defines three checks: tag count, multiple-word test, and genre check. These checks are cheap and deterministic: they run quickly and always return the same result for the same input. But they cannot tell you whether a tag is subjectively “good.”

#### Judge Subjective Quality with a Model

When you need to determine whether a tag describes the book or the reader’s mood, that’s a judgment call, not a rule you can express in code. The sample uses a [`ModelJudgeEvaluator`](modeljudgeevaluator.md) to score those qualities by asking a model to rate each response on one or more [`ScoreDimension`](scoredimension.md) values. Each dimension states a focused question and a numeric scale with levels.

```swift
let relevance = ScoreDimension(
    "Relevance",
    description: """
        Whether each tag describes a quality, theme, or tone
        of the book itself rather than incidental details or
        the reader's personal reactions.
        """,
    scale: .numeric([
        4: "Every tag describes the book itself",
        3: "Most tags describe the book",
        2: "Some tags describe personal reactions",
        1: "Tags don't meaningfully describe the book"
    ])
)
let usefulness = ScoreDimension(
    "Usefulness",
    description: """
        Whether tags are at the right granularity for browsing. Broad enough that
        multiple books could share the tag, specific enough to help filter.
        """,
    scale: .numeric([
        4: "Every tag could group multiple books while still narrowing a search",
        3: "Most tags are at the right level, one is either too broad or too narrow",
        2: "Most tags are too broad to filter or too narrow to group",
        1: "Tags would not help with browsing"
    ])
)
```

Each level has a concrete description instead of an abstract one, such as “the tags are good.” The scale uses four levels rather than three or five, so the judge has no neutral middle ground to default to and needs to commit to whether the tags are good or bad. The evaluator scores both relevance and usefulness in a single pass, and a [`ModelJudgePrompt`](modeljudgeprompt.md) tells the judge what it’s looking at, how to format each response, and what expected tags to consult:

```swift
ModelJudgeEvaluator(
    judge: SystemLanguageModel.default,
    dimensions: [relevance, usefulness],
    prompt: ModelJudgePrompt(
        instructions: """
            You are evaluating tags generated for a personal book-tracking app where users
            organize their library by browsing and filtering tags.
            """,
        evaluationTarget: { value in
            "\(value.tags.count) Generated tags: " + value.tags.joined(separator: ", ")
        },
        reference: { input, _ in
            ["Expected Tags": input.expected?.tags.joined(separator: ", ") ?? "No expected tags defined"]
        }
    )
)
```

For the full range of model-as-judge options, including pairwise comparison and scored examples, see [`Scoring with model-as-judge evaluators`](scoring-with-model-as-judge-evaluators.md). For strategies that make a model as judge reliable, see [`Designing effective model-as-judge evaluators`](designing-effective-model-judges.md).

#### Run the Evaluation and Read Results

The sample’s evaluation aggregates its metrics by building up a [`MetricsAggregator`](metricsaggregator.md) in `aggregateMetrics(using:)`. Grouping the code-based heuristics separately from the model-as-judge quality scores keeps the results organized logically:

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.group("Heuristics") { aggregator in
        aggregator.computeMean(of: tagCount)
        aggregator.computeStandardDeviation(of: tagTotal)
        aggregator.computeMean(of: tagTotal)
        aggregator.computeVariance(of: tagTotal)
        aggregator.computeMean(of: wordCount)
        aggregator.computeMean(of: hasGenreTag)
    }
    aggregator.group("Quality") { group in
        group.computeMean(of: relevance.metric)
        group.computeMean(of: usefulness.metric)
    }
}
```

In the Evaluations framework, an evaluation runs from a Swift Testing test through the [`EvaluationTrait`](evaluationtrait.md) that the `.evaluates(_:info:)` modifier adds. The test reads the aggregated result from [`EvaluationContext`](evaluationcontext.md) and asserts a threshold, which turns a quality target into a pass-or-fail check in the test suite:

```swift
@Test("Book Tag Evaluations", .evaluates(evaluation, info: evaluationInfo))
func evaluateBookTagging() async throws {
    let result = EvaluationContext.current.result
    #expect(result.aggregateValue(.mean(of: evaluation.tagCount)) >= 0.8)
}
```

In the sample’s evaluation, the threshold for the `tagCount` metric requires at least 80 percent of the runs to produce a valid tag count. An intelligence feature that can’t reliably return the right number of tags fails. Xcode records the results and presents them in detail:

![The Xcode test report summary for the Book Tracker tag evaluation. Metric cards report the code-based heuristics, including Has Genre Tag Ratio, Tag Count Ratio, and the tag-total average, variance, and standard deviation, alongside the model-as-judge Relevance and Usefulness averages.](/images/com.apple.evaluations/heuristics-and-quality-metric-groups@2x.png)

#### Scale Coverage with Synthetic Data

A small dataset can demonstrate that the intelligence-powered feature of generating descriptive tags works as expected on familiar titles, but it’s not large enough to produce statistically valid results. In the sample, the `BookSampleGenerator` command-line tool expands the curated set toward a target of 100 samples with a [`SampleGenerator`](samplegenerator.md). It seeds generation with the curated books and rejects any sample that breaks the rules. For this offline step, it uses the more powerful [`PrivateCloudComputeLanguageModel`](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel) instead of the on-device model.

```swift
let generator = SampleGenerator<ModelSample<BookTags>>(
    prompt,
    samples: dataset,
    targetCount: 100,
    sessionProvider: {
        LanguageModelSession(model: PrivateCloudComputeLanguageModel(), instructions: generatorInstructions)
    },
    validator: { sample in
        guard let book = sample.expected else { return false }
        guard sample.promptDescription.count >= 100 else { return false }
        guard (3...8).contains(book.tags.count) else { return false }
        return book.tags.allSatisfy { $0 == $0.lowercased() }
    }
)

for try await sample in generator.run() {
    expandedDataset.append(sample)
}
```

The tool writes the expanded set to `synthetic_book_samples.json`, and `SyntheticBookTaggingEvaluation` loads it with a [`JSONLoader`](jsonloader.md) to run the same metrics against the larger dataset. For the validation and sampling options, see [`Generating synthetic datasets`](generating-synthetic-evaluation-datasets.md).

#### Calibrate the Model As Judge Against an Expert

You can improve the quality of a model-as-judge’s scores for subjective quality evaluation by calibrating the scoring against a human expert. In the sample, `BookTagJudgmentCalibration` checks how closely the model as judge agrees with a set of human scores. The `DatasetExtractor` tool exports a real evaluation run to JSON, an expert scores those same tag sets by hand, and the calibration evaluation re-judges them and compares the two sets of scores.

Adding examples to the model-as-judge prompt can help it match the human scores:

```swift
prompt: ModelJudgePrompt(
    instructions: """
        You are calibrating with an expert librarian who scores
        automatically generated tags for a personal book-tracking
        app. Users write a short review of a book they've read; the app
        generates tags so they can later browse and filter their library.

        Your goal is to match how the librarian scores. The librarian
        is generous: tags only need to broadly fit the book to earn a
        high Relevance score, and standard genre or theme tags carry a
        high Usefulness score even when the set has weaker tags mixed in.
        Low scores are reserved for tag sets containing multiple flatly
        wrong, fabricated, or one-off tags.

        Score Relevance and Usefulness independently, even when one tag
        affects both. Use the worked examples below to calibrate.

        ## Worked examples

        ### Example A — clean fit (Pride and Prejudice)
        Tags: romance, historical-fiction, love, redemption, passion
        Librarian: Relevance 4, Usefulness 4
        Why: every tag describes the book and reads like a standard
        library.

        ### Example B — broadly fits, even with off tags (Dracula)
        Tags: horror, science-fiction, dystopian, classic-literature,
        literary-fiction
        Librarian: Relevance 4, Usefulness 4
        Why: "horror" and "classic-literature" land squarely. The
        sci-fi/dystopian tags are imperfect but not absurd, and the
        set is still browsable. The librarian doesn't drop the score
        for one or two off tags.

        ### Example C — short review, generic tags (Korean medicine book)
        Tags: nonfiction, science, health, history
        Librarian: Relevance 3, Usefulness 4
        Why: tags are generic but plausible. Generic labels are
        highly useful even when relevance is only moderate.

        ### Example D — drift into meta-commentary (Picture of Dorian Gray)
        Tags: literary-fiction, philosophy, witty, character-study,
        plot-device, middle-section, thought-provoking,
        misleadingly-praised
        Librarian: Relevance 3, Usefulness 3
        Why: about half the tags describe the book; the other half
        are commentary on the review itself ("middle-section",
        "misleadingly-praised"). Mixed set, mixed scores.

        ### Example E — flat genre contradiction (Frankenstein)
        Tags: horror, science-fiction, dystopian, philosophical,
        literary-fiction, psychological, self-help, self-improvement
        Librarian: Relevance 2, Usefulness 3
        Why: most tags are book-shaped, but "self-help" and
        "self-improvement" so flatly mis-categorize the book that
        Relevance drops to 2. Usefulness stays at 3 because the
        other tags are still standard labels.

        ### Example F — fabricated specifics (Ramakien)
        Tags: visual-dimension, thai-adaptation, ramayana, tragedy,
        trickster-figure, epic, episodic, quaint-dignity
        Librarian: Relevance 4, Usefulness 2
        Why: the tags do touch on the book's qualities, so Relevance
        holds at 4. But "visual-dimension", "quaint-dignity",
        "thai-adaptation" are not labels — Usefulness drops
        to 2.

        Now score the tag set you are given in the same spirit.
        """,
```

The prompt uses only a handful of examples on purpose. A longer list might teach the model as judge to echo those specific cases and overfit the alignment score, and hide whether the model as judge truly agrees with the expert on tag sets it has not seen.

The aggregator reports agreement as a custom metric. For each dimension, it computes Cohen’s kappa between the human expert’s scores and the model as judge’s. Kappa is a better fit than plain percent agreement here because a four-point scale produces some agreement by chance; the kappa calculation accounts for that chance agreement, so a high Cohen’s kappa score reflects real alignment rather than two raters both drifting to the middle of the scale. The test requires a score above a threshold:

```swift
aggregator.group("Relevance") { group in
    group.computeMean(of: relevance.metric)
    group.custom(of: relevance.metric, label: "Relevance Alignment Score") { judge in
        Statistics.cohensKappa(ratings1: expertRelevance, ratings2: judge) ?? 0
    }
}
```

```swift
#expect(result.aggregateValue(.custom(label: "Relevance Alignment Score")) > 0.6)
#expect(result.aggregateValue(.custom(label: "Usefulness Alignment Score")) > 0.6)
```

![The Xcode test report showing the Judge Calibration test failing. The Relevance Alignment Score is -0.037, well below the required 0.6, so the assertion fails and the judge isn’t yet calibrated against the expert.](/images/com.apple.evaluations/alignment-fail@2x.png)

In the sample, the test requires a Cohen’s kappa above 0.6 on both the relevance and usefulness dimensions. If the test fails, the next step is to revise the model-as-judge’s instructions, often by adding a worked example that covers the disagreement, and run again until the model as judge aligns with human scoring.

#### Evaluate the Assistants Tool Calls

The intelligence-powered search assistant feature answers a person’s question by calling tools rather than returning text, so the quality of its output is based on:

- Which tools it calls
- In what order
- With what arguments

In the sample, `SearchToolEvaluations` registers the app’s three real [`Tool`](https://developer.apple.com/documentation/foundationmodels/tool) implementations and captures the model’s tool calls through the session’s [`StructuredTranscript`](structuredtranscript.md):

```swift
func subject(from sample: ModelSample<BookResults>) async throws -> ModelSubject<BookResults> {
    let session = LanguageModelSession(
        model: SystemLanguageModel(guardrails: .permissiveContentTransformations),
        tools: registeredTools,
        instructions: BookAssistant.instructions
    )
    let response = try await session.respond(to: sample.prompt, generating: BookResults.self)
    return ModelSubject(value: response.content, transcript: session.transcript.structuredTranscript)
}
```

Each sample carries a [`TrajectoryExpectation`](trajectoryexpectation.md) built from one or more [`ToolExpectation`](toolexpectation.md) values that describe the tool calls a correct answer requires. Expectations can be unordered or ordered, can allow extra calls, can match arguments exactly or by natural-language criteria, and can forbid tools a correct answer must never call. This ordered expectation requires the assistant to search by tag and then fetch the matching book’s details:

```swift
expectations: TrajectoryExpectation(
    ordered: [
        ToolExpectation("searchBooks", arguments: [
            .exact(argumentName: "tag", value: .string("gothic"))
        ]),
        ToolExpectation("getBookDetails", arguments: [.keyOnly(argumentName: "bookId")])
    ],
    allowsAdditionalToolCalls: true
)
```

An argument doesn’t always have to match a fixed string. A `.naturalLanguage` matcher checks that an argument captures the right intent, which suits open-ended filters like mood or genre. An expectation can also name tools the assistant must not call. Here the assistant should narrow by genre and never fall back to a similarity search:

```swift
expectations: TrajectoryExpectation(
    unordered: [
        ToolExpectation("searchBooks", arguments: [
            .naturalLanguage(argumentName: "genre", criteria: "Should relate to science fiction")
        ])
    ],
    disallowed: [
        ToolExpectation("findSimilarBooks")
    ]
)
```

A [`ToolCallEvaluator`](toolcallevaluator.md) scores each trajectory, reporting whether every expected call passed and what percentage passed. The test then asserts a minimum pass rate:

```swift
var evaluators: Evaluators {
    ToolCallEvaluator(allPass: pass, percentagePass: percent)
}
```

```swift
#expect(result.aggregateValue(.mean(of: runner.percent)) >= 0.8)
```

For the full set of argument matchers and trajectory options, see [`Evaluating tool-calling behavior`](evaluating-tool-calling-behavior.md).

This evaluation checks which tools the assistant calls, in what order, and with what arguments. It doesn’t score the quality of the answers the assistant produces from those tool results. A production app also evaluates the generated answers, scoring them for qualities like relevance and groundedness with the same code-based and model-as-judge techniques this sample applies to tags.

![The Xcode test report for the search-tool evaluation. An All Passed column marks each prompt with a pass or fail, and a Percentage Passed column reports the share of expected tool calls each prompt matched, with All Passed Ratio and Percentage Passed Average summarized above.](/images/com.apple.evaluations/search-tools-per-sample@2x.png)

Both of Book Tracker’s intelligent features now have a measurable quality check: the sample scores tags with code and a calibrated model as judge, and it measures search against expected tool trajectories. Every change to a prompt, a model, or a tool runs against those evaluations, tracking statistics and failing the test suite when quality regresses. This systematic evaluation turns subjective impressions into evidence you can act on, and makes each round of improvement verifiable before release.

## See Also

- [Evaluating language model responses](evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.
- [Designing effective evaluations](designing-effective-evaluations.md)
  Design evaluations that tell you how well your feature works, why it fails, and where to focus next.
- [protocol Evaluation](evaluation.md)
  A type that defines an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature)*