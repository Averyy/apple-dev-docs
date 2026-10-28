# AggregationOperation

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

The type of aggregation operation used to compute a summary statistic.

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
enum AggregationOperation
```

## Overview

Each case pairs a statistical function with the [`Metric`](./metric.md) it operates on, except [`AggregationOperation.custom(label:)`](./aggregationoperation/custom%28label%29.md) which represents a custom computation.

## Topics

### Enumeration Cases
- [AggregationOperation.custom(label:)](./aggregationoperation/custom%28label%29.md)
  A custom aggregation identified by its label.
- [AggregationOperation.maximum(of:)](./aggregationoperation/maximum%28of%29.md)
  The maximum of the metric’s values.
- [AggregationOperation.mean(of:)](./aggregationoperation/mean%28of%29.md)
  The arithmetic mean of the metric’s values.
- [AggregationOperation.median(of:)](./aggregationoperation/median%28of%29.md)
  The median of the metric’s values.
- [AggregationOperation.minimum(of:)](./aggregationoperation/minimum%28of%29.md)
  The minimum of the metric’s values.
- [AggregationOperation.mode(of:)](./aggregationoperation/mode%28of%29.md)
  The mode of the metric’s values.
- [AggregationOperation.standardDeviation(of:)](./aggregationoperation/standarddeviation%28of%29.md)
  The standard deviation of the metric’s values.
- [AggregationOperation.variance(of:)](./aggregationoperation/variance%28of%29.md)
  The variance of the metric’s values.
### Instance Properties
- [var label: String](./aggregationoperation/label.md)
  The display label this operation produces.
### Default Implementations
- [Decodable Implementations](./aggregationoperation/decodable-implementations.md)
- [Encodable Implementations](./aggregationoperation/encodable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting aggregate results
- [struct AggregateMetric](./aggregatemetric.md)
  An aggregate statistic computed from a metric’s results across the evaluation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/aggregationoperation)*