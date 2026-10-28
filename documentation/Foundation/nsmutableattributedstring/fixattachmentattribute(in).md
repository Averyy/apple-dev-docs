# fixAttachmentAttribute(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func fixAttachmentAttribute(in range: NSRange)
```

```objc
- (void) fixAttachmentAttributeInRange:(NSRange) range;
```

## Discussion

The method preserves the attachment attribute on the [`character`](../../AppKit/nstextattachment/character.md) special character. The method raises a [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the string’s characters.

## Parameters

- `range`: The range of characters.

## See Also

### Fixing Attributes After Changes
- [func fixAttributes(in: NSRange)](./fixattributes%28in%29.md)
  Cleans up font, paragraph style, and attachment attributes within the given range.
- [func fixFontAttribute(in: NSRange)](./fixfontattribute%28in%29.md)
  Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [func fixParagraphStyleAttribute(in: NSRange)](./fixparagraphstyleattribute%28in%29.md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixattachmentattribute(in:))*