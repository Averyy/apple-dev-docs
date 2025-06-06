# mapkit.CircleOverlay

**Framework**: MapKit JS  
**Kind**: class

A circular overlay with a configurable radius that centers on a specific geographic coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.CircleOverlay
```

#### Overview

The circle overlay provides a built-in object for creating circles. MapKit JS defines [`mapkit.CircleOverlay`](mapkit.circleoverlay/mapkit.circleoverlay.md) by a coordinate and a radius (in meters). All [`style`](stylesoverlayoptions/style.md) properties apply to circle overlays except `lineCap`, `lineJoin`, and `fillRule`. MapKit JS ignores properties that don’t apply.

[`mapkit.CircleOverlay`](mapkit.circleoverlay/mapkit.circleoverlay.md) doesn’t implement methods of its own. For more information, see the base object, [`mapkit.Overlay`](mapkit.overlay.md).

The following example uses circle overlays to show the relative population sizes of three cities in the San Francisco Bay Area:

```javascript
var stats = [
    { name: "San Francisco", coordinate: [37.783333, -122.416667], population: 852469 },
    { name: "Oakland", coordinate: [37.804444, -122.270833], population: 390724 },
    { name: "San Jose", coordinate: [37.333333, -121.9], population: 1000536 },
];

var style = new mapkit.Style({
    lineWidth: 2,         // 2 CSS pixels.
    strokeColor: "#999",
    fillColor: "#FFF"
});

var circles = stats.map(function(stat) {
    var coordinate = new mapkit.Coordinate(stat.coordinate[0], stat.coordinate[1]),
        radius = stat.population / 85, // The radius is in meters.
        circle = new mapkit.CircleOverlay(coordinate, radius);
    circle.data = { population: stat.population };
    circle.style = style;
    return circle;
});

map.addOverlays(circles);
```

## Topics

### Creating a circle overlay
- [mapkit.CircleOverlay](mapkit.circleoverlay/mapkit.circleoverlay.md)
  Creates a circle overlay with a center coordinate, radius, and style options.
- [StylesOverlayOptions](stylesoverlayoptions.md)
  An observable set of style attributes for an overlay.
### Defining the circle
- [coordinate](mapkit.circleoverlay/coordinate.md)
  The coordinate of the circle overlay’s center.
- [radius](mapkit.circleoverlay/radius.md)
  The circle overlay’s radius, in meters.

## Relationships

### Inherited By
- [mapkit.Overlay](mapkit.overlay.md)

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
- [mapkit.Overlay](mapkit.overlay.md)
  An abstract base object that defines the methods and attributes for map overlays.
- [mapkit.Style](mapkit.style.md)
  A set of observable attributes for overlays, including the color and opacity of strokes and fills, and line styles.
- [mapkit.PolylineOverlay](mapkit.polylineoverlay.md)
  An overlay of connected line segments that don’t form a closed shape.
- [mapkit.PolygonOverlay](mapkit.polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [mapkit.TileOverlay](mapkit.tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.circleoverlay)*