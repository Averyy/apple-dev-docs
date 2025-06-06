# insertGlyphs(_:length:forStartingGlyphAt:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Inserts the given glyphs into the glyph cache and maps them to the specified characters.

**Availability**:
- macOS ?+

## Declaration

```swift
func insertGlyphs(_ glyphs: UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt glyphIndex: Int, characterIndex charIndex: Int)
```

#### Discussion

This is a bulk insert method for the glyph cache.

## Parameters

- `glyphs`: The glyphs to insert.
- `length`: Number of glyphs to insert.
- `glyphIndex`: Location in the glyph cache to begin inserting glyphs.
- `charIndex`: Index of first character to be mapped.

## See Also

- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](nsglyphstorage/setintattribute(_:value:forglyphat:).md)
  Sets a custom attribute value for a given glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphstorage/insertglyphs(_:length:forstartingglyphat:characterindex:))*