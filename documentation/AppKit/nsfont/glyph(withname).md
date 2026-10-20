# glyph(withName:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the named encoded glyph, or –1 if the receiver contains no such glyph.

**Availability**:
- macOS

## Declaration

```swift
func glyph(withName name: String) -> NSGlyph
```

```objc
- (NSGlyph) glyphWithName:(NSString *) name;
```

#### Return Value

The named encoded glyph.

#### Discussion

Returns –1 if the glyph named `glyphName` isn’t encoded.

Glyph names in fonts do not always accurately identify the glyph. The layout manager, an instance of [`NSLayoutManager`](../nslayoutmanager.md), finds the correspondence between characters and glyphs. See [`NSLayoutManager`](../nslayoutmanager.md) for more information.

## Parameters

- `name`: The name of the glyph.

## See Also

### Instance Methods
- [func advancement(forGlyph: NSGlyph) -> NSSize](./advancement%28forglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func boundingRect(forGlyph: NSGlyph) -> NSRect](./boundingrect%28forglyph%29.md)
  Returns the bounding rectangle for the specified glyph, scaled to the receiver’s size.
- [func getAdvancements(NSSizeArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./getadvancements%28_,forglyphs,count%29.md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.
- [func getAdvancements(NSSizeArray, forPackedGlyphs: UnsafeRawPointer, length: Int)](./getadvancements%28_,forpackedglyphs,length%29.md)
  Returns an array of the advancements for the specified packed glyphs and rendered by the receiver.
- [func getBoundingRects(NSRectArray, forGlyphs: UnsafePointer<NSGlyph>, count: Int)](./getboundingrects%28_,forglyphs,count%29.md)
  Returns an array of the bounding rectangles for the specified glyphs rendered by the receiver.
- [func screenFont(with: NSFontRenderingMode) -> NSFont](./screenfont%28with%29.md)
  Returns a bitmapped screen font, when sent to a font object representing a scalable PostScript font, with the specified rendering mode, matching the receiver in typeface and matrix (or size), or `nil` if such a font can’t be found.
- [func withSize(CGFloat) -> NSFont](./withsize%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/glyph(withname:))*