# overlays

**Framework**: MapKit JS  
**Kind**: property

An array of all of the map’s overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get overlays(): Overlay[];
set overlays(overlays: Overlay[]);
```

#### Discussion

You can set this property to a new (possibly empty) array of overlays to update or delete all the overlays on the map.

## See Also

- [selectedOverlay](map/selectedoverlay.md)
  The selected overlay on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/overlays)*