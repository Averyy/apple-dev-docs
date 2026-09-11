# custom(of:label:_:)

**Framework**: Evaluations  
**Kind**: method

Computes a custom aggregation from a single metric’s results.

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
mutating func custom(of metric: Metric, label: String, _ body: ([Double]) -> Double)
```

## Parameters

- `metric`: The metric to aggregate.
- `label`: The label for this statistic in the aggregated results.
- `body`: A closure that receives the metric’s values and returns a computed statistic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metricsaggregator/custom(of:label:_:))*