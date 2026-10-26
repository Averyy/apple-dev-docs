# AXDataPoint

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

An object that represents a single data point in a chart.

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
class AXDataPoint
```

```objc
@interface AXDataPoint : NSObject
```

## Topics

### Creating a data point
- [convenience init(x: String, y: Double?, additionalValues: [AXDataPoint.Value], label: String?)](./axdatapoint/init%28x,y,additionalvalues,label%29-83xvg.md)
  Creates a data point with the specified x-value, y-value, additional values, and label.
- [convenience init(x: Double, y: Double?, additionalValues: [AXDataPoint.Value], label: String?)](./axdatapoint/init%28x,y,additionalvalues,label%29-4v3sb.md)
  Creates a data point with the specified x-value, y-value, additional values, and label.
- [- initWithX:y:](./axdatapoint/initwithx_y_.md)
  Creates a data point with the specified x- and y-values.
- [- initWithX:y:additionalValues:](./axdatapoint/initwithx_y_additionalvalues_.md)
  Creates a data point with the specified x-value, y-value, and additional values.
- [- initWithX:y:additionalValues:label:](./axdatapoint/initwithx_y_additionalvalues_label_.md)
  Creates a data point with the specified x-value, y-value, additional values, and label.
### Specifying the data value
- [var xValue: AXDataPointValue](./axdatapoint/xvalue.md)
  The value of the x-axis for the data point.
- [var yValue: AXDataPointValue?](./axdatapoint/yvalue.md)
  The value of the y-axis for the data point.
- [class AXDataPointValue](./axdatapointvalue.md)
  A single data value.
- [AXDataPoint.Value](./axdatapoint/value.md)
  Constants that describe types of data values.
- [additionalValues](./axdatapoint/additionalvalues.md)
  An array of values for additional axes for the data point.
### Specifying the label
- [var label: String?](./axdatapoint/label.md)
  The label for the data point.
- [var attributedLabel: NSAttributedString?](./axdatapoint/attributedlabel.md)
  An attributed version of the label for the data point.

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

### Data representation
- [class AXDataSeriesDescriptor](./axdataseriesdescriptor.md)
  An object that represents a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapoint)*