# make(format:matrix:chromaSiting:colorSpace:alphaIsOpaqueHint:)

**Framework**: Accelerate  
**Kind**: method

Creates the description of image encoding in a Core Video pixel buffer from the specified properties.

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
static func make(format: vImageCVImageFormat.Format, matrix: vImage_ARGBToYpCbCrMatrix, chromaSiting: vImageCVImageFormat.ChromaSiting, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?
```

#### Return Value

A [`vImageCVImageFormat`](vimagecvimageformat.md) instance encoded with the function’s parameters.

#### Discussion

This function derives values that parameters from the image format type don’t specify, such as the number of channels, channel names, and channel descriptions.

## Parameters

- `format`: The format type of the image.
- `matrix`: A   that describes the conversion from RGB to the YpCbCr format.
- `chromaSiting`: The chrominance location.
- `colorSpace`: The color space of RGB and monochrome images. For YpCbCr images, this is the color space of the RGB image before conversion to YpCbCr using the ARGB-to-YpCbCr conversion matrix. The YpCbCr format RGB primaries and transfer function define the color space.
- `alphaIsOpaqueHint`: A hint that indicates that the function interprets an image with an alpha channel as opaque.

## See Also

- [func vImageCVImageFormat_Create(UInt32, UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, CFString!, CGColorSpace!, Int32) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_create(_:_:_:_:_:).md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.
- [static func make(buffer: CVPixelBuffer) -> vImageCVImageFormat?](vimagecvimageformat/make(buffer:).md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [static func make(format: vImageCVImageFormat.Format, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?](vimagecvimageformat/make(format:colorspace:alphaisopaquehint:).md)
  Creates the description of an RGB image encoding in a Core Video pixel buffer from the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/make(format:matrix:chromasiting:colorspace:alphaisopaquehint:))*