# contentsAreFlipped()

**Framework**: Core Animation  
**Kind**: method

Returns a Boolean indicating whether the layer content is implicitly flipped when rendered.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func contentsAreFlipped() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the layer contents are implicitly flipped when rendered or [`false`](https://developer.apple.com/documentation/Swift/false) if they are not. This method returns [`false`](https://developer.apple.com/documentation/Swift/false) by default.

#### Discussion

This method provides information about whether the layer’s contents are being flipped during drawing. You should not attempt to override this method and return a different value.

If the layer needs to flip its content, it returns [`true`](https://developer.apple.com/documentation/Swift/true) from this method and applies a y-flip transform to the graphics context before passing it to the layer’s [`draw(in:)`](calayer/draw(in:).md) method. Similarly, the layer converts any rectangles passed to its [`setNeedsDisplay(_:)`](calayer/setneedsdisplay(_:).md) into the flipped coordinate space.

## See Also

- [var isOpaque: Bool](calayer/isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](calayer/edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contentsareflipped())*