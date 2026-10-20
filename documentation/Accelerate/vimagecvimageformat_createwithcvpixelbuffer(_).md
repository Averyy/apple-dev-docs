# vImageCVImageFormat_CreateWithCVPixelBuffer(_:)

**Framework**: Accelerate  
**Kind**: func

Creates the description of the image encoding in an existing Core Video pixel buffer.

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
func vImageCVImageFormat_CreateWithCVPixelBuffer(_ buffer: CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!
```

## Mentions

- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)

#### Return Value

A [`vImageCVImageFormat`](vimagecvimageformat.md) instance that describes the specified pixel buffer’s pixel format.

## Parameters

- `buffer`: The source Core Video pixel buffer.

## See Also

- [static func make(buffer: CVPixelBuffer) -> vImageCVImageFormat?](vimagecvimageformat/make(buffer:).md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [class vImageCVImageFormat](vimagecvimageformat.md)
  A mutable description of image encoding in a Core Video pixel buffer.
- [class vImageConstCVImageFormat](vimageconstcvimageformat.md)
  An immutable description of image encoding in a Core Video pixel buffer.
- [func vImageCVImageFormat_Create(UInt32, UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, CFString!, CGColorSpace!, Int32) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_create(_:_:_:_:_:).md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_createwithcvpixelbuffer(_:))*