# EvaluatorsBuilder

**Framework**: Evaluations  
**Kind**: struct

A result builder that enables declarative evaluator lists.

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
@resultBuilder
struct EvaluatorsBuilder<Sample, Subject> where Sample : SampleProtocol, Subject : EvaluationSubject
```

#### Overview

Apply this builder to the `evaluators` property to remove the need for explicit array literals and type annotations:

```swift
@EvaluatorsBuilder<ModelSample<String>, ModelSubject<String>>
func buildEvaluators() -> [any EvaluatorProtocol<ModelSample<String>, ModelSubject<String>>] {
    Evaluator<ModelSample<String>> { sample, subject in
        Metric("Match").scoring(1.0)
    }
}
```

## Topics

### Type Methods
- [static func buildExpression(any EvaluatorProtocol<Sample, Subject>) -> any EvaluatorProtocol<Sample, Subject>](evaluatorsbuilder/buildexpression(_:).md)
  Wraps a single evaluator expression into the builder pipeline.
- [static func buildOptional([any EvaluatorProtocol<Sample, Subject>]?) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildoptional(_:).md)
  Provides an empty array when an optional evaluator block is absent.
- [static func buildPartialBlock(accumulated: [any EvaluatorProtocol<Sample, Subject>], next: [any EvaluatorProtocol<Sample, Subject>]) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildpartialblock(accumulated:next:)-7lvjo.md)
- [static func buildPartialBlock(accumulated: [any EvaluatorProtocol<Sample, Subject>], next: any EvaluatorProtocol<Sample, Subject>) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildpartialblock(accumulated:next:)-88zf9.md)
- [static func buildPartialBlock(first: [any EvaluatorProtocol<Sample, Subject>]) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildpartialblock(first:)-3o70b.md)
- [static func buildPartialBlock(first: any EvaluatorProtocol<Sample, Subject>) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildpartialblock(first:)-875f9.md)

## See Also

- [var evaluators: Self.Evaluators](evaluation/evaluators-swift.property.md)
  The evaluators to apply to each sample and its corresponding subject.
- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  The evaluator array type for this conformance.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorsbuilder)*