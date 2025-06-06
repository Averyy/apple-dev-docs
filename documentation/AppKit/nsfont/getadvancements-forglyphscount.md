# getAdvancements(_:forGlyphs:count:)

**Framework**: AppKit  
**Kind**: method

Returns an array of the advancements for the specified glyphs rendered by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func getAdvancements(_ advancements: NSSizeArray, forGlyphs glyphs: UnsafePointer<NSGlyph>, count glyphCount: Int)
```

#### Discussion

Returns in `advancements` an array of the advancements for the glyphs specified by `glyphs` and rendered by the receiver. The  `glyphCount` must specify the count of glyphs passed in `glyphs`.

## See Also

- [var boundingRectForFont: NSRect](nsfont/boundingrectforfont.md)
  The font’s bounding rectangle, scaled to the font’s size.
- [func advancement(forGlyph: NSGlyph) -> NSSize](nsfont/advancement(forglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](nsfont/boundingrect(forglyph:).md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](nsfont/getadvancements(_:forpackedglyphs:length:).md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](nsfont/getboundingrects(_:forglyphs:count:).md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func glyph(withName: String) -> NSGlyph](nsfont/glyph(withname:).md)
  Returns the named encoded glyph, or –1 if the receiver contains no such glyph.
- [func screenFont(with: NSFontRenderingMode) -> NSFont](nsfont/screenfont(with:).md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [func withSize(CGFloat) -> NSFont](nsfont/withsize(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/getadvancements(_:forglyphs:count:))*