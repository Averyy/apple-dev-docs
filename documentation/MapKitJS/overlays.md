# Overlays

**Framework**: MapKit JS

Create overlays to highlight geographic regions or paths.

#### Overview

You can enhance your maps by adding  shapes that appear on top of the map. There are three overlay shapes:

- Circle ([`CircleOverlay`](circleoverlay.md))
- Polyline ([`PolylineOverlay`](polylineoverlay.md))
- Polygon ([`PolygonOverlay`](polygonoverlay.md))

These three objects can satisfy a wide variety of purposes, such as outlining routes, highlighting map areas, enabling users to make selections, and more.

To display an overlay, you provide geometry data that determines the overlay’s shape, and a style that determines its visual representation. For example, a circle’s center and radius define its geometry. The coordinates of a polygon’s vertices define its shape. The style specifies how to draw the overlay, including its fill color, outline color, and opacity.

Overlays are dynamic. The system automatically redraws them when their underlying geometry or style data changes. For instance, a circle’s radius can grow, or a polygon’s fill color can update dynamically. This makes overlays a powerful visualization tool. For example, circle overlays can show the spread of an infectious disease over a span of time.

Overlays belong to their own layer that lies above map tiles and below annotations. The order that you add overlays to a map is significant. When multiple overlays overlap, overlays that you add later are higher in the z-order (that is, closer to the foreground).

## Topics

### Overlays
- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
- [class Overlay](overlay.md)
  An abstract base object that defines the methods and properties for map overlays.
- [class Style](style.md)
  A set of observable style properties for overlays, including the color and opacity of strokes and fills, and line styles.
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

## See Also

- [Annotations](annotations.md)
  Create annotations to add indicators and additional details for specific locations on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/overlays)*