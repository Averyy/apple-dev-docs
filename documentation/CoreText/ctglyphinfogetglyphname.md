# CTGlyphInfoGetGlyphName(_:)

**Framework**: Core Text  
**Kind**: func

Retrieves the glyph name for a glyph info object, if that object exists.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTGlyphInfoGetGlyphName(_ glyphInfo: CTGlyphInfo) -> CFString?
```

#### Return Value

A glyph name, if the glyph info object was created with a name; otherwise, `NULL`.

## Parameters

- `glyphInfo`: The glyph info object from which to get the glyph name. This parameter must not be  .

## See Also

- [func CTGlyphInfoGetCharacterIdentifier(CTGlyphInfo) -> CGFontIndex](ctglyphinfogetcharacteridentifier(_:).md)
  Gets the character identifier for a glyph info object.
- [func CTGlyphInfoGetCharacterCollection(CTGlyphInfo) -> CTCharacterCollection](ctglyphinfogetcharactercollection(_:).md)
  Gets the character collection for a glyph info object.
- [func CTGlyphInfoGetGlyph(CTGlyphInfo) -> CGGlyph](ctglyphinfogetglyph(_:).md)
  Retrieves the glyph for a glyph info, if that object exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctglyphinfogetglyphname(_:))*