# CGFontPostScriptFormat

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Possible formats for a PostScript font subset.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CGFontPostScriptFormat
```

```c
enum CGFontPostScriptFormat : int32_t;
```

## Topics

### Constants
- [CGFontPostScriptFormat.type1](./cgfontpostscriptformat/type1.md)
  A Type 1 font format.
- [CGFontPostScriptFormat.type3](./cgfontpostscriptformat/type3.md)
  A Type 3 PostScript format.
- [CGFontPostScriptFormat.type42](./cgfontpostscriptformat/type42.md)
  A constant representing a Type 42 font format.
### Initializers
- [init?(rawValue: Int32)](./cgfontpostscriptformat/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with PostScript Fonts
- [var postScriptName: CFString?](./cgfont/postscriptname.md)
  Obtains the PostScript name of a font.
- [func canCreatePostScriptSubset(CGFontPostScriptFormat) -> Bool](./cgfont/cancreatepostscriptsubset%28_%29.md)
  Determines whether Core Graphics can create a subset of the font in PostScript format.
- [func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?](./cgfont/createpostscriptsubset%28subsetname,format,glyphs,count,encoding%29.md)
  Creates a subset of the font in the specified PostScript format.
- [func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?](./cgfont/createpostscriptencoding%28encoding%29.md)
  Creates a PostScript encoding of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat)*