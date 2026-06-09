# TileOverlay

**Framework**: MapKit JS  
**Kind**: class

An overlay that covers an area of the map with bitmapped tiles.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class TileOverlay extends EventTarget
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Overview

You use tile overlay objects to represent your own tile-based content and to coordinate the display of that content on a map. Your tiles can supplement the underlying map content or replace it completely. You can use a single tile overlay object to represent all of the tiles at one or more zoom levels of the map.

## Topics

### Creating a tile overlay
- [new TileOverlay(imageForTile, options)](tileoverlay/tileoverlayconstructor.md)
  Creates a tile overlay with a URL template or image callback and style options.
- [interface TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.
- [type TileOverlayImageCallback](tileoverlayimagecallback.md)
  A callback function that provides tile images for a tile overlay.
### Events
- [class TileOverlayErrorEvent](tileoverlayerrorevent.md)
  An event object that notifies the developer of an error that occurred while loading tiles.
### Customizing the tile overlay
- [imageForTile](tileoverlay/imagefortile.md)
  A string, or callback function, that provides the requested tile.
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
### Deprecated
- [urlTemplate](tileoverlay/urltemplate.md)
  A string, or callback function, that provides the requested tile.

## Relationships

### Inherits From
- [EventTarget](doc://com.apple.mapkitjs/__unknown__/EventTarget)

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