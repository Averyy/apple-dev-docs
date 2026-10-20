# advancement(forCGGlyph:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func advancement(forCGGlyph glyph: CGGlyph) -> NSSize
```

```objc
- (NSSize) advancementForCGGlyph:(CGGlyph) glyph;
```

#### Return Value

The advancement spacing in points.

#### Discussion

The spacing is given according to the glyph’s movement direction, which is either strictly horizontal or strictly vertical.

## Parameters

- `glyph`: The glyph whose advancement is returned.

## See Also

### Getting Glyph Advancements
- [var maximumAdvancement: NSSize](./maximumadvancement.md)
  The maximum advance of any of the font’s glyphs.
- [func getAdvancements(NSSizeArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](./getadvancements%28_,forcgglyphs,count%29.md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/advancement(forcgglyph:))*