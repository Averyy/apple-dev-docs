# Evaluating language model responses

**Framework**: Evaluations

Build an evaluation that runs your intelligence-powered feature against samples and scores each response.

#### Overview

Evaluations replace manual spot checks with structured, repeatable measurements of your model’s output quality. Define what success looks like by translating broad quality goals into concrete metrics, then run those metrics as often as you need, catching regressions, comparing prompt strategies, and building confidence before shipping.

Because you define your metrics before tuning prompts or switching models, every change is measured against the same criteria. Your focus stays on measurable outcomes rather than subjective impressions of quality. For guidance on how to design your overall strategy for measuring and improving evaluations, see [`Designing effective evaluations`](designing-effective-evaluations.md).

To create an evaluation, you:

- Provide input as a dataset of samples with expected outputs.
- Define the subject, the intelligence-powered feature you are testing.
- Add evaluators that score each response against metrics you define.
- Aggregate those scores into a metric summary you compare across runs.

To see these four steps in use in a complete app, with code-based and model-judge scoring, synthetic data, and tool-call evaluation, see [`Book Tracker: Using Evaluations to evaluate an intelligent feature`](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md).

#### Provide Input

Define your dataset. Each sample carries a [`prompt`](modelsample/prompt.md) that the model receives and an optional [`expected`](modelsample/expected.md) value:

```swift
import Evaluations
import FoundationModels

struct LetterCountEvaluation: Evaluation {
    let dataset = ArrayLoader(samples: [
            ModelSample(prompt: "Count the letter 'r' in 'strawberry'.", expected: 3),
            ModelSample(prompt: "How many a's are in 'banana'?", expected: 3),
            ModelSample(prompt: "Mississippi contains how many s?", expected: 4),
            ModelSample(prompt: "What's the number of l in hello?", expected: 2),
            ModelSample(prompt: "The letter 'e' in 'bookkeeper' appears how many times?", expected: 3),
        ])

```

Building a large, comprehensive sample set by hand is tedious; see [`Generating synthetic datasets`](generating-synthetic-evaluation-datasets.md) for more details on generating samples synthetically.

#### Define the Subject

The *subject* is the model feature you’re testing. Implement the [`subject(from:)`](evaluation/subject(from:).md) method to call your intelligence-powered feature the same way you do in your app. The framework calls this method once for each sample in your dataset, and you return a [`ModelSubject`](modelsubject.md) that wraps the output alongside any conversation transcript:

```swift
func subject(from sample: ModelSample<Int>) async throws -> ModelSubject<Int> {
    // Create the language model session; you can customize this with instructions and you can
    // choose the model you want to use.
    let session = LanguageModelSession()
    // Create the model response the same way you do in your app.
    let response = try await session.respond(to: sample.prompt, generating: Int.self)
    // Return the model's response along with the transcript.
    return ModelSubject(
        value: response.content,
        transcript: session.transcript.structuredTranscript
    )
}
```

You can inspect both the output and the transcript in the detailed results.

#### Add Evaluators

Add evaluators that score each response. For guidance on choosing between code-based and model-judge evaluators, see [`Designing specific, measurable criteria in an evaluation suite`](designing-evaluation-criteria.md). Declare a [`Metric`](metric.md) for each measurement, then return one of its result values: [`passing(rationale:)`](metric/passing(rationale:).md) or [`failing(rationale:)`](metric/failing(rationale:).md) for binary checks, and [`scoring(_:rationale:)`](metric/scoring(_:rationale:).md) for continuous values.

The first evaluator below checks whether the count is exactly correct. The second measures how much the model’s answer deviates from the correct answer:

```swift
// Metrics used by the evaluation and tests.
let exactMatch = Metric("ExactMatch")
let absoluteError = Metric("AbsoluteError")

var evaluators: Evaluators {
    Evaluator { input, subject in
        // Return a pass or fail result for the "ExactMatch" metric.
        guard let expected = input.expected else { return exactMatch.ignore() }
        return subject.value == expected ? exactMatch.passing() : exactMatch.failing()
    }
    Evaluator { input, subject in
        // Return a score that contains the absolute error.
        guard let expected = input.expected else { return absoluteError.ignore() }
        let error = abs(Double(subject.value - expected))
        return absoluteError.scoring(error)
    }
}
```

#### Aggregate the Metric Summary

Finally, implement [`aggregateMetrics(using:)`](evaluation/aggregatemetrics(using:).md) to define how the framework summarizes your metrics into high-level statistics:

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.computeMean(of: exactMatch)
    aggregator.computeMean(of: absoluteError)
}
```

For evaluations with many metrics, group related ones together so the output stays organized:

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    // Create a group called "Accuracy" with the mean of ExactMatch.
    aggregator.group("Accuracy") { group in
        group.computeMean(of: exactMatch)
    }
    // Create a group called "Error" with the maximum AbsoluteError.
    aggregator.group("Error") { group in
        group.computeMaximum(of: absoluteError)
    }
}
```

#### Run Your Evaluation

To run an evaluation, attach the [`EvaluationTrait`](evaluationtrait.md) to a test function using the `@Test(.evaluates(...))` trait. The trait runs the dataset through your model, applies evaluators, and aggregates the metrics. Access the results through [`EvaluationContext`](evaluationcontext.md):

```swift
import Testing
import Evaluations

struct LetterCountTests {
    static let evaluation = LetterCountEvaluation()

    @Test(.evaluates(Self.evaluation))
    func letterCounting() async throws {
        let result = EvaluationContext.current.result
        let score = result.aggregateValue(.mean(of: Self.evaluation.exactMatch))
        #expect(score > 0.8)
    }
}
```

When the run finishes, open the Report navigator and select the Evaluations item beneath the test run to open the evaluation report:

![A screenshot of the Report navigator in Xcode. Beneath a completed LetterCount test run, the Evaluations item is selected, alongside the Insights, Coverage, Tests, and Log items.](/images/com.apple.evaluations/eval-report-navigator@2x.png)

You get back an [`EvaluationResult`](evaluationresult.md) with three views into your data:

- **[`summary`](evaluationresult/summary.md)**: For aggregate statistics you compare across runs
- **[`detailed`](evaluationresult/detailed.md)**: For per-sample scores, including the query, response, and every metric value
- **[`groupedSummary`](evaluationresult/groupedsummary.md)**: To see the summary organized by the groups you defined in [`aggregateMetrics(using:)`](evaluation/aggregatemetrics(using:).md)

Read columns out of the detailed view through the typed descriptors on your evaluation. Each descriptor pairs the column’s name with its value type, so you get back a typed `Column<T>` without restating the type at the call site. The `[metric:]` subscript does the same for metric columns:

```swift
@Test(.evaluates(Self.evaluation))
func inspectDetailedResults() async throws {
    let result = EvaluationContext.current.result

    // Read typed columns out of the per-sample DataFrame.
    let inputs   = result.detailed[Self.evaluation.inputColumn]
    let expected = result.detailed[Self.evaluation.expectedColumn]
    let scores   = result.detailed[metric: Self.evaluation.exactMatch]

    // Surface the prompts where the model's count disagreed with the expected count.
    for row in 0..<scores.count where scores[row]?.value == .failing {
        let prompt = inputs[row]?.promptDescription ?? "<missing>"
        let target = expected[row].map(String.init) ?? "?"
        print("Missed (expected \(target)): \(prompt)")
    }

    #expect(scores.count == 5)
}
```

Use these lookups to identify failing samples for review, build follow-up datasets from edge cases, or write assertions that go beyond aggregate scores.

For guidance on interpreting results and iterating on your feature, see [`Designing effective evaluations`](designing-effective-evaluations.md).

#### Evaluate Tool Calling Behavior

Your intelligence-powered features may rely on tools that fetch live data, perform calculations, or trigger actions. Evaluations let you verify that the model passes the correct arguments and calls tools in the expected order.

For details on how to integrate tool calling with Foundation Models, see [`Expanding generation with tool calling`](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling).

The following example defines a simple, letter-counting tool:

```swift
// Create a tool that conforms to the Tool protocol and supports letter counting.
struct CountLetterOccurrences: Tool {
    let name = "count_letters"
    let description = "Counts how many times a letter appears in a word."

    // The tool needs two arguments: the letter you want to count and the word.
    @Generable
    struct Arguments {
        @Guide(description: "The letter to count")
        var letter: String
        @Guide(description: "The word")
        var word: String
    }

    // The letter counting tool's implementation.
    func call(arguments: Arguments) async throws -> Int {
        return arguments.word.lowercased().filter { String($0) == arguments.letter.lowercased() }.count
    }
}
```

To verify the model calls this tool correctly, attach a [`TrajectoryExpectation`](trajectoryexpectation.md) to the sample with one or more [`ToolExpectation`](toolexpectation.md) entries:

```swift
ModelSample(
    prompt: "Count the letter 'r' in 'strawberry'.",
    expected: 3,
    // Attach a trajectory expectation that defines the expected tool-calling sequence.
    expectations: TrajectoryExpectation(
        ordered: [
            // Expect the model to call `count_letters` with these exact arguments.
            ToolExpectation(
                "count_letters",
                arguments: [
                    .exact(argumentName: "letter", value: .string("r")),
                    .exact(argumentName: "word", value: .string("strawberry")),
                ]
            ),
        ]
    )
),
```

Then, add a [`ToolCallEvaluator`](toolcallevaluator.md) to your evaluators list:

```swift
// Computed metrics.
let exactMatch = Metric("ExactMatch")
let absoluteError = Metric("AbsoluteError")
// Tool calling metrics.
let toolsAllPass = Metric("ToolsAllPass")
let toolsPercentagePass = Metric("ToolsPercentagePass")

var evaluators: Evaluators {
    // Score tool calls against the trajectory expectations defined on each sample.
    ToolCallEvaluator(allPass: toolsAllPass, percentagePass: toolsPercentagePass)
    // Also check whether the final output matches the expected answer.
    Evaluator { input, subject in
        guard let expected = input.expected else { return exactMatch.ignore() }
        return subject.value == expected ? exactMatch.passing() : exactMatch.failing()
    }
}
```

Running the evaluation with and without the tool produces a summary row for each, so you can compare them at a glance. Here are both rows under the same test:

![A screenshot of the Evaluations summary in the Xcode Test Report. Under the LetterCountTests group, the LetterCountEvaluation row shows an Exact Match ratio of 58 percent and the LetterCountEvaluationTools row shows 100 percent, each across 12 responses.](/images/com.apple.evaluations/eval-summary@2x.png)

For a side-by-side view, choose Compare and select a run for each side. This figure shows that adding the counting tool lifts the mean Exact Match score from 58 percent to 100 percent and brings every failing prompt up to a pass:

![A screenshot of the Compare view in the Xcode Test Report showing LetterCountEvaluation beside LetterCountEvaluationTools. The mean Exact Match score rises from 58 percent without the tool to 100 percent with the tool, and the per-prompt table shows the prompts that fail without the tool passing with it.](/images/com.apple.evaluations/eval-run-comparison@2x.png)

For more on evaluating tool calling, see [`Evaluating tool-calling behavior`](evaluating-tool-calling-behavior.md).

#### Evaluate Subjective Quality with a Model Judge

Not every quality dimension has a clear-cut programmatic test. For subjective criteria such as tone, helpfulness, or fluency, use a [`ModelJudgeEvaluator`](modeljudgeevaluator.md) to have a language model score responses on your behalf. Provide a rating scale and evaluation instructions, then add the model judge to your evaluators list:

```swift
var evaluators: Evaluators {
    ModelJudgeEvaluator(
        "HaikuQuality",
        scale: .numeric([
            4: "Excellent - Perfect 5-7-5 form, strongly relevant to the topic, and uses vivid imagery that evokes emotion.",
            3: "Good - Correct or near-correct form, clearly relevant, with some evocative language.",
            2: "Poor - Incorrect syllable count, weak connection to topic, or lacks poetic quality.",
            1: "Very poor - Not recognizable as a haiku, off-topic, or incoherent.",
        ]),
        judge: SystemLanguageModel.default,
        prompt: ModelJudgePrompt(
            instructions: """
                You are an expert poetry evaluator. Evaluate the quality of AI-generated haiku poems \
                considering: form (traditional 5-7-5 syllable structure), relevance (clearly relates to \
                the given topic), and imagery (vivid, sensory language that evokes a feeling). \
                Give step-by-step explanations for your scoring.
                """
        )
    )
}
```

The model judge scores each response on a numeric scale and provides a written rationale explaining its reasoning. For a complete walkthrough of building model-judge configurations, including pointwise and pairwise evaluation, scored examples, and prompt customization, see [`Scoring with model-judge evaluators`](scoring-with-model-as-judge-evaluators.md).

## See Also

- [Designing effective evaluations](designing-effective-evaluations.md)
  Design evaluations that tell you how well your feature works, why it fails, and where to focus next.
- [Book Tracker: Using Evaluations to evaluate an intelligent feature](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md)
  Measure and improve the quality of your app’s intelligence-powered features using the Evaluations framework.
- [protocol Evaluation](evaluation.md)
  A type that defines an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluating-language-model-responses)*