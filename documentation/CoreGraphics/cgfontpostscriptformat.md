# CGFontPostScriptFormat

**Framework**: Core Graphics  
**Kind**: enum

Possible formats for a PostScript font subset.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGFontPostScriptFormat
```

## Topics

### Constants
- [CGFontPostScriptFormat.type1](cgfontpostscriptformat/type1.md)
  A Type 1 font format.
- [CGFontPostScriptFormat.type3](cgfontpostscriptformat/type3.md)
  A Type 3 PostScript format.
- [CGFontPostScriptFormat.type42](cgfontpostscriptformat/type42.md)
  A constant representing a Type 42 font format.
### Initializers
- [init?(rawValue: Int32)](cgfontpostscriptformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var postScriptName: CFString?](cgfont/postscriptname.md)
  Obtains the PostScript name of a font.
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](cgfont/cancreatepostscriptsubset(_:).md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:).md)
  Creates a subset of the font in the specified PostScript format.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](cgfont/createpostscriptencoding(encoding:).md)
  Creates a PostScript encoding of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat)*