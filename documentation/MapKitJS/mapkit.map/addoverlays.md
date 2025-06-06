# addOverlays

**Framework**: MapKit JS  
**Kind**: method

Adds multiple overlays to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.Overlay[] addOverlays(
	mapkit.Overlay[] overlays
);
```

#### Return Value

Returns the array of overlays.

#### Discussion

MapKit JS adds the overlays to the end of the map’s [`overlays`](mapkit.map/overlays.md) array.

## Parameters

- `overlays`: An array of overlays to add.

## See Also

- [overlays](mapkit.map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](mapkit.map/selectedoverlay.md)
  The selected overlay on the map.
- [overlaysAtPoint](mapkit.map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay](mapkit.map/addoverlay.md)
  Adds an overlay to the map.
- [removeOverlay](mapkit.map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays](mapkit.map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint](mapkit.map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/addoverlays)*