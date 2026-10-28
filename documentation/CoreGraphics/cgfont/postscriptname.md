# postScriptName

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Obtains the PostScript name of a font.

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
var postScriptName: CFString? { get }
```

```c
extern CFStringRefCGFontCopyPostScriptName(CGFontRef font);
```

## Discussion

For more information on PostScript format, see *Adobe Type 1 Font Format*, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## See Also

### Working with PostScript Fonts
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](./cancreatepostscriptsubset%28_%29.md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](./createpostscriptsubset%28subsetname,format,glyphs,count,encoding%29.md)
  Creates a subset of the font in the specified PostScript format.
- [enum CGFontPostScriptFormat](../cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](./createpostscriptencoding%28encoding%29.md)
  Creates a PostScript encoding of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/postscriptname)*