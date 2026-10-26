# getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Extracts the information needed to lay out the glyphs in the given glyph buffer from the given glyph range.

**Availability**:
- macOS 10.3+ - Deprecated in 10.13

## Declaration

```swift
func getGlyphs(in glyphsRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<NSGlyph>!, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>!, glyphInscriptions inscribeBuffer: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits elasticBuffer: UnsafeMutablePointer<ObjCBool>!) -> Int
```

```objc
- (NSUInteger) getGlyphsInRange:(NSRange) glyphsRange glyphs:(NSGlyph *) glyphBuffer characterIndexes:(NSUInteger *) charIndexBuffer glyphInscriptions:(NSGlyphInscription *) inscribeBuffer elasticBits:(BOOL *) elasticBuffer;
```

#### Discussion

The `charIndexBuffer` contains the original characters for the glyphs. Note that a glyph at index 1 is not necessarily mapped to the character at index 1, since a glyph may be for a ligature or accent.

The `inscribeBuffer` contains the inscription attributes for each glyph, which are used to layout characters that are combined together. The possible values are described in the `Constants` section of the NSLayoutManager reference.

The `elasticBuffer` contains a Boolean value indicating whether a glyph is elastic for each glyph. An elastic glyph can be made longer at the end of a line or when needed for justification.

A subclass can override this method to interact with custom glyph storage.

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
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28byhyphenatingbeforecharacterat%29.md)
  Breaks a line by hyphenating before the character at the specified index.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./shouldbreakline%28bywordbeforecharacterat%29.md)
  Breaks a line by word-wrapping before the character at the specified index.
- [func willSetLineFragmentRect(UnsafeMutablePointer<NSRect>, forGlyphRange: NSRange, usedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>)](./willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Notifies subclasses that the typesetter is about to set a new line fragment.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./sethardinvalidation%28_,forglyphrange%29.md)
  Sets a Boolean value that determines whether the layout manager invalidates the specified portion of the glyph cache.
- [- lineFragmentRectForProposedRect:remainingRect:](./linefragmentrectforproposedrect_remainingrect_.md)
  This method has been deprecated. Use the NSTypesetter method [`getLineFragmentRect:usedRect:remainingRect:forStartingGlyphAtIndex:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:`](../nstypesetter/getlinefragmentrect%28_,usedrect,remaining,forstartingglyphat,proposedrect,linespacing,paragraphspacingbefore,paragraphspacingafter%29.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:))*