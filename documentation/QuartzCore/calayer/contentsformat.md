# contentsFormat

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A hint for the desired storage format of the layer contents.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var contentsFormat: CALayerContentsFormat { get set }
```

```objc
@property (copy) CALayerContentsFormat contentsFormat;
```

## Discussion

The default value of this property is [`RGBA8Uint`](../calayercontentsformat/rgba8uint.md).

[`UIView`](../../UIKit/uiview.md) and layer-backed [`NSView`](../../AppKit/nsview.md) objects may change the value to a format appropriate for the current device.

## See Also

### Configuring the layer’s rendering behavior
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](./edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
- [func contentsAreFlipped() -> Bool](./contentsareflipped%28%29.md)
  Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [var isGeometryFlipped: Bool](./isgeometryflipped.md)
  A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [var drawsAsynchronously: Bool](./drawsasynchronously.md)
  A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [var shouldRasterize: Bool](./shouldrasterize.md)
  A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [var rasterizationScale: CGFloat](./rasterizationscale.md)
  The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [func render(in: CGContext)](./render%28in%29.md)
  Renders the layer and its sublayers into the specified context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contentsformat)*