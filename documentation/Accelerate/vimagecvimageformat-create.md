# vImageCVImageFormat_Create(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates the description of image encoding in a Core Video pixel buffer from the specified properties.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCVImageFormat_Create(_ imageFormatType: UInt32, _ matrix: UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, _ cvImageBufferChromaLocation: CFString!, _ baseColorspace: CGColorSpace!, _ alphaIsOneHint: Int32) -> Unmanaged<vImageCVImageFormat>!
```

#### Return Value

A [`vImageCVImageFormat`](vimagecvimageformat.md) instance encoded with the function’s parameters.

#### Discussion

This function derives values that parameters from the image format type don’t specify, such as the number of channels, channel names, and channel descriptions.

## Parameters

- `imageFormatType`: The format type of the image. See  .
- `matrix`: A   that describes the conversion from RGB to the YpCbCr format.
- `cvImageBufferChromaLocation`: The chrominance location.
- `baseColorspace`: The color space of RGB and monochrome images. For YpCbCr images, this is the color space of the RGB image before conversion to YpCbCr using the ARGB-to-YpCbCr conversion matrix. The YpCbCr format RGB primaries and transfer function define the color space.
- `alphaIsOneHint`: A hint that indicates that the function interprets an image with an alpha channel as opaque.

## See Also

- [static func make(format: vImageCVImageFormat.Format, matrix: vImage_ARGBToYpCbCrMatrix, chromaSiting: vImageCVImageFormat.ChromaSiting, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?](vimagecvimageformat/make(format:matrix:chromasiting:colorspace:alphaisopaquehint:).md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.
- [class vImageCVImageFormat](vimagecvimageformat.md)
  A mutable description of image encoding in a Core Video pixel buffer.
- [class vImageConstCVImageFormat](vimageconstcvimageformat.md)
  An immutable description of image encoding in a Core Video pixel buffer.
- [func vImageCVImageFormat_CreateWithCVPixelBuffer(CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_createwithcvpixelbuffer(_:).md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_create(_:_:_:_:_:))*