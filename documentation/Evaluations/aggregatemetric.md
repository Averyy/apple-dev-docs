# AggregateMetric

**Framework**: Evaluations  
**Kind**: struct

An aggregate statistic computed from a metric’s results across the evaluation dataset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AggregateMetric
```

#### Overview

```swift
let accuracy = Metric("Accuracy")
let op = AggregationOperation.mean(of: accuracy)
print(op.label) // "Mean of Accuracy"
```

The summary DataFrame stores one `AggregateMetric` for each column. Each value records the operation that produced it, and derives its display label and source metric name from the operation.

## Topics

### Instance Properties
- [let group: String?](aggregatemetric/group.md)
  The group this aggregate belongs to, if any.
- [var label: String](aggregatemetric/label.md)
  The display label for this aggregate.
- [let operation: AggregationOperation](aggregatemetric/operation.md)
  The aggregation operation that produced this value.
- [var sourceMetric: String?](aggregatemetric/sourcemetric.md)
  The name of the source metric.
- [let value: Double](aggregatemetric/value.md)
  The aggregate value.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum AggregationOperation](aggregationoperation.md)
  The type of aggregation operation used to compute a summary statistic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/aggregatemetric)*