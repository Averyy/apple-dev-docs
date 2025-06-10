# mapkit.PolygonOverlay

**Framework**: MapKit JS  
**Kind**: class

An overlay consisting of one or more points that forms a closed shape.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.PolygonOverlay
```

#### Overview

A  is a shape that consists of points connected end-to-end. Unlike polylines, polygons are closed shapes with an inside and an outside. The first and last points connect to each other to form a closed shape.

The [`mapkit.PolygonOverlay`](mapkit.polygonoverlay/mapkit.polygonoverlay.md) initializer doesn’t limit you to whole polygons. You can combine multiple polygons to form noncontiguous shapes or shapes with regions cut out. For example, to show the boundaries of South Africa, an overlay carves out Lesotho, an enclave within South Africa. To do this, you use points to describe Lesotho as a polygon that MapKit JS subtracts from the outer polygon.

You can choose whether a point falls inside or outside the [`mapkit.PolygonOverlay`](mapkit.polygonoverlay/mapkit.polygonoverlay.md) by setting `style.fillRule` to `nonzero` or `evenodd`.

The longitude of all points in a polygon overlay needs to be within a 360-degree range. Depending on how you specify the longitude of the points, drawing a triangle between Tokyo, Los Angeles, and Sydney using a polygon overlay may take a different route. Specifying a longitude of -118º for Los Angeles, 140º for Tokyo, and 151º for Sydney results in a very wide triangle spanning 258º. Specifying a longitude of 242º (that is, -118 + 360) for Los Angeles, 140º for Tokyo, and 151º for Sydney results in a narrower triangle spanning 98º. MapKit JS may not render the polyline correctly if the range of longitudes is larger than 360º.

All [`style`](stylesoverlayoptions/style.md) properties apply to polygon overlays except `lineCap`, which MapKit JS ignores. [`mapkit.PolygonOverlay`](mapkit.polygonoverlay/mapkit.polygonoverlay.md) doesn’t implement methods of its own. For more information, see the base object, [`mapkit.Overlay`](mapkit.overlay.md). The following example uses a rectangle overlay to show the boundary lines for the state of Colorado:

```javascript
const points = [ [41, -109.05], [41, -102.05], [37, -102.05], [37, -109.05] ];

// Map the raw coordinate points to MapKit JS Coordinate objects:
points = points.map(function(point) {
    return new mapkit.Coordinate(point[0], point[1]);
});
const style = new mapkit.Style({
    strokeColor: "#F00",
    strokeOpacity: .2,
    lineWidth: 2,
    lineJoin: "round",
    lineDash: [2, 2, 6, 2, 6, 2]
});

const rectangle = new mapkit.PolygonOverlay(points, { style: style });
map.addOverlay(rectangle);
```

## Topics

### Creating a polygon overlay
- [mapkit.PolygonOverlay](mapkit.polygonoverlay/mapkit.polygonoverlay.md)
  Creates a polygon overlay with an array of points and style options.
- [StylesOverlayOptions](stylesoverlayoptions.md)
  An observable set of style attributes for an overlay.
### Defining the polygon
- [points](mapkit.polygonoverlay/points.md)
  One or more arrays of coordinates that define the polygon overlay shape.

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
- [mapkit.CircleOverlay](mapkit.circleoverlay.md)
  A circular overlay with a configurable radius that centers on a specific geographic coordinate.
- [mapkit.PolylineOverlay](mapkit.polylineoverlay.md)
  An overlay of connected line segments that don’t form a closed shape.
- [OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [mapkit.TileOverlay](mapkit.tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.polygonoverlay)*