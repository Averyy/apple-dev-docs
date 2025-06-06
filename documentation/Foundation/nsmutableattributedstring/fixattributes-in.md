# fixAttributes(in:)

**Framework**: Foundation  
**Kind**: method

Cleans up font, paragraph style, and attachment attributes within the given range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fixAttributes(in range: NSRange)
```

#### Discussion

Removes attachment attributes assigned to characters other than [`character`](https://developer.apple.com/documentation/AppKit/NSTextAttachment/character), assigns default fonts to characters with illegal fonts for their scripts and otherwise corrects font attribute assignments, and assigns the first paragraph style attribute value in each paragraph to all characters of the paragraph.

This method extends the range as needed to cover the last paragraph partially contained.

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of aRange lies beyond the end of the receiver’s characters.

`NSTextStorage` subclasses that return [`true`](https://developer.apple.com/documentation/swift/true) from the [`fixesAttributesLazily`](https://developer.apple.com/documentation/AppKit/NSTextStorage/fixesAttributesLazily) method should avoid directly calling [`fixAttributes(in:)`](nsmutableattributedstring/fixattributes(in:).md) or else bracket such calls with [`beginEditing()`](nsmutableattributedstring/beginediting().md) and [`endEditing()`](nsmutableattributedstring/endediting().md) messages.

## Parameters

- `range`: The character range within which to fix attributes. Raises an   if any part of   lies beyond the end of the receiver’s characters.

## See Also

- [func fixAttachmentAttribute(in: NSRange)](nsmutableattributedstring/fixattachmentattribute(in:).md)
  Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [func fixFontAttribute(in: NSRange)](nsmutableattributedstring/fixfontattribute(in:).md)
  Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [func fixParagraphStyleAttribute(in: NSRange)](nsmutableattributedstring/fixparagraphstyleattribute(in:).md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixattributes(in:))*