# lineSpacing(afterGlyphAt:withProposedLineFragmentRect:)

**Framework**: AppKit  
**Kind**: method

Returns the line spacing in effect following the specified glyph.

**Availability**:
- macOS ?+

## Declaration

```swift
func lineSpacing(afterGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: NSRect) -> CGFloat
```

#### Return Value

The line spacing in effect following the glyph at `glyphIndex`.

#### Discussion

The [`NSATSTypesetter`](nsatstypesetter.md) calls this method to determine the number of points of space to include below the descenders in the used rectangle for the proposed line fragment rectangle `rect`.

Line spacing, also called leading, is an attribute of [`NSParagraphStyle`](nsparagraphstyle.md), which you can set on an [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md) object. A font typically includes a default minimum line spacing metric used if none is set in the paragraph style.

If the typesetter behavior specified in the layout manager is `NSTypesetterOriginalBehavior`, the text system uses the original, private typesetter `NSSimpleHorizontalTypesetter`, which adds the line spacing above the ascender. Similarly, [`NSATSTypesetter`](nsatstypesetter.md) adds the line spacing above the ascender if the value is negative.

## Parameters

- `glyphIndex`: The index of the glyph in question.
- `rect`: The proposed line fragment rectangle.

## See Also

- [func paragraphSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/paragraphspacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the paragraph spacing that is in effect after the specified glyph.
- [func paragraphSpacing(beforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/paragraphspacing(beforeglyphat:withproposedlinefragmentrect:).md)
  Returns the number of points of space—added before a paragraph—that is in effect before the specified glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/linespacing(afterglyphat:withproposedlinefragmentrect:))*