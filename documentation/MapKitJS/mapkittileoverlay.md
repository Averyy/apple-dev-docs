# mapkit.TileOverlay

**Framework**: MapKit JS  
**Kind**: class

An overlay that covers an area of the map with bitmapped tiles.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.TileOverlay
```

#### Overview

You use tile overlay objects to represent your own tile-based content and to coordinate the display of that content on a map. Your tiles can supplement the underlying map content or replace it completely. You can use a single tile overlay object to represent all of the tiles at one or more zoom levels of the map.

## Topics

### Creating a tile overlay
- [mapkit.TileOverlay](mapkit.tileoverlay/mapkit.tileoverlay.md)
  Creates a tile overlay with a URL template and style options.
- [TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.
### Registering event listeners
- [addEventListener](mapkit.tileoverlay/addeventlistener.md)
  Listens for events of the specified type.
- [removeEventListener](mapkit.tileoverlay/removeeventlistener.md)
  Stops listening for events of the specified type.
### Customizing the tile overlay
- [urlTemplate](mapkit.tileoverlay/urltemplate.md)
  A string, or callback function that returns a string, with a URL that provides the requested tile.
- [data](mapkit.tileoverlay/data.md)
  A dictionary of custom properties to use with the URL template.
- [reload](mapkit.tileoverlay/reload.md)
  Reloads the tile overlay for the displayed map region with the latest data values.
### Setting overlay appearance
- [opacity](mapkit.tileoverlay/opacity.md)
  A number that indicates a tile’s opacity.
- [maximumZ](mapkit.tileoverlay/maximumz.md)
  The maximum zoom level for a tile overlay.
- [minimumZ](mapkit.tileoverlay/minimumz.md)
  The minimum zoom level for a tile overlay.

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
- [mapkit.PolygonOverlay](mapkit.polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.tileoverlay)*