# Evaluation.Evaluators

**Framework**: Evaluations  
**Kind**: typealias

The evaluator array type for this conformance.

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
typealias Evaluators = [any EvaluatorProtocol<Self.Sample, Self.Subject>]
```

## See Also

- [var evaluators: Self.Evaluators](evaluation/evaluators-swift.property.md)
  The evaluators to apply to each sample and its corresponding subject.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [struct EvaluatorsBuilder](evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/evaluators-swift.typealias)*