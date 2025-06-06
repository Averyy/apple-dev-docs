# screenFont(with:)

**Framework**: AppKit  
**Kind**: method

Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.

**Availability**:
- macOS ?+

## Declaration

```swift
func screenFont(with renderingMode: NSFontRenderingMode) -> NSFont
```

#### Discussion

For valid rendering modes, see [`NSFontRenderingMode`](nsfontrenderingmode.md).

Screen fonts are for direct use with the window server only. Never use them with Application Kit objects, such as in `setFont:` methods. Internally, the Application Kit automatically uses the corresponding screen font for a font object as long as the view is not rotated or scaled.

## See Also

- [var screen: NSFont](nsfont/screen.md)
  The bitmapped screen font for the current font.
- [var printer: NSFont](nsfont/printer.md)
  The scalable PostScript font corresponding to current font.
- [func advancement(forGlyph: NSGlyph) -> NSSize](nsfont/advancement(forglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](nsfont/boundingrect(forglyph:).md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getAdvancements(NSSizeArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](nsfont/getadvancements(_:forglyphs:count:).md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](nsfont/getadvancements(_:forpackedglyphs:length:).md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](nsfont/getboundingrects(_:forglyphs:count:).md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func glyph(withName: String) -> NSGlyph](nsfont/glyph(withname:).md)
  Returns the named encoded glyph, or –1 if the receiver contains no such glyph.
- [func withSize(CGFloat) -> NSFont](nsfont/withsize(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/screenfont(with:))*