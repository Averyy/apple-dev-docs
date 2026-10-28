# mostCompatibleStringEncoding

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The string encoding that works best with the font.

**Availability**:
- macOS

## Declaration

```swift
var mostCompatibleStringEncoding: UInt { get }
```

```objc
@property (readonly) NSStringEncoding mostCompatibleStringEncoding;
```

## Discussion

The string encoding in this property is the encoding with the fewest unmatched characters and glyphs in the font. If this value is [`NSASCIIStringEncoding`](../../Foundation/nsasciistringencoding.md), the font could not determine the correct encoding; you should assume the font can render only ASCII characters. The font uses heuristically well-known font encodings to determine the value of this property, so for nonstandard encodings the property may not contain the optimal string encoding.

You can use the [`data(using:)`](../../Foundation/nsstring/data%28using%29.md) or [`data(using:allowLossyConversion:)`](../../Foundation/nsstring/data%28using,allowlossyconversion%29.md) methods of [`NSString`](../../Foundation/nsstring.md) to convert strings to this encoding.

## See Also

### Getting Font Metrics and Information
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the font.
- [var coveredCharacterSet: CharacterSet](./coveredcharacterset.md)
  The character set containing all of the nominal characters that the font can render.
- [var fontDescriptor: NSFontDescriptor](./fontdescriptor.md)
  The font descriptor object for the font.
- [var isFixedPitch: Bool](./isfixedpitch.md)
  A Boolean value indicating whether all glyphs in the font have the same advancement.
- [Advanced Font Metrics](../advanced-font-metrics.md)
  Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/mostcompatiblestringencoding)*