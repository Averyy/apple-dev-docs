# MKOverlayPathRenderer

**Framework**: MapKit  
**Kind**: class

The visual representation of a path-based overlay.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKOverlayPathRenderer
```

#### Overview

Use this renderer when a [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) object defines your overlay’s shape. By default, this renderer fills the overlay’s shape and represents the strokes of the path using its current attributes.

You can use this class as-is or subclass it to define additional drawing behaviors. If you subclass it, override the [`createPath()`](mkoverlaypathrenderer/createpath().md) method and use that method to build the appropriate path object. To change the path, invalidate it and recreate the path using the new data your subclass obtains.

## Topics

### Creating and managing the path
- [var path: CGPath!](mkoverlaypathrenderer/path.md)
  The path representing the overlay’s shape.
- [func createPath()](mkoverlaypathrenderer/createpath.md)
  Creates the path for the overlay.
- [func invalidatePath()](mkoverlaypathrenderer/invalidatepath.md)
  Updates the path associated with the overlay renderer.
### Accessing the drawing attributes
- [var fillColor: UIColor?](mkoverlaypathrenderer/fillcolor.md)
  The fill color to use for the path.
- [var strokeColor: UIColor?](mkoverlaypathrenderer/strokecolor.md)
  The stroke color to use for the path.
- [var lineWidth: CGFloat](mkoverlaypathrenderer/linewidth.md)
  The stroke width to use for the path.
- [var lineJoin: CGLineJoin](mkoverlaypathrenderer/linejoin.md)
  The line join style to apply to the corners of the path.
- [var lineCap: CGLineCap](mkoverlaypathrenderer/linecap.md)
  The line cap style to apply to the open ends of the path.
- [var miterLimit: CGFloat](mkoverlaypathrenderer/miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [var lineDashPhase: CGFloat](mkoverlaypathrenderer/linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [var lineDashPattern: [NSNumber]?](mkoverlaypathrenderer/linedashpattern.md)
  An array of numbers specifying the dash pattern to use for the path.
### Drawing the path
- [func applyStrokeProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applystrokeproperties(to:atzoomscale:).md)
  Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [func applyFillProperties(to: CGContext, atZoomScale: MKZoomScale)](mkoverlaypathrenderer/applyfillproperties(to:atzoomscale:).md)
  Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [func strokePath(CGPath, in: CGContext)](mkoverlaypathrenderer/strokepath(_:in:).md)
  Draws a line along the specified path.
- [func fillPath(CGPath, in: CGContext)](mkoverlaypathrenderer/fillpath(_:in:).md)
  Fills the area that the specified path encloses.
- [var shouldRasterize: Bool](mkoverlaypathrenderer/shouldrasterize.md)
  A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.

## Relationships

### Inherits From
- [MKOverlayRenderer](mkoverlayrenderer.md)
### Inherited By
- [MKCircleRenderer](mkcirclerenderer.md)
- [MKMultiPolygonRenderer](mkmultipolygonrenderer.md)
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md)
- [MKPolygonRenderer](mkpolygonrenderer.md)
- [MKPolylineRenderer](mkpolylinerenderer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKPolygon](mkpolygon.md)
  A closed polygon overlay.
- [class MKPolygonRenderer](mkpolygonrenderer.md)
  The visual representation of a single polygon overlay.
- [class MKMultiPolygon](mkmultipolygon.md)
  A collection of multiple closed polygon overlays.
- [class MKMultiPolygonRenderer](mkmultipolygonrenderer.md)
  The visual representation of multiple polygon overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer)*