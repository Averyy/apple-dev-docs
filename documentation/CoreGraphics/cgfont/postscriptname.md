# postScriptName

**Framework**: Core Graphics  
**Kind**: property

Obtains the PostScript name of a font.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var postScriptName: CFString? { get }
```

#### Discussion

For more information on PostScript format, see , which is available from [`http://partners.adobe.com/`](https://developer.apple.comhttp://partners.adobe.com/).

## See Also

- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](cgfont/cancreatepostscriptsubset(_:).md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:).md)
  Creates a subset of the font in the specified PostScript format.
- [enum CGFontPostScriptFormat](cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptencoding(encoding:).md)
  Creates a PostScript encoding of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/postscriptname)*