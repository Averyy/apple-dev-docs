# LineGradient

**Framework**: MapKit JS  
**Kind**: class

A line that displays with a gradient along the length of the line.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
class LineGradient
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

Use [`LineGradient`](linegradient.md) with a [`PolylineOverlay`](polylineoverlay.md) to show a gradient along a route or path. You can also use it to provide additional information about locations along the path, for example, the running pace along a route.

## Topics

### Creating a Line Gradient
- [new LineGradient(colorStops)](linegradient/linegradientconstructor.md)
  Creates a style that renders a gradient along the length of a line.
- [addColorStop(offset, color)](linegradient/addcolorstop.md)
  Adds a color transition point to the gradient.
- [addColorStopAtIndex(index, color)](linegradient/addcolorstopatindex.md)
  Adds a color transition at the index point in the list of points within a polyline.
### Instance Methods
- [toString()](linegradient/tostring.md)
  Returns a string representation of the line gradient object.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/linegradient)*