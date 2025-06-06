# maximumAdvancement

**Framework**: AppKit  
**Kind**: property

The maximum advance of any of the font’s glyphs.

**Availability**:
- macOS ?+

## Declaration

```swift
var maximumAdvancement: NSSize { get }
```

#### Discussion

The advancement is always either strictly horizontal or strictly vertical.

## See Also

- [func advancement(forGlyph: NSGlyph) -> NSSize](nsfont/advancement(forglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func advancement(forCGGlyph: CGGlyph) -> NSSize](nsfont/advancement(forcgglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func getAdvancements(NSSizeArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](nsfont/getadvancements(_:forcgglyphs:count:).md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/maximumadvancement)*