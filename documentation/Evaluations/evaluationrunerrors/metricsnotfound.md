# metricsNotFound

**Framework**: Evaluations  
**Kind**: property

Metric names referenced by `MetricsAggregator` that no evaluator produced.

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
var metricsNotFound: [String]
```

#### Discussion

Typically a typo or missing evaluator; empty on a clean run and when no sample produced inference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors/metricsnotfound)*