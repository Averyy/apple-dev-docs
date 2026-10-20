# CVPixelFormatType

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Identifier for a pixel format type

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct CVPixelFormatType
```

## Topics

### Instance Properties
- [var isCompressionAvailable: Bool](./cvpixelformattype/iscompressionavailable.md)
  True if any of the planes of this format are compressed and hardware support is available.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Types
- [struct CVPixelFormatDescription](./cvpixelformatdescription.md)
  Defines a pixel format which can be used to create custom pixel buffer types.
- [struct CVFillExtendedPixelsCallBackData](./cvfillextendedpixelscallbackdata.md)
  A structure for holding information that describes a custom extended pixel fill algorithm.
- [struct CVSenselSitingOffsets](./cvsenselsitingoffsets.md)
  Siting offsets, relative to pixel center, of individual sensels/components constituting each pixel.
- [enum CVSenselArrayPattern](./cvsenselarraypattern.md)
  Pattern indicating sensel arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformattype)*