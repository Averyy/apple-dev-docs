# mapkit.Style

**Framework**: MapKit JS  
**Kind**: class

A set of observable attributes for overlays, including the color and opacity of strokes and fills, and line styles.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Style
```

#### Overview

You can assign a `mapkit.Style` object to an overlay to customize its appearance, such as changing the opacity of the fill or the thickness of the stroke. Style properties are observable, so MapKit JS automatically reflects any change to a style property on the corresponding overlays.

## Topics

### Creating a style
- [mapkit.Style](mapkit.style/mapkit.style.md)
  Creates and initializes a style object.
- [StyleConstructorOptions](styleconstructoroptions.md)
  Initial values of options for applying style to overlays.
### Styling fills
- [fillColor](mapkit.style/fillcolor.md)
  The fill color of a shape.
- [fillOpacity](mapkit.style/fillopacity.md)
  The opacity of the fill color.
- [fillRule](mapkit.style/fillrule.md)
  A rule for determining whether a point is inside or outside a polygon.
### Styling lines
- [lineCap](mapkit.style/linecap.md)
  The style to use when drawing line endings.
- [lineDash](mapkit.style/linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](mapkit.style/linedashoffset.md)
  The number of CSS pixels to use as an offset when drawing a line’s dash pattern.
- [lineJoin](mapkit.style/linejoin.md)
  The corner style to apply when joining line segments.
- [lineWidth](mapkit.style/linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [lineGradient](mapkit.style/linegradient.md)
  The gradient to apply along the line.
- [mapkit.LineGradient](mapkit.linegradient.md)
  A line that displays with a gradient along the length of the line.
### Styling strokes
- [strokeColor](mapkit.style/strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](mapkit.style/strokeopacity.md)
  The opacity of the stroke color.
- [strokeStart](mapkit.style/strokestart.md)
  The unit distance along the line where a stroke begins.
- [strokeEnd](mapkit.style/strokeend.md)
  The unit distance along the line where a stroke ends.

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
- [mapkit.Overlay](mapkit.overlay.md)
  An abstract base object that defines the methods and attributes for map overlays.
- [mapkit.CircleOverlay](mapkit.circleoverlay.md)
  A circular overlay with a configurable radius that centers on a specific geographic coordinate.
- [mapkit.PolylineOverlay](mapkit.polylineoverlay.md)
  An overlay of connected line segments that don’t form a closed shape.
- [mapkit.PolygonOverlay](mapkit.polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [mapkit.TileOverlay](mapkit.tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.style)*