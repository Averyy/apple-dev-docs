# highQualityRendering

**Framework**: AVFoundation  
**Kind**: property

The rendering quality to use.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var highQualityRendering: Bool { get }
```

#### Discussion

Specifies that the custom compositor should use higher quality, potentially slower algorithms.

Generally this property is [`true`](https://developer.apple.com/documentation/swift/true) for non-real-time use cases.

## See Also

- [var videoComposition: AVVideoComposition](avvideocompositionrendercontext/videocomposition.md)
  The video composition being rendered.
- [var renderScale: Float](avvideocompositionrendercontext/renderscale.md)
  A scaling ratio that is applied when rendering frames.
- [var renderTransform: CGAffineTransform](avvideocompositionrendercontext/rendertransform.md)
  A transform to apply to the source image.
- [var size: CGSize](avvideocompositionrendercontext/size.md)
  The width and height for the rendering frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/highqualityrendering)*