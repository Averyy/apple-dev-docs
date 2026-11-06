# computeMinimum(of:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Instance Method

Computes the minimum value of a metric and adds it to the group.

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
mutating func computeMinimum(of metric: Metric)
```

## Parameters

- `metric`: The metric to aggregate.

## See Also

### Computing standard aggregations
- [func computeMean(of: Metric)](./computemean%28of%29.md)
  Computes the mean of a metric and adds it to the group.
- [func computeMedian(of: Metric)](./computemedian%28of%29.md)
  Computes the median of a metric and adds it to the group.
- [func computeMode(of: Metric)](./computemode%28of%29.md)
  Computes the mode of a metric and adds it to the group.
- [func computeMaximum(of: Metric)](./computemaximum%28of%29.md)
  Computes the maximum value of a metric and adds it to the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metricsaggregator/group/computeminimum(of:))*