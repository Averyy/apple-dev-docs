# copy(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Copies the contents of the pixel buffer to another pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func copy(to destinationBuffer: vImage.PixelBuffer<Format>)
```

Available when `Format` conforms to `StaticPixelFormat`.

## Parameters

- `destinationBuffer`: The destination pixel buffer.

## See Also

### Pixel buffer methods
- [func copy(to: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws](./copy%28to,cvimageformat,cgimageformat%29.md)
  Copies the contents of a pixel buffer to a Core Video pixel buffer.
- [func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?](./makecgimage%28cgimageformat%29.md)
  Returns a Core Graphics image from the pixel buffer’s contents.
- [func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)](./withcvpixelbuffer%28readonly,body%29.md)
  Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/copy(to:))*