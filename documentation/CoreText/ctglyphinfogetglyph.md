# CTGlyphInfoGetGlyph(_:)

**Framework**: Core Text  
**Kind**: func

Retrieves the glyph for a glyph info, if that object exists.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CTGlyphInfoGetGlyph(_ glyphInfo: CTGlyphInfo) -> CGGlyph
```

#### Return Value

A [`CGGlyph`](https://developer.apple.com/documentation/CoreGraphics/CGGlyph) value, if the glyph info object was created with a font; otherwise, `0`.

## Parameters

- `glyphInfo`: The glyph info object from which to get the glyph.

## See Also

- [func CTGlyphInfoGetGlyphName(CTGlyphInfo) -> CFString?](ctglyphinfogetglyphname(_:).md)
  Retrieves the glyph name for a glyph info object, if that object exists.
- [func CTGlyphInfoGetCharacterIdentifier(CTGlyphInfo) -> CGFontIndex](ctglyphinfogetcharacteridentifier(_:).md)
  Gets the character identifier for a glyph info object.
- [func CTGlyphInfoGetCharacterCollection(CTGlyphInfo) -> CTCharacterCollection](ctglyphinfogetcharactercollection(_:).md)
  Gets the character collection for a glyph info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctglyphinfogetglyph(_:))*