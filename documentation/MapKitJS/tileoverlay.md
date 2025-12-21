# TileOverlay

**Framework**: MapKit JS  
**Kind**: class

An overlay that covers an area of the map with bitmapped tiles.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class TileOverlay extends MapKitEventTarget
```

#### Overview

You use tile overlay objects to represent your own tile-based content and to coordinate the display of that content on a map. Your tiles can supplement the underlying map content or replace it completely. You can use a single tile overlay object to represent all of the tiles at one or more zoom levels of the map.

## Topics

### Creating a tile overlay
- [new TileOverlay(urlTemplate, options)](tileoverlay/tileoverlayconstructor.md)
  Creates a tile overlay with a URL template and style options.
- [interface TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.
### Events
- [class TileOverlayErrorEvent](tileoverlayerrorevent.md)
  An event object that notifies the developer of an error that occurred while loading tiles.
### Customizing the tile overlay
- [urlTemplate](tileoverlay/urltemplate.md)
  A string, or callback function that returns a string, with a URL that provides the requested tile.
- [data](tileoverlay/data.md)
  A dictionary of custom properties to use with the URL template.
- [reload()](tileoverlay/reload.md)
  Reloads the tile overlay for the displayed map region with the latest data values.
### Setting overlay appearance
- [opacity](tileoverlay/opacity.md)
  A number that indicates a tile’s opacity.
- [maximumZ](tileoverlay/maximumz.md)
  The maximum zoom level for a tile overlay.
- [minimumZ](tileoverlay/minimumz.md)
  The minimum zoom level for a tile overlay.

## Relationships

### Inherits From
- [MapKitEventTarget](mapkiteventtarget.md)

## See Also

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
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay)*