# MapKit overlays

**Framework**: MapKit

Create overlays to highlight geographic regions or paths.

## Topics

### Samples
- [Displaying overlays on a map](displaying-overlays-on-a-map.md)
  Add regions of layered content to a map view.
- [Displaying an updating path of a user’s location history](displaying-an-updating-path-of-a-user-s-location-history.md)
  Continually update a MapKit overlay displaying the path a user travels.
### Circular overlays
- [class MKCircle](mkcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [class MKCircleRenderer](mkcirclerenderer.md)
  The visual representation of a circular overlay.
### Custom shape overlays
- [class MKPolygon](mkpolygon.md)
  A closed polygon overlay.
- [class MKPolygonRenderer](mkpolygonrenderer.md)
  The visual representation of a single polygon overlay.
- [class MKMultiPolygon](mkmultipolygon.md)
  A collection of multiple closed polygon overlays.
- [class MKMultiPolygonRenderer](mkmultipolygonrenderer.md)
  The visual representation of multiple polygon overlays.
- [class MKOverlayPathRenderer](mkoverlaypathrenderer.md)
  The visual representation of a path-based overlay.
### Multiple segment lines
- [class MKPolyline](mkpolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [class MKGeodesicPolyline](mkgeodesicpolyline.md)
  An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [class MKMultiPolyline](mkmultipolyline.md)
  A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [class MKPolylineRenderer](mkpolylinerenderer.md)
  A visual representation of any polyline overlay object.
- [class MKMultiPolylineRenderer](mkmultipolylinerenderer.md)
  A visual representation of multiple polyline overlay objects.
- [class MKGradientPolylineRenderer](mkgradientpolylinerenderer.md)
  A visual representation of any polyline overlay object with a gradient.
### Tiled image overlays
- [class MKTileOverlay](mktileoverlay.md)
  An overlay that covers an area of the map with tiles of bitmap images.
- [class MKTileOverlayRenderer](mktileoverlayrenderer.md)
  The renderer for a tile overlay that handles the drawing of bitmap images on the map surface.
### Shared behavior
- [protocol MKOverlay](mkoverlay.md)
  An interface for associating content with a specific map region.
- [class MKOverlayRenderer](mkoverlayrenderer.md)
  The shared infrastructure for drawing overlays on the map surface.
- [class MKShape](mkshape.md)
  An abstract class that defines the basic properties for all shape-based overlay objects.
- [class MKMultiPoint](mkmultipoint.md)
  An abstract class that defines the common behavior that open and closed polygon overlays share.
- [class MKPlacemark](mkplacemark.md)
  A user-friendly description of a location on the map.

## See Also

- [MapKit annotations](mapkit-annotations.md)
  Create annotations to add indicators and additional details for specific locations on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapkit-overlays)*