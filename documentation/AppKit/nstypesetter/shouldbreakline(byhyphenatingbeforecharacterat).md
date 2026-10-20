# shouldBreakLine(byHyphenatingBeforeCharacterAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the line being laid out should be broken by hyphenating at the specified character.

**Availability**:
- macOS

## Declaration

```swift
func shouldBreakLine(byHyphenatingBeforeCharacterAt charIndex: Int) -> Bool
```

```objc
- (BOOL) shouldBreakLineByHyphenatingBeforeCharacterAtIndex:(NSUInteger) charIndex;
```

#### Return Value

[`true`](../../Swift/true.md) if the line should be broken by hyphenating, [`false`](../../Swift/false.md) otherwise.

#### Discussion

The typesetter calls this method, if implemented by a subclass, before breaking a line by hyphenating before the character at `charIndex`, enabling the subclass to control line breaking.

A subclass can override this method to customize the text layout process. If the method returns [`false`](../../Swift/false.md), the typesetter continues looking for a break point.

## Parameters

- `charIndex`: The index of the character just after the proposed hyphenation would occur.

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
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](./hyphencharacter%28forglyphat%29.md)
  Returns the hyphen character to be inserted after the specified glyph.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](./hyphenationfactor%28forglyphat%29.md)
  Returns the hyphenation factor in effect at a specified location.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28bywordbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func willSetLineFragmentRect(NSRectPointer, forGlyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)](./willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./sethardinvalidation%28_,forglyphrange%29.md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:))*