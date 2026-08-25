# metric

**Framework**: Evaluations  
**Kind**: property

A metric identifier that uses this dimension’s name.

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
var metric: Metric { get }
```

#### Discussion

Use this to reference the dimension’s metric in [`MetricsAggregator`](metricsaggregator.md) without repeating the name as a raw string:

```swift
let relevance = ScoreDimension("Relevance", scale: .numeric([...]))
aggregator.computeMean(of: relevance.metric)
```

## See Also

- [let scale: ScoringScale](scoredimension/scale.md)
  The scoring scale for this dimension.
- [let description: String?](scoredimension/description.md)
  An optional description providing additional context for the model judge about what this dimension measures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scoredimension/metric)*