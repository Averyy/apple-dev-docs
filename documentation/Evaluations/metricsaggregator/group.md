# MetricsAggregator.Group

**Framework**: Evaluations  
**Kind**: struct

A grouped collection of related metrics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Group
```

#### Overview

Use `Group` within [`group(_:_:)`](metricsaggregator/group(_:_:).md) to add metrics that should be displayed together.

## Topics

### Instance Properties
- [let name: String](metricsaggregator/group/name.md)
  The name of this group.
### Instance Methods
- [func computeMaximum(of: Metric)](metricsaggregator/group/computemaximum(of:).md)
  Computes the maximum value of a metric and adds it to the group.
- [func computeMean(of: Metric)](metricsaggregator/group/computemean(of:).md)
  Computes the mean of a metric and adds it to the group.
- [func computeMedian(of: Metric)](metricsaggregator/group/computemedian(of:).md)
  Computes the median of a metric and adds it to the group.
- [func computeMinimum(of: Metric)](metricsaggregator/group/computeminimum(of:).md)
  Computes the minimum value of a metric and adds it to the group.
- [func computeMode(of: Metric)](metricsaggregator/group/computemode(of:).md)
  Computes the mode of a metric and adds it to the group.
- [func computeStandardDeviation(of: Metric)](metricsaggregator/group/computestandarddeviation(of:).md)
  Computes the standard deviation of a metric and adds it to the group.
- [func computeVariance(of: Metric)](metricsaggregator/group/computevariance(of:).md)
  Computes the variance of a metric and adds it to the group.
- [func custom(of: Metric, label: String, ([Double]) -> Double)](metricsaggregator/group/custom(of:label:_:).md)
  Computes a custom aggregation and adds it to the group.

## See Also

- [func group(String, (inout MetricsAggregator.Group) -> Void)](metricsaggregator/group(_:_:).md)
  Creates a group of related metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metricsaggregator/group)*