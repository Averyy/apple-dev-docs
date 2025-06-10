# makeCGImage(cgImageFormat:)

**Framework**: Accelerate  
**Kind**: method

Returns a Core Graphics image from the pixel buffer’s contents.

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
func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?
```

## Mentions

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
- [Applying flood fills to an image](applying-flood-fills-to-an-image.md)
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)

#### Return Value

A Core Graphics image that contains the source buffer’s contents.

## Parameters

- `cgImageFormat`: The Core Graphics format of the source buffer.

## See Also

- [func copy(to: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/copy(to:).md)
  Copies the contents of the pixel buffer to another pixel buffer.
- [func copy(to: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws](vimage/pixelbuffer/copy(to:cvimageformat:cgimageformat:).md)
  Copies the contents of a pixel buffer to a Core Video pixel buffer.
- [func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)](vimage/pixelbuffer/withcvpixelbuffer(readonly:body:).md)
  Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/makecgimage(cgimageformat:))*