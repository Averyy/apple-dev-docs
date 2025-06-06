# mapkit.Overlay

**Framework**: MapKit JS  
**Kind**: class

An abstract base object that defines the methods and attributes for map overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Overlay
```

## Mentions

- [Handling map events](handling-map-events.md)
- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

#### Overview

Overlays inherit from an abstract base object, [`mapkit.Overlay`](mapkit.overlay.md), and share some common properties with [`mapkit.Annotation`](mapkit.annotation.md) that allow you to control the visibility and interaction with the map in the same way. This object is abstract and you can’t instantiate it.

## Topics

### Registering event listeners
- [addEventListener](mapkit.overlay/addeventlistener.md)
  Starts listening for the specified type of event.
- [removeEventListener](mapkit.overlay/removeeventlistener.md)
  Stops listening for the specified type of event.
### Setting overlay options
- [data](mapkit.overlay/data.md)
  Custom data to associate with the overlay.
- [visible](mapkit.overlay/visible.md)
  A Boolean value that determines whether an overlay is visible.
- [enabled](mapkit.overlay/enabled.md)
  A Boolean value that determines whether the overlay responds to user interaction.
- [selected](mapkit.overlay/selected.md)
  A Boolean value that indicates whether the user selects the overlay.
- [style](mapkit.overlay/style.md)
  Style properties to apply to the overlay.
- [map](mapkit.overlay/map.md)
  The map you add the overlay to.

## Relationships

### Inherits From
- [mapkit.CircleOverlay](mapkit.circleoverlay.md)
- [mapkit.PolygonOverlay](mapkit.polygonoverlay.md)
- [mapkit.PolylineOverlay](mapkit.polylineoverlay.md)

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
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
- [mapkit.TileOverlay](mapkit.tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.overlay)*