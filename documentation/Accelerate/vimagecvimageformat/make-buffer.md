# make(buffer:)

**Framework**: Accelerate  
**Kind**: method

Creates the description of the image encoding in an existing Core Video pixel buffer.

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
static func make(buffer: CVPixelBuffer) -> vImageCVImageFormat?
```

## Mentions

- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)

#### Return Value

A [`vImageCVImageFormat`](vimagecvimageformat.md) instance that describes the specified pixel buffer’s pixel format.

## Parameters

- `buffer`: The source Core Video pixel buffer.

## See Also

- [func vImageCVImageFormat_CreateWithCVPixelBuffer(CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_createwithcvpixelbuffer(_:).md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [static func make(format: vImageCVImageFormat.Format, matrix: vImage_ARGBToYpCbCrMatrix, chromaSiting: vImageCVImageFormat.ChromaSiting, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?](vimagecvimageformat/make(format:matrix:chromasiting:colorspace:alphaisopaquehint:).md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.
- [static func make(format: vImageCVImageFormat.Format, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?](vimagecvimageformat/make(format:colorspace:alphaisopaquehint:).md)
  Creates the description of an RGB image encoding in a Core Video pixel buffer from the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/make(buffer:))*