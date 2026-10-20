# MetricsAggregator.Group

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A grouped collection of related metrics.

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
struct Group
```

#### Overview

Use `Group` within [`group(_:_:)`](./group%28_,_%29.md) to add metrics to display together.

## Topics

### Instance Properties
- [let name: String](./group/name.md)
  The name of this group.
### Instance Methods
- [func computeMaximum(of: Metric)](./group/computemaximum%28of%29.md)
  Computes the maximum value of a metric and adds it to the group.
- [func computeMean(of: Metric)](./group/computemean%28of%29.md)
  Computes the mean of a metric and adds it to the group.
- [func computeMedian(of: Metric)](./group/computemedian%28of%29.md)
  Computes the median of a metric and adds it to the group.
- [func computeMinimum(of: Metric)](./group/computeminimum%28of%29.md)
  Computes the minimum value of a metric and adds it to the group.
- [func computeMode(of: Metric)](./group/computemode%28of%29.md)
  Computes the mode of a metric and adds it to the group.
- [func computeStandardDeviation(of: Metric)](./group/computestandarddeviation%28of%29.md)
  Computes the standard deviation of a metric and adds it to the group.
- [func computeVariance(of: Metric)](./group/computevariance%28of%29.md)
  Computes the variance of a metric and adds it to the group.
- [func custom(of: Metric, label: String, ([Double]) -> Double)](./group/custom%28of,label,_%29.md)
  Computes a custom aggregation and adds it to the group.

## See Also

### Grouping metrics
- [func group(String, (inout MetricsAggregator.Group) -> Void)](./group%28_,_%29.md)
  Creates a group of related metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metricsaggregator/group)*