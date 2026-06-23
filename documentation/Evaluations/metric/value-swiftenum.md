# Metric.Value

**Framework**: Evaluations  
**Kind**: enum

A metric result value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Value
```

## Topics

### Enumeration Cases
- [Metric.Value.failing](metric/value-swift.enum/failing.md)
  A negative/failing result.
- [Metric.Value.ignore](metric/value-swift.enum/ignore.md)
  The metric is not applicable for this sample and should be excluded from aggregation.
- [Metric.Value.passing](metric/value-swift.enum/passing.md)
  A positive/passing result.
- [Metric.Value.scoring(_:)](metric/value-swift.enum/scoring(_:).md)
  A numeric result.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let name: String](metric/name.md)
  The name of the metric, used as the DataFrame column name.
- [let value: Metric.Value](metric/value-swift.property.md)
  The result value of this metric.
- [var doubleValue: Double?](metric/doublevalue.md)
  The numeric value of this metric, or `nil` for ignored metrics.
- [let rationale: String?](metric/rationale.md)
  An optional rationale describing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/value-swift.enum)*