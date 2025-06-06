# CGTextEncoding

**Framework**: Core Graphics  
**Kind**: enum

Text encodings for fonts.

**Availability**:
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CGTextEncoding
```

#### Overview

For more information on setting the font in a graphics context, see [`selectFont(name:size:textEncoding:)`](cgcontext/selectfont(name:size:textencoding:).md).

## Topics

### Constants
- [CGTextEncoding.encodingFontSpecific](cgtextencoding/encodingfontspecific.md)
  The built-in encoding of the font.
- [CGTextEncoding.encodingMacRoman](cgtextencoding/encodingmacroman.md)
  The MacRoman encoding. MacRoman is an ASCII variant originally created for use in the Mac OS, in which characters 127 and lower are ASCII, and characters 128 and higher are non-English characters and symbols.
### Initializers
- [init?(rawValue: Int32)](cgtextencoding/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CGPathFillRule](cgpathfillrule.md)
  Rules for determining which regions are interior to a path, used by the [`fillPath(using:)`](cgcontext/fillpath(using:).md) and [`clip(using:)`](cgcontext/clip(using:).md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgtextencoding)*