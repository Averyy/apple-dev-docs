# NSGlyphStorage

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a glyph storage object must implement to interact properly with [`NSGlyphGenerator`](nsglyphgenerator.md).

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSGlyphStorage
```

#### Overview

An example of a class that conforms to the [`NSGlyphStorage`](nsglyphstorage.md) protocol is [`NSLayoutManager`](nslayoutmanager.md).

## Topics

### Returning text storage
- [func attributedString() -> NSAttributedString](nsglyphstorage/attributedstring.md)
  Returns the text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.
### Returning glyph display options
- [func layoutOptions() -> Int](nsglyphstorage/layoutoptions.md)
  Returns the current layout options.
### Modifying the glyph cache
- [func insertGlyphs(UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt: Int, characterIndex: Int)](nsglyphstorage/insertglyphs(_:length:forstartingglyphat:characterindex:).md)
  Inserts the given glyphs into the glyph cache and maps them to the specified characters.
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](nsglyphstorage/setintattribute(_:value:forglyphat:).md)
  Sets a custom attribute value for a given glyph.
### Constants
- [Layout Options](layout-options.md)
  Layout options returned as a bit mask by the [`layoutOptions()`](nsglyphstorage/layoutoptions().md) method.

## Relationships

### Conforming Types
- [NSLayoutManager](nslayoutmanager.md)

## See Also

- [typealias NSGlyph](nsglyph.md)
  The type used to specify glyphs.
- [class NSGlyphGenerator](nsglyphgenerator.md)
  An object that performs the initial, nominal glyph generation phase in the layout process.
- [class NSGlyphInfo](nsglyphinfo.md)
  A glyph attribute in an attributed string.
- [Reserved Glyph Codes](reserved-glyph-codes.md)
  These constants define reserved glyph codes.
- [enum NSFontRenderingMode](nsfontrenderingmode.md)
  The font rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphstorage)*