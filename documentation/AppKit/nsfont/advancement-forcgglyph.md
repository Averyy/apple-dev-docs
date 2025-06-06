# advancement(forCGGlyph:)

**Framework**: AppKit  
**Kind**: method

Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func advancement(forCGGlyph glyph: CGGlyph) -> NSSize
```

#### Return Value

The advancement spacing in points.

#### Discussion

The spacing is given according to the glyph’s movement direction, which is either strictly horizontal or strictly vertical.

## Parameters

- `glyph`: The glyph whose advancement is returned.

## See Also

- [var maximumAdvancement: NSSize](nsfont/maximumadvancement.md)
  The maximum advance of any of the font’s glyphs.
- [func getAdvancements(NSSizeArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](nsfont/getadvancements(_:forcgglyphs:count:).md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/advancement(forcgglyph:))*