# layoutGlyphs(in:startingAtGlyphIndex:maxNumberOfLineFragments:nextGlyphIndex:)

**Framework**: AppKit  
**Kind**: method

Lays out glyphs in the specified layout manager starting at a specified glyph.

**Availability**:
- macOS ?+

## Declaration

```swift
func layoutGlyphs(in layoutManager: NSLayoutManager, startingAtGlyphIndex startGlyphIndex: Int, maxNumberOfLineFragments maxNumLines: Int, nextGlyphIndex nextGlyph: UnsafeMutablePointer<Int>)
```

## Parameters

- `layoutManager`: The layout manager in which to lay out glyphs.
- `startGlyphIndex`: The index of the starting glyph.
- `maxNumLines`: The maximum number of lines to generate. Fewer lines may be laid out if the glyph storage runs out of glyphs.
- `nextGlyph`: On return, set to the index of the next glyph that needs to be laid out.

## See Also

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
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](nstypesetter/sethardinvalidation(_:forglyphrange:).md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/layoutglyphs(in:startingatglyphindex:maxnumberoflinefragments:nextglyphindex:))*