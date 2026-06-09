# AggregationOperation

**Framework**: Evaluations  
**Kind**: enum

The type of aggregation operation used to compute a summary statistic.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum AggregationOperation
```

#### Overview

Each case pairs a statistical function with the [`Metric`](metric.md) it operates on, except [`AggregationOperation.custom(label:)`](aggregationoperation/custom(label:).md) which represents a custom computation.

## Topics

### Enumeration Cases
- [AggregationOperation.custom(label:)](aggregationoperation/custom(label:).md)
  A custom aggregation identified by its label.
- [AggregationOperation.maximum(of:)](aggregationoperation/maximum(of:).md)
  The maximum of the metric’s values.
- [AggregationOperation.mean(of:)](aggregationoperation/mean(of:).md)
  The arithmetic mean of the metric’s values.
- [AggregationOperation.median(of:)](aggregationoperation/median(of:).md)
  The median of the metric’s values.
- [AggregationOperation.minimum(of:)](aggregationoperation/minimum(of:).md)
  The minimum of the metric’s values.
- [AggregationOperation.mode(of:)](aggregationoperation/mode(of:).md)
  The mode of the metric’s values.
- [AggregationOperation.standardDeviation(of:)](aggregationoperation/standarddeviation(of:).md)
  The standard deviation of the metric’s values.
- [AggregationOperation.variance(of:)](aggregationoperation/variance(of:).md)
  The variance of the metric’s values.
### Instance Properties
- [var label: String](aggregationoperation/label.md)
  The display label derived from this operation.
### Default Implementations
- [Decodable Implementations](aggregationoperation/decodable-implementations.md)
- [Encodable Implementations](aggregationoperation/encodable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AggregateMetric](aggregatemetric.md)
  An aggregate statistic computed from a metric’s results across the evaluation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/aggregationoperation)*