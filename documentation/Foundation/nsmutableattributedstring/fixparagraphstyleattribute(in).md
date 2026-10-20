# fixParagraphStyleAttribute(in:)

**Framework**: Foundation  
**Kind**: method

Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func fixParagraphStyleAttribute(in range: NSRange)
```

#### Discussion

This method assigns the first paragraph style attribute value in each paragraph to all characters of the paragraph. This method extends the range as needed to cover the last paragraph partially contained. A paragraph is delimited by any of these characters, the longest possible sequence being preferred to any shorter:

- U+000D (`\r` or CR)
- U+000A (`\n` or LF)
- U+2029 (Unicode paragraph separator)  `\r\n`, in that order (also known as CRLF)

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range of characters.

## See Also

- [func fixAttributes(in: NSRange)](nsmutableattributedstring/fixattributes(in:).md)
  Cleans up font, paragraph style, and attachment attributes within the given range.
- [func fixAttachmentAttribute(in: NSRange)](nsmutableattributedstring/fixattachmentattribute(in:).md)
  Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [func fixFontAttribute(in: NSRange)](nsmutableattributedstring/fixfontattribute(in:).md)
  Fixes the font attribute in the specified range and assigns default fonts where appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixparagraphstyleattribute(in:))*