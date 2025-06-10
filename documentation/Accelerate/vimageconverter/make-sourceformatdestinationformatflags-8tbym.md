# make(sourceFormat:destinationFormat:flags:)

**Framework**: Accelerate  
**Kind**: method

Creates a vImage converter that converts from one vImage Core Graphics image format to another.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImage_CGImageFormat, flags options: vImage.Options = .noFlags) throws -> vImageConverter
```

## Mentions

- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)

## See Also

- [func vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [static func make(sourceFormat: vImageCVImageFormat, destinationFormat: vImage_CGImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-8iupf.md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImageCVImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-fub5.md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImage_CGImageFormat, colorConversionInfo: CGColorConversionInfo) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:colorconversioninfo:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter/make(sourceformat:destinationformat:flags:)-8tbym)*