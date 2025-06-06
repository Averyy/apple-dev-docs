# boundingBox(forControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)

**Framework**: AppKit  
**Kind**: method

Returns the bounding rectangle for a control glyph, at the specified glyph position and character index in the text container.

**Availability**:
- macOS ?+

## Declaration

```swift
func boundingBox(forControlGlyphAt glyphIndex: Int, for textContainer: NSTextContainer, proposedLineFragment proposedRect: NSRect, glyphPosition: NSPoint, characterIndex charIndex: Int) -> NSRect
```

#### Discussion

Returns the bounding rectangle for the control glyph at `glyphIndex`, at the given `glyphPosition` and character index `charIndex`, in `textContainer`. The proposed line fragment rectangle is specified by `proposedRect`.

The typesetter calls this method when it encounters an [`NSControlGlyph`](nscontrolglyph.md). The default behavior is to return zero width for control glyphs. A subclass can override this method to do something different, such as implement a way to display control characters.

[`NSGlyphGenerator`](nsglyphgenerator.md) can choose whether or not to map control characters to [`NSControlGlyph`](nscontrolglyph.md). Tab characters, for example, do not use this facility.

## See Also

- [func getLineFragmentRect(UnsafeMutablePointer<NSRect>, usedRect: UnsafeMutablePointer<NSRect>, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](nsatstypesetter/getlinefragmentrect(_:usedrect:forparagraphseparatorglyphrange:atproposedorigin:).md)
  Calculates the line fragment rectangle and the portion of the rectangle that contains marks.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](nsatstypesetter/hyphencharacter(forglyphat:).md)
  Returns the hyphen character to be inserted after the specified glyph when hyphenation is enabled in the layout manager.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](nsatstypesetter/hyphenationfactor(forglyphat:).md)
  Returns the hyphenation factor in effect at the specified glyph index.
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](nsatstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:).md)
  Breaks a line by hyphenating before the character at the specified index.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](nsatstypesetter/shouldbreakline(bywordbeforecharacterat:).md)
  Breaks a line by word-wrapping before the character at the specified index.
- [func willSetLineFragmentRect(UnsafeMutablePointer<NSRect>, forGlyphRange: NSRange, usedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>)](nsatstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Notifies subclasses that the typesetter is about to set a new line fragment.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](nsatstypesetter/sethardinvalidation(_:forglyphrange:).md)
  Sets a Boolean value that determines whether the layout manager invalidates the specified portion of the glyph cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:))*