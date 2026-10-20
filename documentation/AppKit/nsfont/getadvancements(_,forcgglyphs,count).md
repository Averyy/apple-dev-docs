# getAdvancements(_:forCGGlyphs:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of the advancements for the specified glyphs rendered by the receiver.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func getAdvancements(_ advancements: NSSizeArray, forCGGlyphs glyphs: UnsafePointer<CGGlyph>, count glyphCount: Int)
```

```objc
- (void) getAdvancements:(NSSizeArray) advancements forCGGlyphs:(const CGGlyph *) glyphs count:(NSUInteger) glyphCount;
```

#### Discussion

Returns in `advancements` an array of the advancements for the glyphs specified by `glyphs` and rendered by the receiver. The `glyphCount` value must specify the count of glyphs passed in `glyphs`.

## See Also

### Getting Glyph Advancements
- [var maximumAdvancement: NSSize](./maximumadvancement.md)
  The maximum advance of any of the font’s glyphs.
- [func advancement(forCGGlyph: CGGlyph) -> NSSize](./advancement%28forcgglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/getadvancements(_:forcgglyphs:count:))*