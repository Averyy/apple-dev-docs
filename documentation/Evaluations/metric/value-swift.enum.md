# Metric.Value

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

A metric result value.

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
enum Value
```

## Topics

### Enumeration Cases
- [Metric.Value.failing](./value-swift.enum/failing.md)
  A failing result.
- [Metric.Value.ignore](./value-swift.enum/ignore.md)
  The metric doesn’t apply to this sample and aggregators skip it.
- [Metric.Value.passing](./value-swift.enum/passing.md)
  A passing result.
- [Metric.Value.scoring(_:)](./value-swift.enum/scoring%28_%29.md)
  A numeric result.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a result
- [let name: String](./name.md)
  The name of the metric, used as the DataFrame column name.
- [let value: Metric.Value](./value-swift.property.md)
  The result value of this metric.
- [var doubleValue: Double?](./doublevalue.md)
  The numeric value of this metric.
- [let rationale: String?](./rationale.md)
  An optional rationale describing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/value-swift.enum)*