# CTFontGetGlyphsForCharacters(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Performs basic character-to-glyph mapping.

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
func CTFontGetGlyphsForCharacters(_ font: CTFont, _ characters: UnsafePointer<UniChar>, _ glyphs: UnsafeMutablePointer<CGGlyph>, _ count: CFIndex) -> Bool
```

#### Return Value

`True` if the font could encode all Unicode characters; otherwise `False`.

#### Discussion

Provides basic Unicode encoding for the given font, returning by reference an array of [`CGGlyph`](https://developer.apple.com/documentation/CoreGraphics/CGGlyph) values corresponding to a given array of Unicode characters for the given font.

If a glyph could not be encoded, a value of `0` is passed back at the corresponding index in the `glyphs` array and the function returns `False`. It is the responsibility of the caller to handle the Unicode properties of the input characters.

## Parameters

- `font`: The font reference.
- `characters`: An array of Unicode characters.
- `glyphs`: On output, points to an array of glyph values.
- `count`: The capacity of the character and glyph arrays.

## See Also

- [func CTFontDrawGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, Int, CGContext)](ctfontdrawglyphs(_:_:_:_:_:).md)
  Renders the given glyphs of a font at the specified positions in the supplied graphics context.
- [func CTFontGetLigatureCaretPositions(CTFont, CGGlyph, UnsafeMutablePointer<CGFloat>?, CFIndex) -> CFIndex](ctfontgetligaturecaretpositions(_:_:_:_:).md)
  Returns caret positions within a glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetglyphsforcharacters(_:_:_:_:))*