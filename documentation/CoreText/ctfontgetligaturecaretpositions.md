# CTFontGetLigatureCaretPositions(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns caret positions within a glyph.

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
func CTFontGetLigatureCaretPositions(_ font: CTFont, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>?, _ maxPositions: CFIndex) -> CFIndex
```

#### Return Value

The maximum number of caret positions for the specified glyph

#### Discussion

This function is used to obtain caret positions for a specific glyph. The return value is the maximum number of positions possible, and the function will populate the caller’s `positions` buffer with available positions if possible. This function might not be able to produce positions if the font does not have the appropriate data, in which case it will return 0.

## Parameters

- `font`: A reference to the font to use.
- `glyph`: A reference to the glyph.
- `positions`: A buffer of at least   to receive the ligature caret positions for  .
- `maxPositions`: The maximum number of positions to return.

## See Also

- [func CTFontGetGlyphsForCharacters(CTFont, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool](ctfontgetglyphsforcharacters(_:_:_:_:).md)
  Performs basic character-to-glyph mapping.
- [func CTFontDrawGlyphs(CTFont, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, Int, CGContext)](ctfontdrawglyphs(_:_:_:_:_:).md)
  Renders the given glyphs of a font at the specified positions in the supplied graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetligaturecaretpositions(_:_:_:_:))*