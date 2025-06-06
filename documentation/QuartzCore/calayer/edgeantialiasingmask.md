# edgeAntialiasingMask

**Framework**: Core Animation  
**Kind**: property

A bitmask defining how the edges of the receiver are rasterized.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var edgeAntialiasingMask: CAEdgeAntialiasingMask { get set }
```

#### Discussion

This property specifies which edges of the layer are antialiased and is a combination of the constants defined in [`CAEdgeAntialiasingMask`](caedgeantialiasingmask.md). You can enable or disable antialiasing for each edge (top, left, bottom, right) separately. By default antialiasing is enabled for all edges.

Typically, you would use this property to disable antialiasing for edges that abut edges of other layers, to eliminate the seams that would otherwise occur.

## See Also

- [var isOpaque: Bool](calayer/isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/edgeantialiasingmask)*