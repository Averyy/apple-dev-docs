# mutablePixelBuffer()

**Framework**: AVFoundation  
**Kind**: method

Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func mutablePixelBuffer() -> CVMutablePixelBuffer?
```

#### Return Value

A CVMutablePixelBuffer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/mutablepixelbuffer())*