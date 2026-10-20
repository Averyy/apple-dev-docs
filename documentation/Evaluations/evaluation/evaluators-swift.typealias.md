# Evaluation.Evaluators

**Framework**: Evaluations  
**Kind**: typealias  
**Role**: Type Alias

The evaluator array type for this conformance.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
typealias Evaluators = [any EvaluatorProtocol<Self.Sample, Self.Subject>]
```

## See Also

### Scoring results
- [var evaluators: Self.Evaluators](./evaluators-swift.property.md)
  The evaluators to apply to each sample and its corresponding subject.
- [protocol EvaluatorProtocol](../evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [struct EvaluatorsBuilder](../evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.
- [func aggregateMetrics(using: inout MetricsAggregator)](./aggregatemetrics%28using%29.md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/evaluators-swift.typealias)*