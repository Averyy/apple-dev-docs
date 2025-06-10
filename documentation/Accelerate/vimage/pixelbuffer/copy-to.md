# copy(to:)

**Framework**: Accelerate  
**Kind**: method

Copies the contents of the pixel buffer to another pixel buffer.

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
func copy(to destinationBuffer: vImage.PixelBuffer<Format>)
```

## Parameters

- `destinationBuffer`: The destination pixel buffer.

## See Also

- [func copy(to: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws](vimage/pixelbuffer/copy(to:cvimageformat:cgimageformat:).md)
  Copies the contents of a pixel buffer to a Core Video pixel buffer.
- [func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?](vimage/pixelbuffer/makecgimage(cgimageformat:).md)
  Returns a Core Graphics image from the pixel buffer’s contents.
- [func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)](vimage/pixelbuffer/withcvpixelbuffer(readonly:body:).md)
  Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/copy(to:))*