# overlays

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An array of all of the map’s overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get overlays(): Overlay[];
set overlays(overlays: Overlay[]);
```

## Discussion

You can set this property to a new (possibly empty) array of overlays to update or delete all the overlays on the map.

## See Also

### Adding and removing overlays
- [selectedOverlay](./selectedoverlay.md)
  The selected overlay on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/overlays)*