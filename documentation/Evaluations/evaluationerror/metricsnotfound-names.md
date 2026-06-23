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

## Declaration

```swift
case metricsNotFound(names: [String])
```

#### Discussion

This occurs when [`MetricsAggregator`](metricsaggregator.md) references metrics that no evaluator produced during the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationerror/metricsnotfound(names:))*