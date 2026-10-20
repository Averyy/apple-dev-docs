# renderScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A scaling ratio that is applied when rendering frames.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderScale: Float { get }
```

```objc
@property (nonatomic, readonly) float renderScale;
```

## See Also

### Getting the render settings
- [var videoComposition: AVVideoComposition](./videocomposition.md)
  The video composition being rendered.
- [var highQualityRendering: Bool](./highqualityrendering.md)
  The rendering quality to use.
- [var renderTransform: CGAffineTransform](./rendertransform.md)
  A transform to apply to the source image.
- [var size: CGSize](./size.md)
  The width and height for the rendering frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/renderscale)*