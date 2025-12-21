# Overlay

**Framework**: MapKit JS  
**Kind**: class

An abstract base object that defines the methods and properties for map overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
abstract class Overlay extends MapKitEventTarget
```

## Mentions

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

#### Overview

Overlays inherit from an abstract base object, [`Overlay`](overlay.md), and share some common properties with [`Annotation`](annotation.md) that allow you to control the visibility and interaction with the map in the same way. This object is abstract and you can’t instantiate it.

## Topics

### Setting overlay options
- [data](overlay/data.md)
  Custom data to associate with the overlay.
- [visible](overlay/visible.md)
  A Boolean value that determines whether an overlay is visible.
- [enabled](overlay/enabled.md)
  A Boolean value that determines whether the overlay responds to user interaction.
- [selected](overlay/selected.md)
  A Boolean value that indicates whether the user selects the overlay.
- [style](overlay/style.md)
  Style properties to apply to the overlay.
- [map](overlay/map.md)
  The map you add the overlay to.

## Relationships

### Inherits From
- [MapKitEventTarget](mapkiteventtarget.md)
### Inherited By
- [CircleOverlay](circleoverlay.md)
- [PolygonOverlay](polygonoverlay.md)
- [PolylineOverlay](polylineoverlay.md)

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/overlay)*