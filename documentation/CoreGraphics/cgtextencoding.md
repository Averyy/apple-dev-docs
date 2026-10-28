# CGTextEncoding

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Text encodings for fonts.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported

## Declaration

```swift
enum CGTextEncoding
```

```c
enum CGTextEncoding : int32_t;
```

## Overview

For more information on setting the font in a graphics context, see [`selectFont(name:size:textEncoding:)`](./cgcontext/selectfont%28name,size,textencoding%29.md).

## Topics

### Constants
- [CGTextEncoding.encodingFontSpecific](./cgtextencoding/encodingfontspecific.md)
  The built-in encoding of the font.
- [CGTextEncoding.encodingMacRoman](./cgtextencoding/encodingmacroman.md)
  The MacRoman encoding. MacRoman is an ASCII variant originally created for use in the Mac OS, in which characters 127 and lower are ASCII, and characters 128 and higher are non-English characters and symbols.
### Initializers
- [init?(rawValue: Int32)](./cgtextencoding/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum CGPathFillRule](./cgpathfillrule.md)
  Rules for determining which regions are interior to a path, used by the [`fillPath(using:)`](./cgcontext/fillpath%28using%29.md) and [`clip(using:)`](./cgcontext/clip%28using%29.md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgtextencoding)*