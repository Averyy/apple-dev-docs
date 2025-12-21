# selectedOverlay

**Framework**: MapKit JS  
**Kind**: property

The selected overlay on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get selectedOverlay(): Overlay | null;
set selectedOverlay(overlay: Overlay | null);
```

#### Discussion

To deselect any selected overlay, set this property to `null`.

To select an overlay that’s already part of the map, set this property to the desired overlay.

When MapKit JS removes the selected overlay from the map (as an effect of [`removeOverlay(overlay)`](map/removeoverlay.md), [`removeOverlays(overlays)`](map/removeoverlays.md), or setting a new set of overlays with the [`overlays`](map/overlays.md) property), MapKit JS deselects the overlay before removing it.

## See Also

- [overlays](map/overlays.md)
  An array of all of the map’s overlays.
- [overlaysAtPoint(point)](map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay(overlay)](map/addoverlay.md)
  Adds an overlay to the map.
- [addOverlays(overlays)](map/addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay(overlay)](map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays(overlays)](map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint(point)](map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/selectedoverlay)*