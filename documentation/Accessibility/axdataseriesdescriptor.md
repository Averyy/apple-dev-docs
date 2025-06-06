# AXDataSeriesDescriptor

**Framework**: Accessibility  
**Kind**: class

An object that represents a series of data points.

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
class AXDataSeriesDescriptor
```

## Topics

### Creating a data series
- [init(name: String, isContinuous: Bool, dataPoints: [AXDataPoint])](axdataseriesdescriptor/init(name:iscontinuous:datapoints:).md)
  Creates a data series with the specified name, a Boolean value that indicates whether the series is continuous, and data points.
- [init(attributedName: NSAttributedString, isContinuous: Bool, dataPoints: [AXDataPoint])](axdataseriesdescriptor/init(attributedname:iscontinuous:datapoints:).md)
  Creates a data series with the specified attributed name, a Boolean value that indicates whether the series is continuous, and data points.
### Naming the series
- [var name: String?](axdataseriesdescriptor/name.md)
  The name of the data series.
- [var attributedName: NSAttributedString](axdataseriesdescriptor/attributedname.md)
  An attributed version of the data series name.
### Configuring the data points
- [var isContinuous: Bool](axdataseriesdescriptor/iscontinuous.md)
  A Boolean value that determines whether the data series is continuous.
- [var dataPoints: [AXDataPoint]](axdataseriesdescriptor/datapoints.md)
  The data points that the series contains.
- [class AXDataPoint](axdatapoint.md)
  An object that represents a single data point in a chart.

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

- [class AXDataPoint](axdatapoint.md)
  An object that represents a single data point in a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdataseriesdescriptor)*