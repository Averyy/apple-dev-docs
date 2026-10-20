# AXDataPointValue

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

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

```objc
@interface AXDataPointValue : NSObject
```

#### Overview

An [`AXDataPointValue`](./axdatapointvalue.md) can be either numeric or categorical. Data points in a numeric axis use the [`number`](./axdatapointvalue/number.md) property, and data points in a categorical axis use the [`category`](./axdatapointvalue/category.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Specifying the data value
- [var xValue: AXDataPointValue](./axdatapoint/xvalue.md)
  The value of the x-axis for the data point.
- [var yValue: AXDataPointValue?](./axdatapoint/yvalue.md)
  The value of the y-axis for the data point.
- [AXDataPoint.Value](./axdatapoint/value.md)
  Constants that describe types of data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapointvalue)*