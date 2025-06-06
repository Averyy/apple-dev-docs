# render(in:)

**Framework**: Core Animation  
**Kind**: method

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

#### Discussion

This method renders directly from the layer tree, ignoring any animations added to the render tree. Renders in the coordinate space of the layer.

The following code shows how you can use [`render(in:)`](calayer/render(in:).md) to create a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) from a [`CAShapeLayer`](cashapelayer.md) with a [`path`](cashapelayer/path.md) that describes a circle. After creating the layer, the code creates a [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) into which the circle is rendered. After rendering, [`UIGraphicsGetImageFromCurrentImageContext()`](https://developer.apple.com/documentation/UIKit/UIGraphicsGetImageFromCurrentImageContext()) generates the image.

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

> ❗ **Important**:  The OS X v10.5 implementation of this method does not support the entire Core Animation composition model. `QCCompositionLayer`, `CAOpenGLLayer`, and `QTMovieLayer` layers are not rendered. Additionally, layers that use 3D transforms are not rendered, nor are layers that specify [`backgroundFilters`](calayer/backgroundfilters.md), [`filters`](calayer/filters.md), [`compositingFilter`](calayer/compositingfilter.md), or a [`mask`](calayer/mask.md) values. Future versions of macOS may add support for rendering these layers and properties.

 The OS X v10.5 implementation of this method does not support the entire Core Animation composition model. `QCCompositionLayer`, `CAOpenGLLayer`, and `QTMovieLayer` layers are not rendered. Additionally, layers that use 3D transforms are not rendered, nor are layers that specify [`backgroundFilters`](calayer/backgroundfilters.md), [`filters`](calayer/filters.md), [`compositingFilter`](calayer/compositingfilter.md), or a [`mask`](calayer/mask.md) values. Future versions of macOS may add support for rendering these layers and properties.

## Parameters

- `ctx`: The graphics context to use to render the layer.

## See Also

- [var isOpaque: Bool](calayer/isopaque.md)
  A Boolean value indicating whether the layer contains completely opaque content.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/render(in:))*