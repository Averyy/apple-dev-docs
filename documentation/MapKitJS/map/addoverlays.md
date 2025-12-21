# addOverlays(overlays)

**Framework**: MapKit JS  
**Kind**: method

Adds multiple overlays to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
addOverlays(overlays: Overlay[]): Overlay[];
```

#### Return Value

Returns the array of overlays.

#### Discussion

MapKit JS adds the overlays to the end of the map’s [`overlays`](map/overlays.md) array.

## Parameters

- `overlays`: An array of overlays to add.

## See Also

- [overlays](map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](map/selectedoverlay.md)
  The selected overlay on the map.
- [overlaysAtPoint(point)](map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay(overlay)](map/addoverlay.md)
  Adds an overlay to the map.
- [removeOverlay(overlay)](map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays(overlays)](map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint(point)](map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/addoverlays)*