# getLineFragmentRect(_:usedRect:remaining:forStartingGlyphAt:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Calculates line fragment rectangle, line fragment used rectangle, and remaining rectangle for a line fragment.

**Availability**:
- macOS

## Declaration

```swift
func getLineFragmentRect(_ lineFragmentRect: NSRectPointer!, usedRect lineFragmentUsedRect: NSRectPointer!, remaining remainingRect: NSRectPointer!, forStartingGlyphAt startingGlyphIndex: Int, proposedRect: NSRect, lineSpacing: CGFloat, paragraphSpacingBefore: CGFloat, paragraphSpacingAfter: CGFloat)
```

```objc
- (void) getLineFragmentRect:(NSRectPointer) lineFragmentRect usedRect:(NSRectPointer) lineFragmentUsedRect remainingRect:(NSRectPointer) remainingRect forStartingGlyphAtIndex:(NSUInteger) startingGlyphIndex proposedRect:(NSRect) proposedRect lineSpacing:(CGFloat) lineSpacing paragraphSpacingBefore:(CGFloat) paragraphSpacingBefore paragraphSpacingAfter:(CGFloat) paragraphSpacingAfter;
```

## Discussion

The height of the line fragment is determined using `lineSpacing`, `paragraphSpacingBefore`, and `paragraphSpacingAfter` as well as `proposedRect`. The width for `lineFragmentUsedRect` is set to the `lineFragmentRect` width. In the standard implementation, paragraph spacing is included in the line fragment rectangle but not the line fragment used rectangle; line spacing is included in both.

## Parameters

- `lineFragmentRect`: On return, the calculated line fragment rectangle.
- `lineFragmentUsedRect`: On return, the used rectangle (the portion of the line fragment rectangle that actually contains marks).
- `remainingRect`: On return, the remaining rectangle of `proposedRect`.
- `startingGlyphIndex`: The glyph index where the line fragment starts.
- `proposedRect`: The proposed rectangle of the line fragment.
- `lineSpacing`: The line spacing.
- `paragraphSpacingBefore`: The spacing before the paragraph.
- `paragraphSpacingAfter`: The spacing after the paragraph.

## See Also

### Laying out glyphs
- [func layoutGlyphs(in: NSLayoutManager, startingAtGlyphIndex: Int, maxNumberOfLineFragments: Int, nextGlyphIndex: UnsafeMutablePointer<Int>)](./layoutglyphs%28in,startingatglyphindex,maxnumberoflinefragments,nextglyphindex%29.md)
  Lays out glyphs in the specified layout manager starting at a specified glyph.
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func getLineFragmentRect(NSRectPointer, usedRect: NSRectPointer, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](./getlinefragmentrect%28_,usedrect,forparagraphseparatorglyphrange,atproposedorigin%29.md)
  Calculates the line fragment rectangle and line fragment used rectangle for blank lines.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](./hyphencharacter%28forglyphat%29.md)
  Returns the hyphen character to be inserted after the specified glyph.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](./hyphenationfactor%28forglyphat%29.md)
  Returns the hyphenation factor in effect at a specified location.
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28byhyphenatingbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by hyphenating at the specified character.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28bywordbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func willSetLineFragmentRect(NSRectPointer, forGlyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)](./willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./sethardinvalidation%28_,forglyphrange%29.md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/getlinefragmentrect(_:usedrect:remaining:forstartingglyphat:proposedrect:linespacing:paragraphspacingbefore:paragraphspacingafter:))*