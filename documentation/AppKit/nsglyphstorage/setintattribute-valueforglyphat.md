# setIntAttribute(_:value:forGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Sets a custom attribute value for a given glyph.

**Availability**:
- macOS ?+

## Declaration

```swift
func setIntAttribute(_ attributeTag: Int, value val: Int, forGlyphAt glyphIndex: Int)
```

#### Discussion

Custom attributes are glyph attributes such as `NSGlyphInscription` or attributes defined by subclasses. Subclasses that define their own custom attributes must override this method and provide their own storage for the attribute values. Nonnegative tags are reserved; you can define your own attributes with negative tags and set values using this method.

## Parameters

- `attributeTag`: The custom attribute.
- `val`: The new attribute value.
- `glyphIndex`: Index of the glyph whose attribute is set.

## See Also

- [func insertGlyphs(UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt: Int, characterIndex: Int)](nsglyphstorage/insertglyphs(_:length:forstartingglyphat:characterindex:).md)
  Inserts the given glyphs into the glyph cache and maps them to the specified characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphstorage/setintattribute(_:value:forglyphat:))*