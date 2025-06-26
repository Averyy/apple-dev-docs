# vImageConverter

**Framework**: Accelerate  
**Kind**: class

A description of a conversion from one image format to another.

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
class vImageConverter
```

## Mentions

- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)

#### Overview

The [`vImageConverter`](vimageconverter.md) class is an opaque type that contains information needed to do a rapid conversion from one image type to another.

You use the converter creation functions, for example, [`vImageConverter_CreateWithCGImageFormat(_:_:_:_:_:)`](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md), to create instances of converters. Sometimes, there can be an overhead when creating a converter, so create them in advance and reuse them. Converters are thread safe; that is, you can use the same object concurrently in multiple threads.

## Topics

### Instance Properties
- [var destinationBufferCount: Int](vimageconverter/destinationbuffercount.md)
  The number of destination buffers written to by the converter.
- [var sourceBufferCount: Int](vimageconverter/sourcebuffercount.md)
  The number of source buffers written to by the converter.
### Instance Methods
- [func convert(source: vImage_Buffer, destination: inout vImage_Buffer, flags: vImage.Options) throws](vimageconverter/convert(source:destination:flags:).md)
  Converts the pixels in a vImage buffer to another format.
- [func mustOperateOutOfPlace(source: vImage_Buffer, destination: vImage_Buffer, flags: vImage.Options) throws -> Bool](vimageconverter/mustoperateoutofplace(source:destination:flags:).md)
  Determines whether a converter is capable of operating in place.
- [func destinationBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]](vimageconverter/destinationbuffers(colorspace:).md)
  Returns a list of vImage destination buffer types, specifying the order of planes.
- [func sourceBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]](vimageconverter/sourcebuffers(colorspace:).md)
  Returns a list of vImage source buffer types, specifying the order of planes.
- [func convert<Src, Dest>(from: vImage.PixelBuffer<Src>, to: vImage.PixelBuffer<Dest>) throws](vimageconverter/convert(from:to:)-9s7p7.md)
- [func convert<F1, F2>(from: [vImage.PixelBuffer<F1>], to: [vImage.PixelBuffer<F2>]) throws](vimageconverter/convert(from:to:)-587gc.md)
- [func makeCGToCVPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](vimageconverter/makecgtocvpixelbuffers(referencing:).md)
- [func makeCVToCGPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](vimageconverter/makecvtocgpixelbuffers(referencing:).md)
### Type Methods
- [static func make(sourceFormat: vImageCVImageFormat, destinationFormat: vImage_CGImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-8iupf.md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImage_CGImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-8tbym.md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImageCVImageFormat, flags: vImage.Options) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:flags:)-fub5.md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [static func make(sourceFormat: vImage_CGImageFormat, destinationFormat: vImage_CGImageFormat, colorConversionInfo: CGColorConversionInfo) throws -> vImageConverter](vimageconverter/make(sourceformat:destinationformat:colorconversioninfo:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func vImageConverter_CreateWithCGImageFormat(UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts from one vImage Core Graphics image format to another.
- [func vImageConverter_CreateWithCGColorConversionInfo(CGColorConversionInfo, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcgcolorconversioninfo(_:_:_:_:_:_:).md)
  Creates an any-to-any converter that uses a color conversion information object to convert from one image format to another.
- [func vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcgtocvimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Graphics-formatted image to a Core Video-formatted image.
- [func vImageConverter_CreateForCVToCGImageFormat(vImageCVImageFormat, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createforcvtocgimageformat(_:_:_:_:_:).md)
  Creates a vImage converter that converts a Core Video-formatted image to a Core Graphics-formatted image.
- [func vImageConverter_CreateWithColorSyncCodeFragment(CFTypeRef, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>!, UnsafePointer<CGFloat>!, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<vImageConverter>!](vimageconverter_createwithcolorsynccodefragment(_:_:_:_:_:_:).md)
  Creates a vImage converter to convert from one vImage Core Graphics image format to another, using custom ColorSync transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter)*