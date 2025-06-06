# paragraphSpacing(beforeGlyphAt:withProposedLineFragmentRect:)

**Framework**: AppKit  
**Kind**: method

Returns the number of points of space added before a paragraph, which is in effect before the specified glyph.

**Availability**:
- macOS ?+

## Declaration

```swift
func paragraphSpacing(beforeGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: NSRect) -> CGFloat
```

#### Discussion

The `rect` argument specifies the line fragment rectangle of the first line in the paragraph.

The typesetter adds the number of points specified in the return value to the top of the line fragment rectangle specified by `rect` (but not to the used line fragment rectangle for that line). Paragraph spacing added before a paragraph correlates to the value in the [`paragraphSpacingBefore`](nsparagraphstyle/paragraphspacingbefore.md) property of [`NSParagraphStyle`](nsparagraphstyle.md). You can set the value of this property in an [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md) object.

## See Also

- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nsatstypesetter/linespacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nsatstypesetter/paragraphspacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the number of points of space added following a paragraph, in effect after the specified glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/paragraphspacing(beforeglyphat:withproposedlinefragmentrect:))*