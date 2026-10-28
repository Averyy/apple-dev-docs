# contentsAreFlipped()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) contentsAreFlipped;
```

## Return Value

[`true`](../../Swift/true.md) if the layer contents are implicitly flipped when rendered or [`false`](../../Swift/false.md) if they are not. This method returns [`false`](../../Swift/false.md) by default.

## Discussion

This method provides information about whether the layer’s contents are being flipped during drawing. You should not attempt to override this method and return a different value.

If the layer needs to flip its content, it returns [`true`](../../Swift/true.md) from this method and applies a y-flip transform to the graphics context before passing it to the layer’s [`draw(in:)`](./draw%28in%29.md) method. Similarly, the layer converts any rectangles passed to its [`setNeedsDisplay(_:)`](./setneedsdisplay%28_%29.md) into the flipped coordinate space.

## See Also

### Configuring the layer’s rendering behavior
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
- [var edgeAntialiasingMask: CAEdgeAntialiasingMask](./edgeantialiasingmask.md)
  A bitmask defining how the edges of the receiver are rasterized.
- [var isGeometryFlipped: Bool](./isgeometryflipped.md)
  A Boolean that indicates whether the geometry of the layer and its sublayers is flipped vertically.
- [var drawsAsynchronously: Bool](./drawsasynchronously.md)
  A Boolean indicating whether drawing commands are deferred and processed asynchronously in a background thread.
- [var shouldRasterize: Bool](./shouldrasterize.md)
  A Boolean that indicates whether the layer is rendered as a bitmap before compositing. Animatable
- [var rasterizationScale: CGFloat](./rasterizationscale.md)
  The scale at which to rasterize content, relative to the coordinate space of the layer. Animatable
- [var contentsFormat: CALayerContentsFormat](./contentsformat.md)
  A hint for the desired storage format of the layer contents.
- [func render(in: CGContext)](./render%28in%29.md)
  Renders the layer and its sublayers into the specified context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contentsareflipped())*