# AVVideoCompositionRenderContext

**Framework**: AVFoundation  
**Kind**: class

An object that defines the context in which custom compositors render pixel buffers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVVideoCompositionRenderContext
```

#### Overview

A render context provides size and scaling information and offers a service for efficiently providing pixel buffers from a managed pool of buffers.

## Topics

### Creating the Pixel Buffer
- [func newPixelBuffer() -> CVPixelBuffer?](avvideocompositionrendercontext/newpixelbuffer.md)
  Returns a pixel buffer to use for rendering.
### Getting the Render Settings
- [var videoComposition: AVVideoComposition](avvideocompositionrendercontext/videocomposition.md)
  The video composition being rendered.
- [var highQualityRendering: Bool](avvideocompositionrendercontext/highqualityrendering.md)
  The rendering quality to use.
- [var renderScale: Float](avvideocompositionrendercontext/renderscale.md)
  A scaling ratio that is applied when rendering frames.
- [var renderTransform: CGAffineTransform](avvideocompositionrendercontext/rendertransform.md)
  A transform to apply to the source image.
- [var size: CGSize](avvideocompositionrendercontext/size.md)
  The width and height for the rendering frames.
### Getting Pixel and Edge Width Information
- [var edgeWidths: AVEdgeWidths](avvideocompositionrendercontext/edgewidths.md)
  The width of the edge processing region on the left, top, right, and bottom edges, in pixels.
- [struct AVEdgeWidths](avedgewidths.md)
  A structure that defines edge processing region widths.
- [var pixelAspectRatio: AVPixelAspectRatio](avvideocompositionrendercontext/pixelaspectratio.md)
  The pixel aspect ratio for rendered frames.
- [struct AVPixelAspectRatio](avpixelaspectratio.md)
  A structure that defines a pixel aspect ratio for a rendering context.
### Instance Methods
- [func mutablePixelBuffer() -> CVMutablePixelBuffer?](avvideocompositionrendercontext/mutablepixelbuffer.md)
  Vends a CVMutablePixelBuffer to use for rendering. The buffer will have its kCVImageBufferCleanApertureKey and kCVImageBufferPixelAspectRatioKey attachments set to match the current composition processor properties.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func renderContextChanged(AVVideoCompositionRenderContext)](avvideocompositing/rendercontextchanged(_:).md)
  Tells the compositor that the composition changed render contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext)*