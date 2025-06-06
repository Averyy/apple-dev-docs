# AXDataPointValue

**Framework**: Accessibility  
**Kind**: class

A single data value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AXDataPointValue
```

#### Overview

An [`AXDataPointValue`](axdatapointvalue.md) can be either numeric or categorical. Data points in a numeric axis use the [`number`](axdatapointvalue/number.md) property, and data points in a categorical axis use the [`category`](axdatapointvalue/category.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var xValue: AXDataPointValue](axdatapoint/xvalue.md)
  The value of the x-axis for the data point.
- [var yValue: AXDataPointValue?](axdatapoint/yvalue.md)
  The value of the y-axis for the data point.
- [AXDataPoint.Value](axdatapoint/value.md)
  Constants that describe types of data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapointvalue)*