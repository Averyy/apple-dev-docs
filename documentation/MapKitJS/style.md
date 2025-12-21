# Style

**Framework**: MapKit JS  
**Kind**: class

A set of observable style properties for overlays, including the color and opacity of strokes and fills, and line styles.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Style
```

#### Overview

You can assign a `mapkit.Style` object to an overlay to customize its appearance, such as changing the opacity of the fill or the thickness of the stroke. Style properties are observable, so MapKit JS automatically reflects any change to a style property on the corresponding overlays.

## Topics

### Creating a style
- [new Style(options)](style/styleconstructor.md)
  Creates and initializes a style object.
- [interface StyleConstructorOptions](styleconstructoroptions.md)
  Initial values of options for applying style to overlays.
### Styling fills
- [fillColor](style/fillcolor.md)
  The fill color of a shape.
- [fillOpacity](style/fillopacity.md)
  The opacity of the fill color.
- [fillRule](style/fillrule.md)
  A rule for determining whether a point is inside or outside a polygon.
### Styling lines
- [lineCap](style/linecap.md)
  The style to use when drawing line endings.
- [lineDash](style/linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](style/linedashoffset.md)
  The number of CSS pixels to use as an offset when drawing a line’s dash pattern.
- [lineJoin](style/linejoin.md)
  The corner style to apply when joining line segments.
- [lineWidth](style/linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [lineGradient](style/linegradient.md)
  The gradient to apply along the line.
- [class LineGradient](linegradient.md)
  A line that displays with a gradient along the length of the line.
### Styling strokes
- [strokeColor](style/strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](style/strokeopacity.md)
  The opacity of the stroke color.
- [strokeStart](style/strokestart.md)
  The unit distance along the line where a stroke begins.
- [strokeEnd](style/strokeend.md)
  The unit distance along the line where a stroke ends.
### Instance Methods
- [toString()](style/tostring.md)
  Returns a string representation of the style object.

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
- [class Overlay](overlay.md)
  An abstract base object that defines the methods and properties for map overlays.
- [class CircleOverlay](circleoverlay.md)
  A circular overlay with a configurable radius that centers on a specific geographic coordinate.
- [class PolylineOverlay](polylineoverlay.md)
  An overlay of connected line segments that don’t form a closed shape.
- [class PolygonOverlay](polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [class TileOverlay](tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style)*