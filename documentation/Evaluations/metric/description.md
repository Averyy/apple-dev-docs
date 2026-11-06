# description

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

A human-readable string representation of the metric, including its name, value, and optional rationale.

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
var description: String { get }
```

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
- [let metricDescription: String?](./metricdescription.md)
  An optional description of the associated metric.
- [Metric.Value](./value-swift.enum.md)
  A metric result value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/description)*