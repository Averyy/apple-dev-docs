# recommendedPixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property

Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelbuffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 17.4+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var recommendedPixelBufferAttributes: CVPixelBufferAttributes { get }
```

#### Discussion

The returned attributes are not sufficient for pixel buffer creation. Use `CVPixelBufferAttributes/init?(merging:)` to merge these with other required attributes.

## See Also

- [func displayedPixelBuffer() -> CVPixelBuffer?](avsamplebuffervideorenderer/displayedpixelbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6zrqb)*