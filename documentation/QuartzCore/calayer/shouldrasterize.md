# shouldRasterize

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var shouldRasterize: Bool { get set }
```

```objc
@property BOOL shouldRasterize;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the layer is rendered as a bitmap in its local coordinate space and then composited to the destination with any other content. Shadow effects and any filters in the [`filters`](./filters.md) property are rasterized and included in the bitmap. However, the current opacity of the layer is not rasterized. If the rasterized bitmap requires scaling during compositing, the filters in the [`minificationFilter`](./minificationfilter.md) and [`magnificationFilter`](./magnificationfilter.md) properties are applied as needed.

When the value of this property is [`false`](../../Swift/false.md), the layer is composited directly into the destination whenever possible. The layer may still be rasterized prior to compositing if certain features of the compositing model (such as the inclusion of filters) require it.

The default value of this property is [`false`](../../Swift/false.md).

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
- [var rasterizationScale: CGFloat](./rasterizationscale.md)
  The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [var contentsFormat: CALayerContentsFormat](./contentsformat.md)
  A hint for the desired storage format of the layer contents.
- [func render(in: CGContext)](./render%28in%29.md)
  Renders the layer and its sublayers into the specified context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/shouldrasterize)*