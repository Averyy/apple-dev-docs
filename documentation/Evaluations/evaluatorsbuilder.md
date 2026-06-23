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
- [static func buildBlock(any EvaluatorProtocol<Sample, Subject>...) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildblock(_:).md)
- [static func buildExpression(any EvaluatorProtocol<Sample, Subject>) -> any EvaluatorProtocol<Sample, Subject>](evaluatorsbuilder/buildexpression(_:).md)
- [static func buildOptional([any EvaluatorProtocol<Sample, Subject>]?) -> [any EvaluatorProtocol<Sample, Subject>]](evaluatorsbuilder/buildoptional(_:).md)

## See Also

- [var evaluators: Self.Evaluators](evaluation/evaluators-swift.property.md)
  The evaluators to apply to each subject/sample pair.
- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  Shorthand for the evaluator array type, resolved per-conformance.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorsbuilder)*