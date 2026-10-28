# selectedOverlay

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The selected overlay on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get selectedOverlay(): Overlay | null;
set selectedOverlay(overlay: Overlay | null);
```

## Discussion

To deselect any selected overlay, set this property to `null`.

To select an overlay that’s already part of the map, set this property to the desired overlay.

When MapKit JS removes the selected overlay from the map (as an effect of [`removeOverlay()`](./removeoverlay.md), [`removeOverlays()`](./removeoverlays.md), or setting a new set of overlays with the [`overlays`](./overlays.md) property), MapKit JS deselects the overlay before removing it.

## See Also

### Adding and removing overlays
- [overlays](./overlays.md)
  An array of all of the map’s overlays.
- [overlaysAtPoint(point)](./overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay(overlay)](./addoverlay.md)
  Adds an overlay to the map.
- [addOverlays(overlays)](./addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay(overlay)](./removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays(overlays)](./removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint(point)](./topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/selectedoverlay)*