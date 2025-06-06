# paragraphSpacing(beforeGlyphAt:withProposedLineFragmentRect:)

**Framework**: AppKit  
**Kind**: method

Returns the number of points of space—added before a paragraph—that is in effect before the specified glyph.

**Availability**:
- macOS ?+

## Declaration

```swift
func paragraphSpacing(beforeGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: NSRect) -> CGFloat
```

#### Return Value

The number of points of space—added before a paragraph—that is in effect before the glyph specified by `glyphIndex`.

#### Discussion

The typesetter adds the number of points specified in the return value to the top of the line fragment rectangle specified by `rect` (but not to the used line fragment rectangle for that line). Paragraph spacing added before a paragraph correlates to the value returned by the [`paragraphSpacingBefore`](nsparagraphstyle/paragraphspacingbefore.md) method of [`NSParagraphStyle`](nsparagraphstyle.md), which you can set using the [`paragraphSpacingBefore`](nsmutableparagraphstyle/paragraphspacingbefore.md) method of [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md).

## Parameters

- `glyphIndex`: The index of the glyph in question.
- `rect`: The line fragment rectangle of the first line in the paragraph.

## See Also

- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/linespacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/paragraphspacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the paragraph spacing that is in effect after the specified glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/paragraphspacing(beforeglyphat:withproposedlinefragmentrect:))*