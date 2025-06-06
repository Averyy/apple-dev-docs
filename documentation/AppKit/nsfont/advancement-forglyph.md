# advancement(forGlyph:)

**Framework**: AppKit  
**Kind**: method

Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.

**Availability**:
- macOS ?+

## Declaration

```swift
func advancement(forGlyph glyph: NSGlyph) -> NSSize
```

#### Return Value

The advancement spacing in points.

#### Discussion

This spacing is given according to the glyph’s movement direction, which is either strictly horizontal or strictly vertical.

## Parameters

- `glyph`: The glyph whose advancement is returned.

## See Also

- [var maximumAdvancement: NSSize](nsfont/maximumadvancement.md)
  The maximum advance of any of the font’s glyphs.
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
- [func screenFont(with: NSFontRenderingMode) -> NSFont](nsfont/screenfont(with:).md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [func withSize(CGFloat) -> NSFont](nsfont/withsize(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/advancement(forglyph:))*