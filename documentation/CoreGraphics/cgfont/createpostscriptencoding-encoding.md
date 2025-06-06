# createPostScriptEncoding(encoding:)

**Framework**: Core Graphics  
**Kind**: method

Creates a PostScript encoding of a font.

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
func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?
```

#### Return Value

A PostScript encoding of the font that contains glyphs in the specified encoding.

#### Discussion

For more information on PostScript format, see , which is available from [`http://partners.adobe.com/`](https://developer.apple.comhttp://partners.adobe.com/).

## Parameters

- `encoding`: The encoding to use.

## See Also

- [var postScriptName: CFString?](cgfont/postscriptname.md)
  Obtains the PostScript name of a font.
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](cgfont/cancreatepostscriptsubset(_:).md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:).md)
  Creates a subset of the font in the specified PostScript format.
- [enum CGFontPostScriptFormat](cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/createpostscriptencoding(encoding:))*