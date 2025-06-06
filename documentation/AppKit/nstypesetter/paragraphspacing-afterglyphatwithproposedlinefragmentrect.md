# paragraphSpacing(afterGlyphAt:withProposedLineFragmentRect:)

**Framework**: AppKit  
**Kind**: method

Returns the paragraph spacing that is in effect after the specified glyph.

**Availability**:
- macOS ?+

## Declaration

```swift
func paragraphSpacing(afterGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: NSRect) -> CGFloat
```

#### Return Value

The paragraph spacing—that is, the number of points of space added following a paragraph—that is in effect after the glyph specified by `glyphIndex`.

#### Discussion

The typesetter adds the number of points specified in the return value to the bottom of the line fragment rectangle specified by `rect` (but not to the used line fragment rectangle for that line). Paragraph spacing added after a paragraph correlates to the value returned by the [`paragraphSpacing`](nsparagraphstyle/paragraphspacing.md) method of [`NSParagraphStyle`](nsparagraphstyle.md), which you can set using the [`paragraphSpacing`](nsparagraphstyle/paragraphspacing.md) method of [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md).

## Parameters

- `glyphIndex`: The index of the glyph in question.
- `rect`: The line fragment rectangle of the last line in the paragraph.

## See Also

- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/linespacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(beforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/paragraphspacing(beforeglyphat:withproposedlinefragmentrect:).md)
  Returns the number of points of space—added before a paragraph—that is in effect before the specified glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/paragraphspacing(afterglyphat:withproposedlinefragmentrect:))*