# Scoring with model-as-judge evaluators

**Framework**: Evaluations

Score subjective qualities like tone, accuracy, and relevance that programmatic checks cannot measure.

#### Overview

Programmatic evaluators work well when correctness is easily measurable, for example, exact matches, numeric ranges, or JSON schema validation. But there are many quality metrics that you cannot verify with simple code checks. Judging whether a joke is funny, an explanation is clear, or an email strikes the right tone requires reasoning about language, context, and intent.

[`ModelJudgeEvaluator`](modeljudgeevaluator.md) uses a language model to score the output of another model. You configure the model as judge with a scoring scale that defines what quality levels look like and, optionally, a [`ModelJudgePrompt`](modeljudgeprompt.md) with domain-specific instructions.

The model as judge scores each response alongside a written rationale explaining its reasoning. The result is a [`Metric`](metric.md) you can aggregate and track just as with any code-based evaluator. For guidance on when to use a model as judge versus a code-based evaluator, see [`Designing specific, measurable criteria in an evaluation suite`](designing-evaluation-criteria.md). For best practices on scoring scales and calibration, see [`Designing effective model-as-judge evaluators`](designing-effective-model-judges.md).

The Evaluations Framework supports two modes:

- **Pointwise**: Scores a single response independently against your scale.
- **Pairwise**: Compares a response against a baseline to determine which is better.

This article shows you how to create pointwise evaluations with single and multi-dimension scoring, build pairwise evaluations, and customize the model-as-judge prompt with instructions, evaluation targets, and reference data.

#### Build a Pointwise Evaluator

A pointwise evaluator scores each response independently against criteria you define. This lets you evaluate domain-specific qualities that programmatic checks cannot measure, such as whether generated content is accurate, relevant, and useful for your app’s purpose.

The following evaluation uses a [`ModelJudgeEvaluator`](modeljudgeevaluator.md) to assess how well a model generates tags for books based on user reviews. The `BookTags` type uses [`Generable`](https://developer.apple.com/documentation/FoundationModels/Generable) and [`Guide(description:_:)`](https://developer.apple.com/documentation/FoundationModels/Guide(description:_:)) from [`Foundation Models`](https://developer.apple.com/documentation/FoundationModels) to describe the expected output structure to the language model:

```swift
@Generable
struct BookTags: Codable, Sendable {
    @Guide(description: "Tags describing the book's genre, themes, and setting",
           .count(3...8))
    var tags: [String]
}

struct BookTagEvaluation: Evaluation {

    // Book reviews for the model to generate tags from.
    let dataset = ArrayLoader(samples: [
            ModelSample(prompt: "An absolutely breathtaking novel. The characters are richly drawn, the plot twists kept me guessing, and the prose is lyrical without being overwrought.", expected: BookTags(tags: [])),
            ModelSample(prompt: "Honestly a slog. It's a dystopian novel about a totalitarian surveillance state but the characters are paper-thin and the romance subplot felt forced.", expected: BookTags(tags: [])),
            ModelSample(prompt: "A fun, twisty murder mystery set on a private island. Classic whodunit vibes with an eccentric cast of suspects and a storm that cuts them off from the mainland.", expected: BookTags(tags: [])),
            ModelSample(prompt: "This book completely changed how I think about habits. The idea that tiny changes compound over time really stuck with me. Very practical.", expected: BookTags(tags: [])),
            ModelSample(prompt: "A devastating, beautiful novel about a family torn apart by war. The way the author writes about memory and loss had me in tears.", expected: BookTags(tags: [])),
        ])

    // Run the intelligent feature under test.
    func subject(from sample: ModelSample<BookTags>) async throws -> ModelSubject<BookTags> {
        let session = LanguageModelSession(
            instructions: "Generate tags for this book based on the review."
        )
        let response = try await session.respond(to: sample.prompt, generating: BookTags.self)
        return ModelSubject(value: response.content)
    }

    // Evaluate the output from the intelligent feature.
    var evaluators: Evaluators {
        ModelJudgeEvaluator(
            "TagQuality",
            scale: .numeric([
                4: "Tags accurately represent the book and are useful for browsing.",
                3: "Tags are accurate but include one or two that are too vague or generic.",
                2: "Tags get the general idea but miss important qualities of the book.",
                1: "Tags are inaccurate or misleading.",
            ])
        )
    }

    // Summarize the metrics.
    let tagQuality = Metric("TagQuality")
    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        aggregator.computeMean(of: tagQuality)
    }
}
```

This evaluation generates tags for each review, then asks the model as judge to score them. The [`ModelJudgeEvaluator`](modeljudgeevaluator.md) sends the original review and the model’s tags to the model as judge, which returns a score and rationale.

The name you pass as the first parameter, `"TagQuality"`, identifies this metric in the results. Use the same string in [`aggregateMetrics(using:)`](evaluation/aggregatemetrics(using:).md) to compute summary statistics.

The scale maps numeric values to quality-level descriptions. Each entry describes what a response at that score looks like, constraining the model as judge to one of these values. Each level needs to describe observable features rather than restating a quality gradient. “Tags accurately represent the book and are useful for browsing” gives the model as judge something concrete to check. “Excellent quality” does not.

#### Evaluate Multiple Dimensions in a Single Pass

The single `"TagQuality"` scale above asks two different questions at once: are the tags accurate and are they useful for browsing?

Use [`ScoreDimension`](scoredimension.md) to split each concern into its own focused question with its own scale. Pass an array of dimensions to [`ModelJudgeEvaluator`](modeljudgeevaluator.md) using the `dimensions:` parameter. The evaluator scores all dimensions in a single call to the model as judge, so you get multiple metrics without extra latency:

```swift
    private let accuracy = ScoreDimension(
        "Accuracy",
        description: "Does each tag describe the book itself?",
        scale: .numeric([
            4: "Every tag describes the book's genre, themes, or setting.",
            3: "Most tags describe the book but one or two reflect the reader's opinion.",
            2: "Some tags describe the book but most reflect the reader's opinion.",
            1: "None of the tags meaningfully describe the book.",
        ])
    )
    private let usefulness = ScoreDimension(
        "Usefulness",
        description: "Is each tag the right level for browsing a personal library?",
        scale: .numeric([
            4: "Every tag would help someone find this book while browsing.",
            3: "Most tags are useful for browsing but a couple are too narrow or generic.",
            2: "About half the tags are useful; the rest are too narrow or generic.",
            1: "The tags would not help someone browse a library.",
        ])
    )

    var evaluators: Evaluators {
        ModelJudgeEvaluator(
            dimensions: [accuracy, usefulness]
        )
    }
```

Each [`ScoreDimension`](scoredimension.md) answers exactly one question, which gives the model as judge a clearer task and gives you a more specific signal. In the example above, a book-tagging service might score high on accuracy (the tags match the review text) but low on usefulness (subjective tags like “uninspired” are too narrow to browse by). A single combined scale obscures that distinction.

Aggregate each dimension separately to track them independently:

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.group("Judge") { group in
        group.computeMean(of: accuracy.metric)
        group.computeMean(of: usefulness.metric)
    }
}
```

#### Customize the Pointwise Model As Judge Prompt

For pointwise evaluation, you can provide a [`ModelJudgePrompt`](modeljudgeprompt.md) to control how the model as judge sees and evaluates the response. The prompt has three components:

- **Instructions**: The system prompt for the judge session. Define the judge’s role, list the criteria to assess, and provide step-by-step evaluation procedures.
- **Evaluation target**: An optional closure that extracts the text the judge evaluates from the model’s response. When omitted, the response is JSON-serialized automatically.
- **Reference**: An optional closure that provides additional context to the judge, such as expected values or source material.

Pairwise evaluation builds its own prompt internally. The `instructions` and `reference` components only apply to pointwise evaluators. Pairwise evaluation supports `evaluationTarget` through its own parameter to control how both the response and baseline are formatted for the model as judge.

##### Write Effective Instructions

Good instructions include three things:

- A role that frames the judge’s expertise
- Criteria that list the specific dimensions to assess
- Evaluation steps that give the judge a procedure to follow before assigning a score

Including steps promotes consistent evaluation by preventing the model as judge from jumping to a score based on a first impression.

The following prompt demonstrates a role, criteria, and evaluation steps for the book-tag evaluator from the earlier section:

```swift
ModelJudgePrompt(
    instructions: """
        You are evaluating automatically generated tags for Shelf, a personal
        book-tracking app. A good tag describes the book itself: its genre, themes, tone,
        or setting. A bad tag picks up the reader's personal reactions rather than
        describing the book.

        Evaluate the tags considering the following criteria:

        - Accuracy: Each tag should describe an objective quality of the book, not the
        reader's opinion. "dystopian" and "romance" are good. "predictable" and
        "unrecommended" are the reader's judgment.
        - Usefulness: Each tag should be the right level of specificity for browsing a
        personal library. "literary fiction" is useful. "uninspired" is too subjective
        to group books by.
        - Coverage: The tags should capture the book's main genre and the most
        important themes without redundancy.

        Evaluate step by step:
        1. List each tag and classify it as a book descriptor or a reader reaction.
        2. For the book descriptors, check whether they are at the right level for
        browsing a personal library.
        3. Check whether the tags cover the book's genre and key themes.
        4. Assign a score based on the scale, considering all criteria together.
        """
)
```

If you omit the [`ModelJudgePrompt`](modeljudgeprompt.md) entirely, the evaluator uses default instructions that ask the model as judge to rate the response using the scoring scale.

##### Improve Consistency with Scored Examples

Improve scoring consistency by embedding scored examples directly in the instructions. These examples of what different score levels look like help the model as judge apply the scale consistently across samples.

Include labeled examples in the instructions. Each example shows a prompt, a response, the expected score, and a rationale explaining the reasoning:

```swift
ModelJudgeEvaluator(
    "EmailTone",
    scale: .numeric([
        4: "Professional, clear, and well-matched to the scenario, with appropriate warmth.",
        3: "Professional and clear, but feels slightly generic, formal, or impersonal.",
        2: "Noticeable tone issues: too curt, too informal, or mismatched to the scenario.",
        1: "Unprofessional, unclear, rude, or completely inappropriate for the scenario.",
    ]),
    judge: SystemLanguageModel.default,
    prompt: ModelJudgePrompt(
        instructions: """
            You are an expert evaluator of professional email tone. Your task is to evaluate
            whether an AI-generated email strikes the right professional tone for a workplace
            setting.

            Evaluate the email considering:

            - Professionalism: Uses appropriate language for a workplace. Avoids slang, overly
            casual phrasing, or unnecessarily stiff formality.
            - Clarity: Clearly communicates its purpose. The reader immediately understands
            what is being asked or conveyed.
            - Warmth: Feels human and approachable. Includes appropriate pleasantries without
            being excessive.
            - Appropriateness: The tone matches the scenario: a complaint is firm but
            respectful; a request is polite but clear; good news is enthusiastic but
            professional.

            Here are some examples to calibrate your scoring:

            ### Example 1
            **Prompt:** Write an email to a colleague asking them to review your document
            by Friday.
            **Response:** "Will you take a look at the Q3 report when you get a chance?
            It would be great to have your feedback by Friday so I can incorporate any changes
            before the Monday meeting. Let me know if that timeline works for you. Thanks!"
            **Score:** 4
            **Rationale:** The email is polite, clear, and professional. It states the request,
            gives a reason for the deadline, and respects the recipient's time by checking if
            the timeline works.

            ### Example 2
            **Prompt:** Write an email sharing a project status update with stakeholders.
            **Response:** "Hi everyone, I wanted to share a quick update on Project Atlas.
            We completed the design review last week, and development is on track for the
            June deadline. There are a couple of open questions about the API integration
            that I'll follow up on separately. Please reach out if you have any concerns."
            **Score:** 3
            **Rationale:** Professional and clear with good structure. Could be slightly warmer
            or more engaging, the update is efficient but reads as formulaic.

            ### Example 3
            **Prompt:** Write an email declining a meeting invitation.
            **Response:** "I can't make it. Sorry."
            **Score:** 2
            **Rationale:** While not rude, the email is too brief for a professional setting.
            It doesn't offer an alternative or show engagement with the topic.

            ### Example 4
            **Prompt:** Write an email to a colleague asking them to review your document
            by Friday.
            **Response:** "I need you to review my document. Get it done by Friday."
            **Score:** 1
            **Rationale:** The email is curt and demanding. It lacks any politeness, gives no
            context for the request, and does not acknowledge the recipient's workload or time.

            Use these examples to calibrate your scoring. Apply the same standards
            consistently. Evaluate step by step, then assign a score from 4, 3, 2, or 1.
            """
    )
)
```

Include examples that span the full range of your scale. At minimum, show what a high score and a low score look like. Ideally, include an example at every level so the judge has a clear reference point for each step on the scale.

> 💡 **Tip**: Add a final instruction such as “Use these examples to calibrate your scoring.” to remind the model as judge to use the examples as reference points.

##### Format Structured Output for the Model As Judge

When you use structured output, the `evaluationTarget` closure formats the response into readable text for the model as judge. By default, the model as judge receives a JSON serialized version of the result.

```swift
prompt: ModelJudgePrompt(
    evaluationTarget: { value in
        "\(value.tags.count) tags: " + value.tags.joined(separator: ", ")
    }
)
```

##### Provide Reference Data for the Model As Judge

Use the `reference` closure to give the model as judge additional context, such as expected values, source material, or ground truth data that’s known to be accurate. The closure receives the input sample and the model’s response, and returns a `[String: String]` dictionary. Each key-value pair becomes a labeled section in the judge’s prompt.

For example, if your model generates tags for a book-tracking app, you can provide the expected tags so the model as judge can compare:

```swift
ModelJudgeEvaluator(
    "TagQuality",
    scale: .numeric([
        4: "All tags are relevant and match the expected tags closely.",
        3: "Most tags match the expected tags, with one or two missing or incorrect.",
        2: "Some tags match but several are missing or incorrect.",
        1: "Tags are mostly irrelevant or completely wrong.",
    ]),
    judge: SystemLanguageModel.default,
    prompt: ModelJudgePrompt(
        instructions: """
            You are evaluating automatically generated tags for Shelf, a personal
            book-tracking app. A good tag is specific, relevant to the book's content, and useful
            for organizing a personal library. A bad tag is generic, irrelevant, or misleading.
            Compare the generated tags against the expected tags and evaluate step by step.
            """,
        evaluationTarget: { value in
            "\(value.tags.count) Generated tags: " + value.tags.joined(separator: ", ")
        },
        reference: { input, _ in
            guard let expected = input.expected else { return [:] }
            return ["Expected Tags": expected.tags.joined(separator: ", ")]
        }
    )
)
```

Without `reference`, the model as judge only sees the prompt and the response. Adding reference data lets the model as judge evaluate how well the response matches expectations, not just whether it seems reasonable in isolation.

#### Compare Two Responses with Pairwise Evaluation

Pairwise evaluation compares two responses and tells you which one the model as judge rates higher. Use it to compare prompt strategies, model versions, or before-and-after changes. Instead of scoring absolute quality, the model as judge decides whether a response is better or worse than a baseline.

Use the [`pairwise(_:scale:judge:scoringMode:evaluationTarget:)`](modeljudgeevaluator/pairwise(_:scale:judge:scoringmode:evaluationtarget:).md) method and frame your scale as a comparison. A score of 4 means the response is much better than the baseline, and a score of 1 means the baseline is much better. The 1–4 scale has no neutral midpoint, so the judge has to decide which side of the comparison wins on every sample.

Unlike pointwise evaluation, the pairwise method uses its own built-in prompt and automatically sends the sample’s [`expected`](modelsample/expected.md) value to the model as judge as the baseline. You provide the baseline when you create each sample, and the evaluator handles the rest.

```swift
struct ExplanationPairwiseEvaluation: Evaluation {
    private let explanationComparison = Metric("ExplanationComparison")

    let dataset = ArrayLoader(samples: [
            ModelSample(
                prompt: "Explain why the sky is blue.",
                expected: "The sky is blue because of the way sunlight interacts with the atmosphere. Blue light gets scattered more than other colors."
            ),
            ModelSample(
                prompt: "Explain what DNA is.",
                expected: "DNA is a molecule in your cells that contains your genetic information. It looks like a twisted ladder. It determines things like your eye color and height."
            ),
            ModelSample(
                prompt: "Explain why ice floats.",
                expected: "Ice floats because water expands when it freezes, making ice less dense than liquid water. The lighter ice sits on top of the heavier water."
            ),
        ])

    func subject(from sample: ModelSample<String>) async throws -> ModelSubject<String> {
        let session = LanguageModelSession(
            instructions: """
                You are a knowledgeable science communicator. Explain concepts clearly and
                engagingly for a general audience. Use analogies and examples where helpful.
                Keep your explanation concise but thorough.
                """
        )
        let response = try await session.respond(to: sample.prompt, generating: String.self)
        return ModelSubject(value: response.content)
    }

    var evaluators: Evaluators {
        ModelJudgeEvaluator.pairwise(
            "ExplanationComparison",
            scale: .numeric([
                4: "Response is significantly clearer, more accurate, and more engaging than the baseline.",
                3: "Response is noticeably better than the baseline in most areas.",
                2: "Baseline is noticeably better than the response in most areas.",
                1: "Baseline is significantly clearer, more accurate, and more engaging than the response.",
            ]),
            judge: SystemLanguageModel.default
        )
    }

    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        aggregator.computeMean(of: explanationComparison)
    }
}
```

In this example, a mean score above 2.5 indicates the model’s responses are generally better than the baselines. A mean score below 2.5 indicates regressions. Scores near 2.5 suggest comparable quality.

#### Combine Model As Judge Metrics with Programmatic Evaluators

Model-as-judge evaluators and code-based evaluators work together in the same evaluation. Use code-based evaluators for dimensions with clear right answers, and model-as-judge evaluators for subjective quality. Both produce [`Metric`](metric.md) values that you aggregate in the same [`MetricsAggregator`](metricsaggregator.md):

```swift
    private let nonEmpty = Metric("NonEmpty")
    private let quality = Metric("Quality")

    var evaluators: Evaluators {
        Evaluator { input, subject in
            return subject.value.isEmpty ? nonEmpty.failing() : nonEmpty.passing()
        }
        ModelJudgeEvaluator(
            "Quality",
            scale: .numeric([
                4: "Clear, relevant, and well-crafted.",
                3: "Mostly clear and relevant with minor issues.",
                2: "Below expectations in clarity, relevance, or craft.",
                1: "Poor quality, unclear, irrelevant, or incoherent.",
            ]),
            judge: SystemLanguageModel.default,
            prompt: ModelJudgePrompt(
                instructions: """
                    You are an expert evaluator. Assess the overall quality of the response
                    considering clarity, relevance to the prompt, and craft. Evaluate step by
                    step, then assign a score.
                    """
            )
        )
    }

    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        aggregator.group("Validation") { group in
            group.computeMean(of: nonEmpty)
        }
        aggregator.group("Judge") { group in
            group.computeMean(of: quality)
        }
    }
```

#### Run a Model As Judge Evaluation

Run your model-as-judge evaluation with [`Swift Testing`](https://developer.apple.com/documentation/Testing), just as you do with other evaluations:

```swift
import Testing
import Evaluations

struct BookTagTests {
    static let evaluation = BookTagEvaluation()
    @Test(.evaluates(Self.evaluation))
    func evaluateTagQuality() async throws {
        let result = EvaluationContext.current.result
        let score = result.aggregateValue(.mean(of: Self.evaluation.tagQuality))
        #expect(score > 2.5)
    }
}
```

#### Use Rationales to Debug and Refine Your Evaluator

When the model as judge scores a response, it also produces a written rationale explaining its reasoning. These rationales appear in the detailed results alongside the score for each sample. When scores seem wrong or inconsistent, the rationales usually show you why. For a guide to interpreting rationales, identifying common scoring problems, and refining your evaluator configuration, see [`Designing effective model-as-judge evaluators`](designing-effective-model-judges.md).

## See Also

- [Designing effective model-as-judge evaluators](designing-effective-model-judges.md)
  Configure model-as-judge evaluators that produce scores you correlate with human review.
- [struct ModelJudgeEvaluator](modeljudgeevaluator.md)
  An evaluator that uses a language model as a judge to score responses.
- [struct ModelJudgePrompt](modeljudgeprompt.md)
  A configuration for how a model-as-judge evaluator constructs its prompt.
- [struct ScoreDimension](scoredimension.md)
  A named scoring dimension for a model judge evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoring-with-model-as-judge-evaluators)*