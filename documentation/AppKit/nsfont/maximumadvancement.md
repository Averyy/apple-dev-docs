# maximumAdvancement

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum advance of any of the font’s glyphs.

**Availability**:
- macOS

## Declaration

```swift
var maximumAdvancement: NSSize { get }
```

```objc
@property (readonly) NSSize maximumAdvancement;
```

#### Discussion

The advancement is always either strictly horizontal or strictly vertical.

## See Also

### Related Documentation
- [func advancement(forGlyph: NSGlyph) -> NSSize](./advancement%28forglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
### Getting Glyph Advancements
- [func advancement(forCGGlyph: CGGlyph) -> NSSize](./advancement%28forcgglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [func getAdvancements(NSSizeArray, forCGGlyphs: UnsafePointer<CGGlyph>, count: Int)](./getadvancements%28_,forcgglyphs,count%29.md)
  Returns an array of the advancements for the specified glyphs rendered by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/maximumadvancement)*