# shouldBreakLine(byHyphenatingBeforeCharacterAt:)

**Framework**: AppKit  
**Kind**: method

Breaks a line by hyphenating before the character at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
func shouldBreakLine(byHyphenatingBeforeCharacterAt charIndex: Int) -> Bool
```

#### Discussion

The typesetter calls this method, if implemented by a subclass, before breaking a line by hyphenating before the character at the given character index, enabling the subclass to control line breaking. A subclass can override this method to customize the text layout process. If the method returns [`false`](https://developer.apple.com/documentation/Swift/false), the typesetter continues looking for a break point.

## See Also

- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nsatstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for a control glyph, at the specified glyph position and character index in the text container.
- [func getLineFragmentRect(UnsafeMutablePointer<NSRect>, usedRect: UnsafeMutablePointer<NSRect>, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](nsatstypesetter/getlinefragmentrect(_:usedrect:forparagraphseparatorglyphrange:atproposedorigin:).md)
  Calculates the line fragment rectangle and the portion of the rectangle that contains marks.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](nsatstypesetter/hyphencharacter(forglyphat:).md)
  Returns the hyphen character to be inserted after the specified glyph when hyphenation is enabled in the layout manager.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](nsatstypesetter/hyphenationfactor(forglyphat:).md)
  Returns the hyphenation factor in effect at the specified glyph index.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](nsatstypesetter/shouldbreakline(bywordbeforecharacterat:).md)
  Breaks a line by word-wrapping before the character at the specified index.
- [func willSetLineFragmentRect(UnsafeMutablePointer<NSRect>, forGlyphRange: NSRange, usedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>)](nsatstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Notifies subclasses that the typesetter is about to set a new line fragment.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](nsatstypesetter/sethardinvalidation(_:forglyphrange:).md)
  Sets a Boolean value that determines whether the layout manager invalidates the specified portion of the glyph cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:))*