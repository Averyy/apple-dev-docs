# AXDataAxisDescriptor

**Framework**: Accessibility  
**Kind**: protocol

The basic interface for a data axis in a chart.

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
protocol AXDataAxisDescriptor : NSCopying
```

#### Overview

Each [`AXChart`](axchart.md) requires at least two [`AXDataAxisDescriptor`](axdataaxisdescriptor.md) objects to describe an x-axis and a y-axis.

## Topics

### Specifying the title
- [var title: String](axdataaxisdescriptor/title.md)
  The title of the axis.
- [var attributedTitle: NSAttributedString](axdataaxisdescriptor/attributedtitle.md)
  An attributed version of the axis title.

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
### Conforming Types
- [AXCategoricalDataAxisDescriptor](axcategoricaldataaxisdescriptor.md)
- [AXNumericDataAxisDescriptor](axnumericdataaxisdescriptor.md)

## See Also

- [class AXCategoricalDataAxisDescriptor](axcategoricaldataaxisdescriptor.md)
  An object that represents an axis of categorical data.
- [class AXNumericDataAxisDescriptor](axnumericdataaxisdescriptor.md)
  An object that represents an axis of numerical data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdataaxisdescriptor)*