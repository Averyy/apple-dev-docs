# metric

**Framework**: Evaluations  
**Kind**: property

A metric identifier derived from this dimension’s name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var metric: Metric { get }
```

#### Discussion

Use this to reference the dimension’s metric in [`MetricsAggregator`](metricsaggregator.md) without repeating the name as a raw string:

```swift
let relevance = ScoreDimension("Relevance", scale: .numeric([...]))
aggregator.computeMean(of: relevance.metric)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoredimension/metric)*