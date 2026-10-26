# shouldBreakLine(byHyphenatingBeforeCharacterAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Breaks a line by hyphenating before the character at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func shouldBreakLine(byHyphenatingBeforeCharacterAt charIndex: Int) -> Bool
```

```objc
- (BOOL) shouldBreakLineByHyphenatingBeforeCharacterAtIndex:(NSUInteger) charIndex;
```

#### Discussion

The typesetter calls this method, if implemented by a subclass, before breaking a line by hyphenating before the character at the given character index, enabling the subclass to control line breaking. A subclass can override this method to customize the text layout process. If the method returns [`false`](../../Swift/false.md), the typesetter continues looking for a break point.

## See Also

### Laying Out Glyphs
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for a control glyph, at the specified glyph position and character index in the text container.
- [func getLineFragmentRect(UnsafeMutablePointer<NSRect>, usedRect: UnsafeMutablePointer<NSRect>, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](./getlinefragmentrect%28_,usedrect,forparagraphseparatorglyphrange,atproposedorigin%29.md)
  Calculates the line fragment rectangle and the portion of the rectangle that contains marks.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](./hyphencharacter%28forglyphat%29.md)
  Returns the hyphen character to be inserted after the specified glyph when hyphenation is enabled in the layout manager.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](./hyphenationfactor%28forglyphat%29.md)
  Returns the hyphenation factor in effect at the specified glyph index.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28bywordbeforecharacterat%29.md)
  Breaks a line by word-wrapping before the character at the specified index.
- [func willSetLineFragmentRect(UnsafeMutablePointer<NSRect>, forGlyphRange: NSRange, usedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>)](./willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Notifies subclasses that the typesetter is about to set a new line fragment.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./sethardinvalidation%28_,forglyphrange%29.md)
  Sets a Boolean value that determines whether the layout manager invalidates the specified portion of the glyph cache.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!) -> Int](./getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits%29.md)
  Extracts the information needed to lay out the glyphs in the given glyph buffer from the given glyph range.
- [- lineFragmentRectForProposedRect:remainingRect:](./linefragmentrectforproposedrect_remainingrect_.md)
  This method has been deprecated. Use the NSTypesetter method [`getLineFragmentRect:usedRect:remainingRect:forStartingGlyphAtIndex:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:`](../nstypesetter/getlinefragmentrect%28_,usedrect,remaining,forstartingglyphat,proposedrect,linespacing,paragraphspacingbefore,paragraphspacingafter%29.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:))*