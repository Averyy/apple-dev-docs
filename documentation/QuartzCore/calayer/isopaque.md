# isOpaque

**Framework**: Core Animation  
**Kind**: property

A Boolean value indicating whether the layer contains completely opaque content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isOpaque: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). If your app draws completely opaque content that fills the layer’s bounds, setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) lets the system optimize the rendering behavior for the layer. Specifically, when the layer creates the backing store for your drawing commands, Core Animation omits the alpha channel of that backing store. Doing so can improve the performance of compositing operations. If you set the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true), you must fill the layer’s bounds with opaque content.

Setting this property affects only the backing store managed by Core Animation. If you assign an image with an alpha channel to the layer’s [`contents`](calayer/contents.md) property, that image retains its alpha channel regardless of the value of this property.

## See Also

- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](calayer/edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
- [func contentsAreFlipped() -> Bool](calayer/contentsareflipped.md)
  Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [var isGeometryFlipped: Bool](calayer/isgeometryflipped.md)
  A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [var drawsAsynchronously: Bool](calayer/drawsasynchronously.md)
  A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [var shouldRasterize: Bool](calayer/shouldrasterize.md)
  A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [var rasterizationScale: CGFloat](calayer/rasterizationscale.md)
  The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [var contentsFormat: CALayerContentsFormat](calayer/contentsformat.md)
  A hint for the desired storage format of the layer contents.
- [func render(in: CGContext)](calayer/render(in:).md)
  Renders the layer and its sublayers into the specified context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/isopaque)*