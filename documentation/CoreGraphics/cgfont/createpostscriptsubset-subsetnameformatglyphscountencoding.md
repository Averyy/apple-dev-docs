# createPostScriptSubset(subsetName:format:glyphs:count:encoding:)

**Framework**: Core Graphics  
**Kind**: method

Creates a subset of the font in the specified PostScript format.

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
func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?
```

#### Return Value

A subset of the font created from the supplied parameters.

#### Discussion

For more information on PostScript format, see , which is available from [`http://partners.adobe.com/`](https://developer.apple.comhttp://partners.adobe.com/).

## Parameters

- `subsetName`: The name of the subset.
- `format`: The PostScript format of the font.
- `glyphs`: An array that contains the glyphs in the subset.
- `count`: The number of glyphs specified by the   array.
- `encoding`: The default encoding for the subset. You can pass   if you do not want to specify an encoding.

## See Also

- [var postScriptName: CFString?](cgfont/postscriptname.md)
  Obtains the PostScript name of a font.
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](cgfont/cancreatepostscriptsubset(_:).md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [enum CGFontPostScriptFormat](cgfontpostscriptformat.md)
  Possible formats for a PostScript font subset.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptencoding(encoding:).md)
  Creates a PostScript encoding of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:))*