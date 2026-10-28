# CTGlyphInfoCreateWithCharacterIdentifier(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable glyph info object with a character identifier.

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
func CTGlyphInfoCreateWithCharacterIdentifier(_ cid: CGFontIndex, _ collection: CTCharacterCollection, _ baseString: CFString) -> CTGlyphInfo?
```

```c
extern CTGlyphInfoRefCTGlyphInfoCreateWithCharacterIdentifier(CGFontIndex cid, CTCharacterCollection collection, CFStringRef baseString);
```

## Return Value

A valid reference to an immutable CTGlyphInfo object if glyph info creation was successful; otherwise, `NULL`.

## Discussion

This function creates an immutable glyph info object for a character identifier and a character collection.

## Parameters

- `cid`: A character identifier.
- `collection`: A character collection identifier.
- `baseString`: The part of the string the returned object is intended to override.

## See Also

### Creating GlyphInfo Objects
- [func CTGlyphInfoCreateWithGlyphName(CFString, CTFont, CFString) -> CTGlyphInfo?](./ctglyphinfocreatewithglyphname%28_,_,_%29.md)
  Creates an immutable glyph info object with a glyph name.
- [func CTGlyphInfoCreateWithGlyph(CGGlyph, CTFont, CFString) -> CTGlyphInfo?](./ctglyphinfocreatewithglyph%28_,_,_%29.md)
  Creates an immutable glyph info object with a glyph index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctglyphinfocreatewithcharacteridentifier(_:_:_:))*