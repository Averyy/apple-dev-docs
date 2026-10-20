# fixFontAttribute(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Fixes the font attribute in the specified range and assigns default fonts where appropriate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func fixFontAttribute(in range: NSRange)
```

```objc
- (void) fixFontAttributeInRange:(NSRange) range;
```

#### Discussion

This method assigns default fonts to characters with illegal fonts for their scripts and corrects other font attribute assignments. For example, Kanji characters assigned a Latin font are reassigned an appropriate Kanji font. Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range of characters.

## See Also

### Fixing Attributes After Changes
- [func fixAttributes(in: NSRange)](./fixattributes%28in%29.md)
  Cleans up font, paragraph style, and attachment attributes within the given range.
- [func fixAttachmentAttribute(in: NSRange)](./fixattachmentattribute%28in%29.md)
  Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [func fixParagraphStyleAttribute(in: NSRange)](./fixparagraphstyleattribute%28in%29.md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixfontattribute(in:))*