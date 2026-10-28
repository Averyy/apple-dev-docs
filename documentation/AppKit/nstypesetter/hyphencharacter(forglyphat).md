# hyphenCharacter(forGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the hyphen character to be inserted after the specified glyph.

**Availability**:
- macOS

## Declaration

```swift
func hyphenCharacter(forGlyphAt glyphIndex: Int) -> UTF32Char
```

```objc
- (UTF32Char) hyphenCharacterForGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Return Value

The hyphen character to be inserted after the glyph at `glyphIndex`.

## Discussion

The typesetter calls this method before hyphenating. A subclass can override this method to return a different hyphen glyph.

## Parameters

- `glyphIndex`: The index of the glyph in question.

## See Also

### Laying out glyphs
- [func layoutGlyphs(in: NSLayoutManager, startingAtGlyphIndex: Int, maxNumberOfLineFragments: Int, nextGlyphIndex: UnsafeMutablePointer<Int>)](./layoutglyphs%28in,startingatglyphindex,maxnumberoflinefragments,nextglyphindex%29.md)
  Lays out glyphs in the specified layout manager starting at a specified glyph.
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func getLineFragmentRect(NSRectPointer, usedRect: NSRectPointer, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](./getlinefragmentrect%28_,usedrect,forparagraphseparatorglyphrange,atproposedorigin%29.md)
  Calculates the line fragment rectangle and line fragment used rectangle for blank lines.
- [func getLineFragmentRect(NSRectPointer!, usedRect: NSRectPointer!, remaining: NSRectPointer!, forStartingGlyphAt: Int, proposedRect: NSRect, lineSpacing: CGFloat, paragraphSpacingBefore: CGFloat, paragraphSpacingAfter: CGFloat)](./getlinefragmentrect%28_,usedrect,remaining,forstartingglyphat,proposedrect,linespacing,paragraphspacingbefore,paragraphspacingafter%29.md)
  Calculates line fragment rectangle, line fragment used rectangle, and remaining rectangle for a line fragment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/hyphencharacter(forglyphat:))*