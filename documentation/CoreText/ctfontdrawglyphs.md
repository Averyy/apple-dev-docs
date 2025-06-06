# CTFontDrawGlyphs(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Renders the given glyphs of a font at the specified positions in the supplied graphics context.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontDrawGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int, _ context: CGContext)
```

#### Discussion

This function modifies graphics state including font, text size, and text matrix if these attributes are specified in `font`. These attributes are not restored.

## Parameters

- `font`: The font with glyphs to render. If the font has a size or matrix attribute,   is set with these values.
- `glyphs`: The glyphs to be rendered. The glyphs should be the result of proper Unicode text layout operations (such as with  ). Functions such as   do not perform any Unicode text layout.
- `positions`: The positions (origins) for each glyph in  . The positions are in user space. The number of positions passed in must match the number of glyphs (in  ).
- `count`: The number of glyphs to be rendered from the   array.
- `context`: The graphics context used to render the glyphs.

## See Also

- [func CTFontGetGlyphsForCharacters(CTFont, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool](ctfontgetglyphsforcharacters(_:_:_:_:).md)
  Performs basic character-to-glyph mapping.
- [func CTFontGetLigatureCaretPositions(CTFont, CGGlyph, UnsafeMutablePointer<CGFloat>?, CFIndex) -> CFIndex](ctfontgetligaturecaretpositions(_:_:_:_:).md)
  Returns caret positions within a glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdrawglyphs(_:_:_:_:_:))*