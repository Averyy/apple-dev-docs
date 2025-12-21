# makeMutablePixelBuffer()

**Framework**: AVFoundation  
**Kind**: method

Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeMutablePixelBuffer() throws -> CVMutablePixelBuffer
```

#### Return Value

A CVMutablePixelBuffer to use for rendering.

#### Discussion

> **Note**: Insufficient memory or other system error.

## See Also

- [func newPixelBuffer() -> CVPixelBuffer?](avvideocompositionrendercontext/newpixelbuffer.md)
  Returns a pixel buffer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/makemutablepixelbuffer())*