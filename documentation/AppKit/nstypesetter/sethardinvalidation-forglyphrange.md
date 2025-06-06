# setHardInvalidation(_:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.

**Availability**:
- macOS ?+

## Declaration

```swift
func setHardInvalidation(_ flag: Bool, forGlyphRange glyphRange: NSRange)
```

## Parameters

- `flag`:   if the layout manager should invalidate the specified portion of the glyph cache,   otherwise.
- `glyphRange`: The range of glyphs in the cache to be marked for hard invalidation.

## See Also

- [func layoutGlyphs(in: NSLayoutManager, startingAtGlyphIndex: Int, maxNumberOfLineFragments: Int, nextGlyphIndex: UnsafeMutablePointer<Int>)](nstypesetter/layoutglyphs(in:startingatglyphindex:maxnumberoflinefragments:nextglyphindex:).md)
  Lays out glyphs in the specified layout manager starting at a specified glyph.
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func getLineFragmentRect(NSRectPointer, usedRect: NSRectPointer, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](nstypesetter/getlinefragmentrect(_:usedrect:forparagraphseparatorglyphrange:atproposedorigin:).md)
  Calculates the line fragment rectangle and line fragment used rectangle for blank lines.
- [func getLineFragmentRect(NSRectPointer!, usedRect: NSRectPointer!, remaining: NSRectPointer!, forStartingGlyphAt: Int, proposedRect: NSRect, lineSpacing: CGFloat, paragraphSpacingBefore: CGFloat, paragraphSpacingAfter: CGFloat)](nstypesetter/getlinefragmentrect(_:usedrect:remaining:forstartingglyphat:proposedrect:linespacing:paragraphspacingbefore:paragraphspacingafter:).md)
  Calculates line fragment rectangle, line fragment used rectangle, and remaining rectangle for a line fragment.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](nstypesetter/hyphencharacter(forglyphat:).md)
  Returns the hyphen character to be inserted after the specified glyph.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](nstypesetter/hyphenationfactor(forglyphat:).md)
  Returns the hyphenation factor in effect at a specified location.
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](nstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:).md)
  Returns whether the line being laid out should be broken by hyphenating at the specified character.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](nstypesetter/shouldbreakline(bywordbeforecharacterat:).md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func willSetLineFragmentRect(NSRectPointer, forGlyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)](nstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/sethardinvalidation(_:forglyphrange:))*