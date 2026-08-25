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
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
enum Value
```

## Topics

### Enumeration Cases
- [Metric.Value.failing](metric/value-swift.enum/failing.md)
  A failing result.
- [Metric.Value.ignore](metric/value-swift.enum/ignore.md)
  The metric doesn’t apply to this sample and aggregators skip it.
- [Metric.Value.passing](metric/value-swift.enum/passing.md)
  A passing result.
- [Metric.Value.scoring(_:)](metric/value-swift.enum/scoring(_:).md)
  A numeric result.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let name: String](metric/name.md)
  The name of the metric, used as the DataFrame column name.
- [let value: Metric.Value](metric/value-swift.property.md)
  The result value of this metric.
- [var doubleValue: Double?](metric/doublevalue.md)
  The numeric value of this metric.
- [let rationale: String?](metric/rationale.md)
  An optional rationale describing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/value-swift.enum)*