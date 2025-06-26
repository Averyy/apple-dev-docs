# recommededPixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property

Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelbuffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 17.4+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var recommededPixelBufferAttributes: CVPixelBufferAttributes { get }
```

#### Discussion

The returned attributes are not sufficient for pixel buffer creation. Use `CVPixelBufferAttributes/init?(merging:)` to merge these with other required attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/recommededpixelbufferattributes)*