# AXCategoricalDataAxisDescriptor

**Framework**: Accessibility  
**Kind**: class

An object that represents an axis of categorical data.

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
class AXCategoricalDataAxisDescriptor
```

#### Overview

A categorical data axis divides information into groups, or categories. For example, a categorical axis may represent blood type data divided into the possible categories , , , and .

## Topics

### Creating a categorial data axis
- [init(title: String, categoryOrder: [String])](axcategoricaldataaxisdescriptor/init(title:categoryorder:).md)
  Creates a categorical data axis with the specified title and an array of categories in the specified order.
- [init(attributedTitle: NSAttributedString, categoryOrder: [String])](axcategoricaldataaxisdescriptor/init(attributedtitle:categoryorder:).md)
  Creates a categorical data axis with the specified attributed title and an array of categories in the specified order.
### Configuring the order of categories
- [var categoryOrder: [String]](axcategoricaldataaxisdescriptor/categoryorder.md)
  A list of every category value for the axis in the order they appear visually in the graph or legend.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [AXDataAxisDescriptor](axdataaxisdescriptor.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AXDataAxisDescriptor](axdataaxisdescriptor.md)
  The basic interface for a data axis in a chart.
- [class AXNumericDataAxisDescriptor](axnumericdataaxisdescriptor.md)
  An object that represents an axis of numerical data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcategoricaldataaxisdescriptor)*