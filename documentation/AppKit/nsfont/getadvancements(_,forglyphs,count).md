# getAdvancements(_:forGlyphs:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of the advancements for the specified glyphs rendered by the receiver.

**Availability**:
- macOS

> **Deprecated**: Use [`getAdvancements(_:forCGGlyphs:count:)`](./getadvancements%28_,forcgglyphs,count%29.md) instead.

## Declaration

```swift
func getAdvancements(_ advancements: NSSizeArray, forGlyphs glyphs: UnsafePointer<NSGlyph>, count glyphCount: Int)
```

```objc
- (void) getAdvancements:(NSSizeArray) advancements forGlyphs:(const NSGlyph *) glyphs count:(NSUInteger) glyphCount;
```

## Discussion

Returns in `advancements` an array of the advancements for the glyphs specified by `glyphs` and rendered by the receiver. The  `glyphCount` must specify the count of glyphs passed in `glyphs`.

## See Also

### Related Documentation
- [var boundingRectForFont: NSRect](./boundingrectforfont.md)
  The font’s bounding rectangle, scaled to the font’s size.
### Instance Methods
- [func advancement(forGlyph: NSGlyph) -> NSSize](./advancement%28forglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](./boundingrect%28forglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/getadvancements(_:forglyphs:count:))*