# OverlayOptions

**Framework**: MapKit JS  
**Kind**: struct

A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary OverlayOptions {
	Object data;
	boolean visible;
	boolean enabled;
	boolean selected;
};
```

#### Overview

Use [`OverlayOptions`](overlayoptions.md) to set the initial state of your overlay and provide the data MapKit JS uses to render it.

## Topics

### Overlay options
- [data](overlayoptions/data.md)
  Custom data to associate with the overlay.
- [enabled](overlayoptions/enabled.md)
  A Boolean value that determines whether the overlay responds to user interaction.
- [selected](overlayoptions/selected.md)
  A Boolean value that indicates whether the overlay is in a selected state.
- [visible](overlayoptions/visible.md)
  A Boolean value that determines if an overlay is visible.

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
- [mapkit.TileOverlay](mapkit.tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/overlayoptions)*