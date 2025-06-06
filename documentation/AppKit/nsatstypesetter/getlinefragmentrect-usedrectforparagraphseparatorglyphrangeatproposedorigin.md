# getLineFragmentRect(_:usedRect:forParagraphSeparatorGlyphRange:atProposedOrigin:)

**Framework**: AppKit  
**Kind**: method

Calculates the line fragment rectangle and the portion of the rectangle that contains marks.

**Availability**:
- macOS ?+

## Declaration

```swift
func getLineFragmentRect(_ lineFragmentRect: UnsafeMutablePointer<NSRect>, usedRect lineFragmentUsedRect: UnsafeMutablePointer<NSRect>, forParagraphSeparatorGlyphRange paragraphSeparatorGlyphRange: NSRange, atProposedOrigin lineOrigin: NSPoint)
```

#### Discussion

The method returns the calculated line fragment rectangle in `lineFragmentRect`, and it returns the used rectangle (the portion of the line fragment rectangle that actually contains marks) in `lineFragmentUsedRect`. The `paragraphSeparatorGlyphRange` is the range of glyphs under consideration, and `lineOrigin` is the origin point of the line fragment rectangle. A `paragraphSeparatorGlyphRange` with length 0 indicates an extra line fragment (which occurs if the last character in the paragraph is a line separator.)

## See Also

- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nsatstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for a control glyph, at the specified glyph position and character index in the text container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/getlinefragmentrect(_:usedrect:forparagraphseparatorglyphrange:atproposedorigin:))*