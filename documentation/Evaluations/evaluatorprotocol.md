# EvaluatorProtocol

**Framework**: Evaluations  
**Kind**: protocol

A type that evaluates subjects and produces metrics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol EvaluatorProtocol<Input, Subject> : Sendable
```

#### Overview

Conform to `EvaluatorProtocol` to create custom evaluators that measure the system’s output against expected criteria. Each evaluator returns an array of [`Metric`](metric.md) values — one per DataFrame column produced.

The protocol is parameterized by `Input` (the sample type). `Subject` is an associated type constrained to [`EvaluationSubject`](evaluationsubject.md), ensuring the subject’s value type matches the sample’s expected value type.

Conforming types must be `Sendable`.

```swift
struct MyEvaluator<Input: SampleProtocol>: EvaluatorProtocol
where Input.ExpectedValue: Sendable & Codable {
    let metric = Metric("Quality")

    func metrics(
        subject: ModelSubject<Input.ExpectedValue>,
        input: Input
    ) async throws -> [Metric] {
        return [metric.scoring(1.0)]
    }
}
```

## Topics

### Associated Types
- [associatedtype Input : SampleProtocol](evaluatorprotocol/input.md)
  The input sample type.
- [associatedtype Subject : EvaluationSubject](evaluatorprotocol/subject.md)
  The type of the subject produced by the system under test.
### Instance Methods
- [func metrics(subject: Self.Subject, input: Self.Input) async throws -> [Metric]](evaluatorprotocol/metrics(subject:input:).md)
  Computes metrics for the given subject, given the input sample.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Evaluator](evaluator.md)
- [ModelJudgeEvaluator](modeljudgeevaluator.md)
- [ToolCallEvaluator](toolcallevaluator.md)

## See Also

- [var evaluators: Self.Evaluators](evaluation/evaluators-swift.property.md)
  The evaluators to apply to each subject/sample pair.
- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  Shorthand for the evaluator array type, resolved per-conformance.
- [struct EvaluatorsBuilder](evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorprotocol)*