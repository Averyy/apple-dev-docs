# willSetLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.

**Availability**:
- macOS

## Declaration

```swift
func willSetLineFragmentRect(_ lineRect: NSRectPointer, forGlyphRange glyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)
```

```objc
- (void) willSetLineFragmentRect:(NSRectPointer) lineRect forGlyphRange:(NSRange) glyphRange usedRect:(NSRectPointer) usedRect baselineOffset:(CGFloat *) baselineOffset;
```

## Discussion

Called by the typesetter just prior to calling [`setLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)`](./setlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md) which stores the actual line fragment rectangle location in the layout manager.

A subclass can override this method to customize the text layout process. For example, it could change the shape of the line fragment rectangle. The subclass is responsible for ensuring that the modified rectangle remains valid (for example, that it lies within the text container).

## Parameters

- `lineRect`: The rectangle in which the glyphs in `glyphRange` are laid out.
- `glyphRange`: The range of the glyphs to lay out.
- `usedRect`: The portion of `lineRect`, in the NSTextContainer object’s coordinate system, that actually contains glyphs or other marks that are drawn (including the text container’s line fragment padding). The `usedRect` must be equal to or contained within `lineRect`.
- `baselineOffset`: The vertical distance in pixels from the line fragment origin to the baseline on which the glyphs align.

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
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28byhyphenatingbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by hyphenating at the specified character.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28bywordbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./sethardinvalidation%28_,forglyphrange%29.md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:))*