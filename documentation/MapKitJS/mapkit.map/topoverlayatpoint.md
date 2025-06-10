# topOverlayAtPoint

**Framework**: MapKit JS  
**Kind**: method

Returns the topmost overlay at a given point on the webpage.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.Overlay topOverlayAtPoint(
	DOMPoint point
);
```

#### Return Value

Returns the topmost overlay or `null`.

#### Discussion

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

- `point`: A point in the page’s coordinate system, such as   when handling a mouse event.

## See Also

- [overlays](mapkit.map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](mapkit.map/selectedoverlay.md)
  The selected overlay on the map.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/topoverlayatpoint)*