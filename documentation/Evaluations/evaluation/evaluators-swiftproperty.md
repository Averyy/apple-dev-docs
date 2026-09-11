# evaluators

**Framework**: Evaluations  
**Kind**: property  
**Required**: Yes

The evaluators to apply to each sample and its corresponding subject.

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
@EvaluatorsBuilder
<Self.Sample, Self.Subject> var evaluators: Self.Evaluators { get }
```

## See Also

- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  The evaluator array type for this conformance.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [struct EvaluatorsBuilder](evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/evaluators-swift.property)*