# selectedOverlay

**Framework**: MapKit JS  
**Kind**: property

The selected overlay on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Overlay selectedOverlay;
```

#### Discussion

To deselect any selected overlay, set this attribute to `null`.

To select an overlay that’s already part of the map, set this attribute to the desired overlay.

When MapKit JS removes the selected overlay from the map (as an effect of [`removeOverlay`](mapkit.map/removeoverlay.md), [`removeOverlays`](mapkit.map/removeoverlays.md), or setting a new set of overlays with the [`overlays`](mapkit.map/overlays.md) property), MapKit JS deselects the overlay before removing it.

## See Also

- [overlays](mapkit.map/overlays.md)
  An array of all of the map’s overlays.
- [overlaysAtPoint](mapkit.map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay](mapkit.map/addoverlay.md)
  Adds an overlay to the map.
- [addOverlays](mapkit.map/addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay](mapkit.map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays](mapkit.map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint](mapkit.map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/selectedoverlay)*