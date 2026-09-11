# metricsNotFound

**Framework**: Evaluations  
**Kind**: property

Metric names referenced by `MetricsAggregator` that no evaluator produced.

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
var metricsNotFound: [String]
```

#### Discussion

Typically a typo or missing evaluator; empty on a clean run and when no sample produced inference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors/metricsnotfound)*