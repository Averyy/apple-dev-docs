# newPixelBuffer()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a pixel buffer to use for rendering.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.9+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use newReadOnlyPixelBuffer() instead

## Declaration

```swift
func newPixelBuffer() -> CVPixelBuffer?
```

```objc
- (CVPixelBufferRef) newPixelBuffer;
```

## Return Value

A [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md) to use for rendering.

## Discussion

The buffer’s [`kCVImageBufferCleanApertureKey`](../../CoreVideo/kcvimagebuffercleanaperturekey.md) and [`kCVImageBufferPixelAspectRatioKey`](../../CoreVideo/kcvimagebufferpixelaspectratiokey.md) attachments are set to match the current composition processor properties. You’re responsible for calling [`CVBufferRelease`](../../CoreVideo/cvbufferrelease.md) on the pixel buffer.

## See Also

### Creating the pixel buffer
- [func makeMutablePixelBuffer() throws -> CVMutablePixelBuffer](./makemutablepixelbuffer%28%29.md)
  Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/newpixelbuffer())*