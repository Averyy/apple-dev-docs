# CTGlyphInfoGetCharacterIdentifier(_:)

**Framework**: Core Text  
**Kind**: func

Gets the character identifier for a glyph info object.

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
func CTGlyphInfoGetCharacterIdentifier(_ glyphInfo: CTGlyphInfo) -> CGFontIndex
```

#### Return Value

The character identifier of the given glyph info object.

## Parameters

- `glyphInfo`: The glyph info from which to get the character identifier. May not be  .

## See Also

- [func CTGlyphInfoGetGlyphName(CTGlyphInfo) -> CFString?](ctglyphinfogetglyphname(_:).md)
  Retrieves the glyph name for a glyph info object, if that object exists.
- [func CTGlyphInfoGetCharacterCollection(CTGlyphInfo) -> CTCharacterCollection](ctglyphinfogetcharactercollection(_:).md)
  Gets the character collection for a glyph info object.
- [func CTGlyphInfoGetGlyph(CTGlyphInfo) -> CGGlyph](ctglyphinfogetglyph(_:).md)
  Retrieves the glyph for a glyph info, if that object exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctglyphinfogetcharacteridentifier(_:))*