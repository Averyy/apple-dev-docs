# paragraphSpacing(afterGlyphAt:withProposedLineFragmentRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of points of space added following a paragraph, in effect after the specified glyph.

**Availability**:
- macOS

## Declaration

```swift
func paragraphSpacing(afterGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: NSRect) -> CGFloat
```

```objc
- (CGFloat) paragraphSpacingAfterGlyphAtIndex:(NSUInteger) glyphIndex withProposedLineFragmentRect:(NSRect) rect;
```

#### Discussion

The `rect` argument specifies the line fragment rectangle of the last line in the paragraph.

The typesetter adds the number of points specified in the return value to the bottom of the line fragment rectangle specified by `rect` (but not to the used line fragment rectangle for that line). Paragraph spacing added after a paragraph correlates to the value in the [`paragraphSpacing`](../nsparagraphstyle/paragraphspacing.md) property of [`NSParagraphStyle`](../nsparagraphstyle.md). You can set the value of this property in an [`NSMutableParagraphStyle`](../nsmutableparagraphstyle.md) object.

## See Also

### Getting Spacing Information
- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./linespacing%28afterglyphat,withproposedlinefragmentrect%29.md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(beforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./paragraphspacing%28beforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the number of points of space added before a paragraph, which is in effect before the specified glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/paragraphspacing(afterglyphat:withproposedlinefragmentrect:))*