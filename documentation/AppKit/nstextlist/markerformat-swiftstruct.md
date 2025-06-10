# NSTextList.MarkerFormat

**Framework**: AppKit  
**Kind**: struct

Constants that describe marker symbols you can apply to list elements in text lists.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct MarkerFormat
```

#### Overview

Select a marker symbol to apply to your list elements in your text list, then set it in [`markerFormat`](nstextlist/markerformat-swift.property.md). Or, specify a marker symbol when you create a text list with [`init(markerFormat:options:)`](nstextlist/init(markerformat:options:).md) or [`init(markerFormat:options:startingItemNumber:)`](nstextlist/init(markerformat:options:startingitemnumber:).md).

## Topics

### Selecting a marker format
- [static let box: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/box.md)
  The value that represents a square-shaped marker that you can apply to a text list item.
- [static let check: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/check.md)
  The value that represents a checkmark-shaped marker that you can apply to a text list item.
- [static let circle: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/circle.md)
  The value that represents a circle-shaped marker that you can apply to a text list item.
- [static let decimal: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/decimal.md)
  The value that represents a decimal annotation marker that you can apply to a text list item.
- [static let diamond: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/diamond.md)
  The value that represents a diamond-shaped marker that you can apply to a text list item.
- [static let disc: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/disc.md)
  The value that represents a disc-shaped marker that you can apply to a text list item.
- [static let hyphen: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/hyphen.md)
  The value that represents a hyphen-shaped marker that you can apply to a text list item.
- [static let lowercaseAlpha: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/lowercasealpha.md)
  The value that represents a lowercase localized alphabetical marker you that can apply to a text list item.
- [static let lowercaseHexadecimal: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/lowercasehexadecimal.md)
  The value that represents a lowercase hexadecimal (base 16) numerical marker that you can apply to a text list item.
- [static let lowercaseLatin: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/lowercaselatin.md)
  The value that represents a lowercase Latin alphabetical marker that you can apply to a text list item.
- [static let lowercaseRoman: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/lowercaseroman.md)
  The value that represents a lowercase Roman numeral marker that you can apply to a text list item.
- [static let octal: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/octal.md)
  The value that represents an octal (base 8) numerical marker that you can apply to a text list item.
- [static let square: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/square.md)
  The value that represents a square-shaped marker that you can apply to a text list item.
- [static let uppercaseAlpha: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/uppercasealpha.md)
  The value that represents an uppercase localized alphabetical marker that you can apply to a text list item.
- [static let uppercaseHexadecimal: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/uppercasehexadecimal.md)
  The value that represents an uppercase hexadecimal (base 16) numerical marker that you can apply to a text list item.
- [static let uppercaseLatin: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/uppercaselatin.md)
  The value that represents an uppercase Latin alphabetical marker that you can apply to a text list item.
- [static let uppercaseRoman: NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct/uppercaseroman.md)
  The value that represents an uppercase Roman numeral marker that you can apply to a text list item.
### Initializing a marker format
- [init(String)](nstextlist/markerformat-swift.struct/init(_:).md)
  Creates a new marker that you can apply to an item in a text list with the raw value you provide.
- [init(rawValue: String)](nstextlist/markerformat-swift.struct/init(rawvalue:).md)
  Creates a new marker that you can apply to an item in a text list using the string you provide.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var markerFormat: NSTextList.MarkerFormat](nstextlist/markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [func marker(forItemNumber: Int) -> String](nstextlist/marker(foritemnumber:).md)
  Returns the computed value for a specific ordinal position in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/markerformat-swift.struct)*