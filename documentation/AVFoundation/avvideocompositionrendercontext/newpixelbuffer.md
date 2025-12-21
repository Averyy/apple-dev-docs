# newPixelBuffer()

**Framework**: AVFoundation  
**Kind**: method

Returns a pixel buffer to use for rendering.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newPixelBuffer() -> CVPixelBuffer?
```

#### Return Value

A [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) to use for rendering.

#### Discussion

The buffer’s [`kCVImageBufferCleanApertureKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferCleanApertureKey) and [`kCVImageBufferPixelAspectRatioKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferPixelAspectRatioKey) attachments are set to match the current composition processor properties. You’re responsible for calling [`CVBufferRelease`](https://developer.apple.com/documentation/CoreVideo/CVBufferRelease) on the pixel buffer.

## See Also

- [func makeMutablePixelBuffer() throws -> CVMutablePixelBuffer](avvideocompositionrendercontext/makemutablepixelbuffer.md)
  Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/newpixelbuffer())*