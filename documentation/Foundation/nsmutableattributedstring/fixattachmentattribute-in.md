# fixAttachmentAttribute(in:)

**Framework**: Foundation  
**Kind**: method

Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func fixAttachmentAttribute(in range: NSRange)
```

#### Discussion

The method preserves the attachment attribute on the [`character`](https://developer.apple.com/documentation/AppKit/NSTextAttachment/character) special character. The method raises a [`rangeException`](nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the string’s characters.

## Parameters

- `range`: The range of characters.

## See Also

- [func fixAttributes(in: NSRange)](nsmutableattributedstring/fixattributes(in:).md)
  Cleans up font, paragraph style, and attachment attributes within the given range.
- [func fixFontAttribute(in: NSRange)](nsmutableattributedstring/fixfontattribute(in:).md)
  Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [func fixParagraphStyleAttribute(in: NSRange)](nsmutableattributedstring/fixparagraphstyleattribute(in:).md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixattachmentattribute(in:))*