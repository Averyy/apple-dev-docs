# NSTextTab

**Framework**: UIKit  
**Kind**: class

A tab in a paragraph.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSTextTab
```

#### Overview

A text tab represents a tab in an [`NSParagraphStyle`](nsparagraphstyle.md) object, storing an alignment type and location. [`NSTextTab`](nstexttab.md) objects are most frequently used with the TextKit system and with [`NSRulerView`](https://developer.apple.com/documentation/appkit/nsrulerview) and [`NSRulerMarker`](https://developer.apple.com/documentation/appkit/nsrulermarker) objects.

The text system supports four alignment types: left, center, right, and decimal (based on the decimal separator character of the locale in effect). These alignment types are absolute, not based on the line sweep direction of text. For example, tabbed text is always positioned to the left of a right-aligned tab, whether the line sweep direction is left to right or right to left. A tab’s location, on the other hand, is relative to the back margin. A tab set at 1.5”, for example, is at 1.5” from the right in right to left text.

## Topics

### Creating a text tab
- [init(textAlignment: NSTextAlignment, location: CGFloat, options: [NSTextTab.OptionKey : Any])](nstexttab/init(textalignment:location:options:).md)
  Initializes a text tab with the specified text alignment, location, and options.
### Getting tab stop information
- [var location: CGFloat](nstexttab/location.md)
  The text tab’s ruler location relative to the back margin.
### Getting text tab information
- [var alignment: NSTextAlignment](nstexttab/alignment.md)
  The text alignment of the text tab.
- [var options: [NSTextTab.OptionKey : Any]](nstexttab/options.md)
  The dictionary of attributes for the text tab.
- [class func columnTerminators(for: Locale?) -> CharacterSet](nstexttab/columnterminators(for:).md)
  Returns the column terminators for the specified locale.
### Constants
- [NSParagraphStyle.TextTabType](../appkit/nsparagraphstyle/texttabtype.md)
  Constants that specify the type of tab stop.
- [NSTextTab.OptionKey](nstexttab/optionkey.md)
  The terminating character for a tab column.
### Deprecated
- [convenience init(type: NSParagraphStyle.TextTabType, location: CGFloat)](../appkit/nstexttab/init(type:location:).md)
  Initializes a newly allocated text tab with the specified alignment and location.
- [var tabStopType: NSParagraphStyle.TextTabType](../appkit/nstexttab/tabstoptype.md)
  The text tab’s type of tab stop.
### Initializers
- [init?(coder: NSCoder)](nstexttab/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextList](nstextlist.md)
  A section of text that forms a single list.
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md)
  Create and configure tables in attributed strings and display them in a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexttab)*