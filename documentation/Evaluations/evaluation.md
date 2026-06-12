# Evaluation

**Framework**: Evaluations  
**Kind**: protocol

A type that defines an evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol Evaluation : Sendable
```

## Mentions

- [Designing effective evaluations](designing-effective-evaluations.md)

#### Overview

Implement this protocol to create custom evaluations. The evaluation runs your system under test against a dataset and applies evaluators to measure performance.

```swift
struct MyEvaluation: Evaluation {
    let metric = Metric("Match")

    let dataset = ArrayLoader(samples: [
        ModelSample(prompt: "One plus one is...", expected: "Two.")
    ])

    func subject(from sample: ModelSample<String>) async throws -> ModelSubject<String> {
        ModelSubject(value: "Two.")
    }

    var evaluators: Evaluators {
        Evaluator { sample, subject in
            let metric = Metric("Match")
            guard let expected = sample.expected else { return metric.ignore() }
            return subject.value == expected ? metric.passing() : metric.failing()
        }
    }

    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        aggregator.computeMean(of: metric)
    }
}
```

## Topics

### Providing data
- [associatedtype Sample](evaluation/sample.md)
  The type of input samples in the evaluation dataset.
- [associatedtype SampleLoader : Loader](evaluation/sampleloader.md)
  The type of the sample loader used to provide the evaluation dataset.
- [var dataset: Self.SampleLoader](evaluation/dataset.md)
  The evaluation dataset.
### Testing an intelligent feature
- [associatedtype Subject : EvaluationSubject](evaluation/subject.md)
  The type of the subject produced by the system under test.
- [func subject(from: Self.Sample) async throws -> Self.Subject](evaluation/subject(from:).md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](evaluationsubject.md)
  A type that represents the output produced by the system under test.
- [struct ModelSubject](modelsubject.md)
  The subject type for language model evaluations.
- [var name: String](evaluation/name.md)
  The default name, derived from the type name.
### Scoring results
- [var evaluators: Self.Evaluators](evaluation/evaluators-swift.property.md)
  The evaluators to apply to each subject/sample pair.
- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  Shorthand for the evaluator array type, resolved per-conformance.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [struct EvaluatorsBuilder](evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.
### Running an evaluation
- [struct EvaluationTrait](evaluationtrait.md)
  A test trait that runs an evaluation and records the result as attachments.
- [struct EvaluationContext](evaluationcontext.md)
  A context that provides the evaluation result within a test scope.
- [struct EvaluationResult](evaluationresult.md)
  The results of running a model evaluation.
- [func run(info: [String : String]) async throws -> EvaluationResult](evaluation/run(info:).md)
  Runs the evaluation against the dataset and computes metric results.
### Inspecting detailed results
- [var inputColumn: ResultColumn<Self.Sample>](evaluation/inputcolumn.md)
  A typed column descriptor for the input samples in the detailed DataFrame.
- [var responseColumn: ResultColumn<Self.Subject>](evaluation/responsecolumn.md)
  A typed column descriptor for the model responses in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](evaluation/expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.
### Errors
- [enum EvaluationError](evaluationerror.md)
  Errors thrown during an evaluation run.
- [enum EvaluationResultsError](evaluationresultserror.md)
  Errors the framework throws when parsing evaluation results.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Evaluating language model responses](evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.
- [Designing effective evaluations](designing-effective-evaluations.md)
  Design evaluations that tell you how well your feature works, why it fails, and where to focus next.
- [Book Tracker: Using Evaluations to evaluate an intelligent feature](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md)
  Measure and improve the quality of your app’s intelligence-powered features using the Evaluations framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation)*