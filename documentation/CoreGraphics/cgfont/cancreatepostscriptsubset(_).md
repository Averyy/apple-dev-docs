# canCreatePostScriptSubset(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Determines whether Core Graphics can create a subset of the font in PostScript format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func canCreatePostScriptSubset(_ format: CGFontPostScriptFormat) -> Bool
```

```c
extern bool CGFontCanCreatePostScriptSubset(CGFontRef font, CGFontPostScriptFormat format);
```

## Return Value

Returns `true` if a subset in the PostScript format can be created for the font; `false` otherwise.

## Discussion

For more information on PostScript format, see *Adobe Type 1 Font Format*, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## Parameters

- `format`: A PostScript font format.

## See Also

### Working with PostScript Fonts
- [var postScriptName: CFString?](./postscriptname.md)
  Obtains the PostScript name of a font.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](./createpostscriptsubset%28subsetname,format,glyphs,count,encoding%29.md)
  Creates a subset of the font in the specified PostScript format.
- [enum CGFontPostScriptFormat](../cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](./createpostscriptencoding%28encoding%29.md)
  Creates a PostScript encoding of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/cancreatepostscriptsubset(_:))*