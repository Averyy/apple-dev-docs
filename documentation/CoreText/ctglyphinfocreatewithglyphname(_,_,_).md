# CTGlyphInfoCreateWithGlyphName(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable glyph info object with a glyph name.

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
func CTGlyphInfoCreateWithGlyphName(_ glyphName: CFString, _ font: CTFont, _ baseString: CFString) -> CTGlyphInfo?
```

```c
extern CTGlyphInfoRefCTGlyphInfoCreateWithGlyphName(CFStringRef glyphName, CTFontRef font, CFStringRef baseString);
```

#### Return Value

A valid reference to an immutable CTGlyphInfo object if glyph info creation was successful; otherwise, `NULL`.

#### Discussion

This function creates an immutable glyph info object for a glyph name such as `copyright` using a specified font.

## Parameters

- `glyphName`: The name of the glyph.
- `font`: The font to be associated with the returned CTGlyphInfo object.
- `baseString`: The part of the string the returned object is intended to override.

## See Also

### Creating GlyphInfo Objects
- [func CTGlyphInfoCreateWithGlyph(CGGlyph, CTFont, CFString) -> CTGlyphInfo?](./ctglyphinfocreatewithglyph%28_,_,_%29.md)
  Creates an immutable glyph info object with a glyph index.
- [func CTGlyphInfoCreateWithCharacterIdentifier(CGFontIndex, CTCharacterCollection, CFString) -> CTGlyphInfo?](./ctglyphinfocreatewithcharacteridentifier%28_,_,_%29.md)
  Creates an immutable glyph info object with a character identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctglyphinfocreatewithglyphname(_:_:_:))*