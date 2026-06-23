# evaluators

**Framework**: Evaluations  
**Kind**: property  
**Required**: Yes

The evaluators to apply to each subject/sample pair.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@EvaluatorsBuilder
<Self.Sample, Self.Subject> var evaluators: Self.Evaluators { get }
```

## See Also

- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  Shorthand for the evaluator array type, resolved per-conformance.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [struct EvaluatorsBuilder](evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.
- [func aggregateMetrics(using: inout MetricsAggregator)](evaluation/aggregatemetrics(using:).md)
  Aggregates the collected metric results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/evaluators-swift.property)*