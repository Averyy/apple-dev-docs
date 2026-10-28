# NSTextList.MarkerFormat

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that describe marker symbols you can apply to list elements in text lists.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct MarkerFormat
```

```c
typedef NSString * NSTextListMarkerFormat;
```

## Overview

Select a marker symbol to apply to your list elements in your text list, then set it in [`markerFormat`](./markerformat-swift.property.md). Or, specify a marker symbol when you create a text list with [`init(markerFormat:options:)`](./init%28markerformat,options%29.md) or [`init(markerFormat:options:startingItemNumber:)`](./init%28markerformat,options,startingitemnumber%29.md).

## Topics

### Selecting a marker format
- [static let box: NSTextList.MarkerFormat](./markerformat-swift.struct/box.md)
  The value that represents a square-shaped marker that you can apply to a text list item.
- [static let check: NSTextList.MarkerFormat](./markerformat-swift.struct/check.md)
  The value that represents a checkmark-shaped marker that you can apply to a text list item.
- [static let circle: NSTextList.MarkerFormat](./markerformat-swift.struct/circle.md)
  The value that represents a circle-shaped marker that you can apply to a text list item.
- [static let decimal: NSTextList.MarkerFormat](./markerformat-swift.struct/decimal.md)
  The value that represents a decimal annotation marker that you can apply to a text list item.
- [static let diamond: NSTextList.MarkerFormat](./markerformat-swift.struct/diamond.md)
  The value that represents a diamond-shaped marker that you can apply to a text list item.
- [static let disc: NSTextList.MarkerFormat](./markerformat-swift.struct/disc.md)
  The value that represents a disc-shaped marker that you can apply to a text list item.
- [static let hyphen: NSTextList.MarkerFormat](./markerformat-swift.struct/hyphen.md)
  The value that represents a hyphen-shaped marker that you can apply to a text list item.
- [static let lowercaseAlpha: NSTextList.MarkerFormat](./markerformat-swift.struct/lowercasealpha.md)
  The value that represents a lowercase localized alphabetical marker you that can apply to a text list item.
- [static let lowercaseHexadecimal: NSTextList.MarkerFormat](./markerformat-swift.struct/lowercasehexadecimal.md)
  The value that represents a lowercase hexadecimal (base 16) numerical marker that you can apply to a text list item.
- [static let lowercaseLatin: NSTextList.MarkerFormat](./markerformat-swift.struct/lowercaselatin.md)
  The value that represents a lowercase Latin alphabetical marker that you can apply to a text list item.
- [static let lowercaseRoman: NSTextList.MarkerFormat](./markerformat-swift.struct/lowercaseroman.md)
  The value that represents a lowercase Roman numeral marker that you can apply to a text list item.
- [static let octal: NSTextList.MarkerFormat](./markerformat-swift.struct/octal.md)
  The value that represents an octal (base 8) numerical marker that you can apply to a text list item.
- [static let square: NSTextList.MarkerFormat](./markerformat-swift.struct/square.md)
  The value that represents a square-shaped marker that you can apply to a text list item.
- [static let uppercaseAlpha: NSTextList.MarkerFormat](./markerformat-swift.struct/uppercasealpha.md)
  The value that represents an uppercase localized alphabetical marker that you can apply to a text list item.
- [static let uppercaseHexadecimal: NSTextList.MarkerFormat](./markerformat-swift.struct/uppercasehexadecimal.md)
  The value that represents an uppercase hexadecimal (base 16) numerical marker that you can apply to a text list item.
- [static let uppercaseLatin: NSTextList.MarkerFormat](./markerformat-swift.struct/uppercaselatin.md)
  The value that represents an uppercase Latin alphabetical marker that you can apply to a text list item.
- [static let uppercaseRoman: NSTextList.MarkerFormat](./markerformat-swift.struct/uppercaseroman.md)
  The value that represents an uppercase Roman numeral marker that you can apply to a text list item.
### Initializing a marker format
- [init(String)](./markerformat-swift.struct/init%28_%29.md)
  Creates a new marker that you can apply to an item in a text list with the raw value you provide.
- [init(rawValue: String)](./markerformat-swift.struct/init%28rawvalue%29.md)
  Creates a new marker that you can apply to an item in a text list using the string you provide.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with markers
- [var markerFormat: NSTextList.MarkerFormat](./markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [func marker(forItemNumber: Int) -> String](./marker%28foritemnumber%29.md)
  Returns the computed value for a specific ordinal position in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/markerformat-swift.struct)*