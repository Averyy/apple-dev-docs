# drawsAsynchronously

**Framework**: Core Animation  
**Kind**: property

A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var drawsAsynchronously: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the graphics context used to draw the layer’s contents queues drawing commands and executes them on a background thread rather than executing them synchronously. Performing these commands asynchronously can improve performance in some apps. However, you should always measure the actual performance benefits before enabling this capability.

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isOpaque: Bool](calayer/isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](calayer/edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
- [func contentsAreFlipped() -> Bool](calayer/contentsareflipped.md)
  Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.
- [var isGeometryFlipped: Bool](calayer/isgeometryflipped.md)
  A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [var shouldRasterize: Bool](calayer/shouldrasterize.md)
  A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [var rasterizationScale: CGFloat](calayer/rasterizationscale.md)
  The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [var contentsFormat: CALayerContentsFormat](calayer/contentsformat.md)
  A hint for the desired storage format of the layer contents.
- [func render(in: CGContext)](calayer/render(in:).md)
  Renders the layer and its sublayers into the specified context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/drawsasynchronously)*