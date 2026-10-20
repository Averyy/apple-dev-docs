# AXNumericDataAxisDescriptor

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

An object that represents an axis of numerical data.

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
class AXNumericDataAxisDescriptor
```

```objc
@interface AXNumericDataAxisDescriptor : NSObject
```

## Topics

### Creating a numeric data axis
- [convenience init(title: String, range: ClosedRange<Double>, gridlinePositions: [Double], valueDescriptionProvider: (Double) -> String)](./axnumericdataaxisdescriptor/init%28title,range,gridlinepositions,valuedescriptionprovider%29.md)
  Creates a numeric data axis with the specified title, range, gridline positions, and value description provider closure.
- [convenience init(attributedTitle: NSAttributedString, range: ClosedRange<Double>, gridlinePositions: [Double], valueDescriptionProvider: (Double) -> String)](./axnumericdataaxisdescriptor/init%28attributedtitle,range,gridlinepositions,valuedescriptionprovider%29.md)
  Creates a numeric data axis with the specified attributed title, range, gridline positions, and value description provider closure.
### Specifying the value description
- [var valueDescriptionProvider: (Double) -> String](./axnumericdataaxisdescriptor/valuedescriptionprovider.md)
  A description to speak for a particular data value on the axis.
### Configuring the axis scale
- [var scaleType: AXNumericDataAxisDescriptor.ScaleType](./axnumericdataaxisdescriptor/scaletype-swift.property.md)
  The scale for the axis.
- [AXNumericDataAxisDescriptor.ScaleType](./axnumericdataaxisdescriptor/scaletype-swift.enum.md)
  Constants that describe the scale of a numeric axis.
### Configuring the axis range
- [var range: ClosedRange<Double>](./axnumericdataaxisdescriptor/range.md)
  A range that defines the minimum and maximum displayable values for the axis.
### Configuring the gridlines
- [var gridlinePositions: [Double]](./axnumericdataaxisdescriptor/gridlinepositions-5cfmw.md)
  The positions of the gridlines along the axis.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [AXDataAxisDescriptor](./axdataaxisdescriptor.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Axis representation
- [protocol AXDataAxisDescriptor](./axdataaxisdescriptor.md)
  The basic interface for a data axis in a chart.
- [class AXCategoricalDataAxisDescriptor](./axcategoricaldataaxisdescriptor.md)
  An object that represents an axis of categorical data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor)*