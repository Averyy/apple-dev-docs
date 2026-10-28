# topOverlayAtPoint(point)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Returns the topmost overlay at a given point on the webpage.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
topOverlayAtPoint(point: DOMPoint): Overlay | null;
```

## Return Value

Returns the topmost overlay or `null`.

## Discussion

If there are multiple overlays at a point, MapKit JS returns the overlay closest to the foreground. If the user selects an overlay, MapKit JS draws user-selected overlays on top of all other overlays. So when a user selects an overlay, MapKit JS returns that overlay.

The following code example identifies the topmost overlay during a mouse move event:

```javascript
document.querySelector(".mk-map-view").addEventListener("mousemove", function(event) {
    const targetOverlay = map.topOverlayAtPoint(new DOMPoint(event.pageX, event.pageY));
    // Add special styling to the overlay to indicate its hover state or whatever you want.
    // ...
});

```

## Parameters

- `point`: A point in the page’s coordinate system, such as `new DOMPoint(event.pageX, event.pageY)` when handling a mouse event.

## See Also

### Adding and removing overlays
- [overlays](./overlays.md)
  An array of all of the map’s overlays.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/topoverlayatpoint)*