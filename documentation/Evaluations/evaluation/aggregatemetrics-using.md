# aggregateMetrics(using:)

**Framework**: Evaluations  
**Kind**: method  
**Required**: Yes

Aggregates the collected metric results.

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
func aggregateMetrics(using aggregator: inout MetricsAggregator)
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)
- [Scoring with model-judge evaluators](scoring-with-model-as-judge-evaluators.md)

## Parameters

- `aggregator`: The aggregator for computing statistics.

## See Also

- [var evaluators: Self.Evaluators](evaluation/evaluators-swift.property.md)
  The evaluators to apply to each sample and its corresponding subject.
- [Evaluation.Evaluators](evaluation/evaluators-swift.typealias.md)
  The evaluator array type for this conformance.
- [protocol EvaluatorProtocol](evaluatorprotocol.md)
  A type that evaluates subjects and produces metrics.
- [struct EvaluatorsBuilder](evaluatorsbuilder.md)
  A result builder that enables declarative evaluator lists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/aggregatemetrics(using:))*