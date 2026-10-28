# fixAttributes(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) fixAttributesInRange:(NSRange) range;
```

## Discussion

Removes attachment attributes assigned to characters other than [`character`](../../AppKit/nstextattachment/character.md), assigns default fonts to characters with illegal fonts for their scripts and otherwise corrects font attribute assignments, and assigns the first paragraph style attribute value in each paragraph to all characters of the paragraph.

This method extends the range as needed to cover the last paragraph partially contained.

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of aRange lies beyond the end of the receiver’s characters.

`NSTextStorage` subclasses that return [`true`](../../Swift/true.md) from the [`fixesAttributesLazily`](../../AppKit/nstextstorage/fixesattributeslazily.md) method should avoid directly calling [`fixAttributes(in:)`](./fixattributes%28in%29.md) or else bracket such calls with [`beginEditing()`](./beginediting%28%29.md) and [`endEditing()`](./endediting%28%29.md) messages.

## Parameters

- `range`: The character range within which to fix attributes. Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## See Also

### Fixing Attributes After Changes
- [func fixAttachmentAttribute(in: NSRange)](./fixattachmentattribute%28in%29.md)
  Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [func fixFontAttribute(in: NSRange)](./fixfontattribute%28in%29.md)
  Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [func fixParagraphStyleAttribute(in: NSRange)](./fixparagraphstyleattribute%28in%29.md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/fixattributes(in:))*