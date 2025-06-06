# willSetLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)

**Framework**: AppKit  
**Kind**: method

Notifies subclasses that the typesetter is about to set a new line fragment.

**Availability**:
- macOS ?+

## Declaration

```swift
func willSetLineFragmentRect(_ lineRect: UnsafeMutablePointer<NSRect>, forGlyphRange glyphRange: NSRange, usedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>)
```

#### Discussion

The typesetter calls this method before calling [`setLineFragmentRect(_:forGlyphRange:usedRect:)`](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md), which stores the actual line fragment rectangle location in the layout manager.

The `lineRect` argument is the rectangle in which the glyphs in `glyphRange` are laid out. The `usedRect` argument indicates the portion of `lineRect`, in the [`NSTextContainer`](nstextcontainer.md) object’s coordinate system, that actually contains glyphs or other marks that are drawn (including the text container’s line fragment padding). The `usedRect` must be equal to or contained within `lineRect`. The `baselineOffset` argument is the vertical distance in pixels from the line fragment origin to the baseline on which the glyphs align.

A subclass can override this method to customize the text layout process. For example, it could change the shape of the line fragment rectangle. The subclass is responsible for ensuring that the modified rectangle remains valid (for example, that it lies within the text container).

## See Also

- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nsatstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for a control glyph, at the specified glyph position and character index in the text container.
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
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](nsatstypesetter/sethardinvalidation(_:forglyphrange:).md)
  Sets a Boolean value that determines whether the layout manager invalidates the specified portion of the glyph cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:))*