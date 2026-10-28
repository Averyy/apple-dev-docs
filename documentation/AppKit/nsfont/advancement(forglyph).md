# advancement(forGlyph:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.

**Availability**:
- macOS

> **Deprecated**: Use [`advancement(forCGGlyph:)`](./advancement%28forcgglyph%29.md) instead.

## Declaration

```swift
func advancement(forGlyph glyph: NSGlyph) -> NSSize
```

```objc
- (NSSize) advancementForGlyph:(NSGlyph) glyph;
```

## Return Value

The advancement spacing in points.

## Discussion

This spacing is given according to the glyph’s movement direction, which is either strictly horizontal or strictly vertical.

## Parameters

- `glyph`: The glyph whose advancement is returned.

## See Also

### Related Documentation
- [var maximumAdvancement: NSSize](./maximumadvancement.md)
  The maximum advance of any of the font’s glyphs.
### Instance Methods
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](./boundingrect%28forglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getAdvancements(NSSizeArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./getadvancements%28_,forglyphs,count%29.md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](./getadvancements%28_,forpackedglyphs,length%29.md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./getboundingrects%28_,forglyphs,count%29.md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func glyph(withName: String) -> NSGlyph](./glyph%28withname%29.md)
  Returns the named encoded glyph, or –1 if the receiver contains no such glyph.
- [func screenFont(with: NSFontRenderingMode) -> NSFont](./screenfont%28with%29.md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [func withSize(CGFloat) -> NSFont](./withsize%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/advancement(forglyph:))*