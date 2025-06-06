# hyphenationFactor(forGlyphAt:)

**Framework**: AppKit  
**Kind**: method

Returns the hyphenation factor in effect at a specified location.

**Availability**:
- macOS ?+

## Declaration

```swift
func hyphenationFactor(forGlyphAt glyphIndex: Int) -> Float
```

#### Return Value

The hyphenation factor in effect at `glyphIndex`. The hyphenation factor is a value ranging from 0.0 to 1.0 that controls when hyphenation is attempted. By default, the value is 0.0, meaning hyphenation is off. A factor of 1.0 causes hyphenation to be attempted always.

#### Discussion

The typesetter calls this method with a proposed hyphenation point for a line break to find the hyphenation factor in effect at that time. A subclass can override this method to customize the text layout process.

## Parameters

- `glyphIndex`: The index of the glyph position to examine.

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
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](nstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:).md)
  Returns whether the line being laid out should be broken by hyphenating at the specified character.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](nstypesetter/shouldbreakline(bywordbeforecharacterat:).md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func willSetLineFragmentRect(NSRectPointer, forGlyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)](nstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](nstypesetter/sethardinvalidation(_:forglyphrange:).md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/hyphenationfactor(forglyphat:))*