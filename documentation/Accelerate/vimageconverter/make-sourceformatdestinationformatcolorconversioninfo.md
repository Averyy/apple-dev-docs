# make(sourceFormat:destinationFormat:colorConversionInfo:)

**Framework**: Accelerate  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImage_CGImageFormat, colorConversionInfo: CGColorConversionInfo) throws -> vImageConverter
```

## See Also

- [static func make(sourceFormat: vImageCVImageFormat, destinationFormat: vImage_CGImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-8iupf.md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImage_CGImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-8tbym.md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImageCVImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-fub5.md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter/make(sourceformat:destinationformat:colorconversioninfo:))*