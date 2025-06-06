# AXDataPoint

**Framework**: Accessibility  
**Kind**: class

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

## Topics

### Creating a data point
- [convenience init(x: String, y: Double?, additionalValues: [AXDataPoint.Value], label: String?)](axdatapoint/init(x:y:additionalvalues:label:)-83xvg.md)
  Creates a data point with the specified x-value, y-value, additional values, and label.
- [convenience init(x: Double, y: Double?, additionalValues: [AXDataPoint.Value], label: String?)](axdatapoint/init(x:y:additionalvalues:label:)-4v3sb.md)
  Creates a data point with the specified x-value, y-value, additional values, and label.
### Specifying the data value
- [var xValue: AXDataPointValue](axdatapoint/xvalue.md)
  The value of the x-axis for the data point.
- [var yValue: AXDataPointValue?](axdatapoint/yvalue.md)
  The value of the y-axis for the data point.
- [class AXDataPointValue](axdatapointvalue.md)
  A single data value.
- [AXDataPoint.Value](axdatapoint/value.md)
  Constants that describe types of data values.
### Specifying the label
- [var label: String?](axdatapoint/label.md)
  The label for the data point.
- [var attributedLabel: NSAttributedString?](axdatapoint/attributedlabel.md)
  An attributed version of the label for the data point.

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

- [class AXDataSeriesDescriptor](axdataseriesdescriptor.md)
  An object that represents a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapoint)*