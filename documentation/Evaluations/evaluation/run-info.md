# run(info:)

**Framework**: Evaluations  
**Kind**: method

Runs the evaluation against the dataset and computes metric results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func run(info: [String : String] = [:]) async throws -> EvaluationResult
```

#### Return Value

An [`EvaluationResult`](evaluationresult.md) that contains the summary statistics and sample-level results.

#### Discussion

This method executes the evaluation by iterating through your dataset, producing subjects, applying evaluators, and producing summary statistics. The evaluation logs and skips inference errors rather than halting the run.

The resulting [`EvaluationResult`](evaluationresult.md) contains typed data in its DataFrames:

- The Input column contains the full `Sample` from the dataset.
- The Response column contains the full subject that the system under test produces.
- Metric columns contain [`Metric`](metric.md) values directly, preserving pass, fail, and score semantics and rationale.
- The SubjectInferenceError column contains the failure reason for any sample whose subject could not be produced by `subject(from:)` (the same rows whose Response is `nil`). It is present only when at least one subject failed.
- The EvaluatorErrors column contains the failure reason(s), labeled by evaluator type, for any sample whose subject was produced but one or more evaluators threw. It is present only when at least one evaluator failed.

## Parameters

- `info`: User-defined key-value pairs attached to the result, such as model name or dataset version.

## See Also

- [struct EvaluationTrait](evaluationtrait.md)
  A test trait that runs an evaluation and records the result as attachments.
- [struct EvaluationContext](evaluationcontext.md)
  A context that provides the evaluation result within a test scope.
- [struct EvaluationResult](evaluationresult.md)
  The results of running a model evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/run(info:))*