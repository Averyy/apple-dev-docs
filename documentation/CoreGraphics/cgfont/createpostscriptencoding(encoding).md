# createPostScriptEncoding(encoding:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Creates a PostScript encoding of a font.

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
func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?
```

```c
extern CFDataRefCGFontCreatePostScriptEncoding(CGFontRef font, const CGGlyph encoding[256]);
```

#### Return Value

A PostScript encoding of the font that contains glyphs in the specified encoding.

#### Discussion

For more information on PostScript format, see *Adobe Type 1 Font Format*, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## Parameters

- `encoding`: The encoding to use.

## See Also

### Working with PostScript Fonts
- [var postScriptName: CFString?](./postscriptname.md)
  Obtains the PostScript name of a font.
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](./cancreatepostscriptsubset%28_%29.md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](./createpostscriptsubset%28subsetname,format,glyphs,count,encoding%29.md)
  Creates a subset of the font in the specified PostScript format.
- [enum CGFontPostScriptFormat](../cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/createpostscriptencoding(encoding:))*