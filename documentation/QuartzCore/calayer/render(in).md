# render(in:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Renders the layer and its sublayers into the specified context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func render(in ctx: CGContext)
```

```objc
- (void) renderInContext:(CGContextRef) ctx;
```

## Discussion

This method renders directly from the layer tree, ignoring any animations added to the render tree. Renders in the coordinate space of the layer.

The following code shows how you can use [`render(in:)`](./render%28in%29.md) to create a [`UIImage`](../../UIKit/uiimage.md) from a [`CAShapeLayer`](../cashapelayer.md) with a [`path`](../cashapelayer/path.md) that describes a circle. After creating the layer, the code creates a [`CGContext`](../../CoreGraphics/cgcontext.md) into which the circle is rendered. After rendering, [`UIGraphicsGetImageFromCurrentImageContext()`](../../UIKit/uigraphicsgetimagefromcurrentimagecontext%28%29.md) generates the image.

```swift
let diameter: CGFloat = 100
let rect = CGRect(origin: CGPoint.zero,
                  size: CGSize(width: diameter, height: diameter))
    
let shapeLayer = CAShapeLayer()
shapeLayer.fillColor = UIColor.white.cgColor
shapeLayer.lineWidth = 10
shapeLayer.path = CGPath(ellipseIn: rect,
                         transform: nil)
        
let renderer = UIGraphicsImageRenderer(size: rect.size)
     
let image = renderer.image {
    context in

    return shapeLayer.render(in: context.cgContext)
}

```

> ❗ **Important**:  The OS X v10.5 implementation of this method does not support the entire Core Animation composition model. `QCCompositionLayer`, `CAOpenGLLayer`, and `QTMovieLayer` layers are not rendered. Additionally, layers that use 3D transforms are not rendered, nor are layers that specify [`backgroundFilters`](./backgroundfilters.md), [`filters`](./filters.md), [`compositingFilter`](./compositingfilter.md), or a [`mask`](./mask.md) values. Future versions of macOS may add support for rendering these layers and properties.

## Parameters

- `ctx`: The graphics context to use to render the layer.

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
- [var contentsFormat: CALayerContentsFormat](./contentsformat.md)
  A hint for the desired storage format of the layer contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/render(in:))*