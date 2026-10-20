# addOverlay(overlay)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Adds an overlay to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
addOverlay(overlay: Overlay): Overlay | null;
```

#### Return Value

Returns the overlay.

#### Discussion

MapKit JS adds the overlay to the end of the map’s [`overlays`](./overlays.md) array.

## Parameters

- `overlay`: The overlay to add.

## See Also

### Adding and removing overlays
- [overlays](./overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](./selectedoverlay.md)
  The selected overlay on the map.
- [overlaysAtPoint(point)](./overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlays(overlays)](./addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay(overlay)](./removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays(overlays)](./removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint(point)](./topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/addoverlay)*