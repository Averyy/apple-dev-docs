# PolylineOverlay

**Framework**: MapKit JS  
**Kind**: class

An overlay of connected line segments that don’t form a closed shape.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class PolylineOverlay extends Overlay
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

A  is a shape that consists of connected line segments that you define with a set of points. The first and last points don’t connect to each other.

The longitude of all points should be within a 360-degree range. Depending on how you specify the longitude, a line between Tokyo and Los Angeles that you create with a [`PolylineOverlay`](polylineoverlay.md) may take a different route. Specifying a longitude of -118º for Los Angeles and 140º for Tokyo results in a very long line spanning 258º. Specifying a longitude of 242º (that’s, -118 + 360) for Los Angeles and 140º for Tokyo results in a shorter line spanning 98º. MapKit JS may not render the polyline correctly if the range of longitudes is larger than 360º.

All [`style`](overlayoptions/style.md) properties apply to polyline overlays except `fillColor`, `fillOpacity,` and `fillRule`. MapKit JS ignores properties that don’t apply. [`PolylineOverlay`](polylineoverlay.md) doesn’t implement methods of its own. For more information, see the base object, [`Overlay`](overlay.md).

The following example shows a polyline object for a map.

```javascript
const points = [ [10, 1], [5, 6], [1, 1] ];
const coords = points.map(function(point) {
    return new mapkit.Coordinate(point[0], point[1]);
});

const style = new mapkit.Style({
    lineWidth: 2,
    lineJoin: "round",
    lineDash: [8, 4],
    strokeColor: "#F0F"
});

const polyline = new mapkit.PolylineOverlay(coords, { style: style });
map.addOverlay(polyline);
```

## Topics

### Creating a polyline overlay
- [new PolylineOverlay(points, options)](polylineoverlay/polylineoverlayconstructor.md)
  Creates a polyline overlay with coordinate points and style options.
- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
### Defining the polyline
- [points](polylineoverlay/points.md)
  An array of coordinate points that define the polyline overlay’s shape.

## Relationships

### Inherits From
- [Overlay](overlay.md)

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
- [class Overlay](overlay.md)
  An abstract base object that defines the methods and properties for map overlays.
- [class Style](style.md)
  A set of observable style properties for overlays, including the color and opacity of strokes and fills, and line styles.
- [class CircleOverlay](circleoverlay.md)
  A circular overlay with a configurable radius that centers on a specific geographic coordinate.
- [class PolygonOverlay](polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [class TileOverlay](tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/polylineoverlay)*