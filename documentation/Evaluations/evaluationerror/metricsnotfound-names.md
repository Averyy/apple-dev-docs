# EvaluationError.metricsNotFound(names:)

**Framework**: Evaluations  
**Kind**: case

One or more metric columns were not found in the evaluation results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case metricsNotFound(names: [String])
```

#### Discussion

The evaluation runner no longer throws this. When [`MetricsAggregator`](metricsaggregator.md) references a metric that no evaluator produced, the runner materializes it as an ignored column and logs a warning instead of failing the run. This case is deprecated and will be removed before general availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror/metricsnotfound(names:))*