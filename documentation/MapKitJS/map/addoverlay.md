# addOverlay(overlay)

**Framework**: MapKit JS  
**Kind**: method

Adds an overlay to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
addOverlay(overlay: Overlay): Overlay | undefined;
```

#### Return Value

Returns the overlay.

#### Discussion

MapKit JS adds the overlay to the end of the map’s [`overlays`](map/overlays.md) array.

## Parameters

- `overlay`: The overlay to add.

## See Also

- [overlays](map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](map/selectedoverlay.md)
  The selected overlay on the map.
- [overlaysAtPoint(point)](map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlays(overlays)](map/addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay(overlay)](map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays(overlays)](map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint(point)](map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/addoverlay)*