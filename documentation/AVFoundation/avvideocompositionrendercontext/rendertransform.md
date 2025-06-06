# renderTransform

**Framework**: AVFoundation  
**Kind**: property

A transform to apply to the source image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderTransform: CGAffineTransform { get }
```

#### Discussion

The transform to apply to the source image incorporating the [`renderScale`](avvideocompositionrendercontext/renderscale.md), [`pixelAspectRatio`](avvideocompositionrendercontext/pixelaspectratio.md), and [`edgeWidths`](avvideocompositionrendercontext/edgewidths.md).

The coordinate system origin is the top left corner of the buffer.

## See Also

- [var videoComposition: AVVideoComposition](avvideocompositionrendercontext/videocomposition.md)
  The video composition being rendered.
- [var highQualityRendering: Bool](avvideocompositionrendercontext/highqualityrendering.md)
  The rendering quality to use.
- [var renderScale: Float](avvideocompositionrendercontext/renderscale.md)
  A scaling ratio that is applied when rendering frames.
- [var size: CGSize](avvideocompositionrendercontext/size.md)
  The width and height for the rendering frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/rendertransform)*