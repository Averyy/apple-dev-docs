# overlaysAtPoint(point)

**Framework**: MapKit JS  
**Kind**: method

Returns an array of overlays at a given point on the webpage.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
overlaysAtPoint(point: DOMPoint): Overlay[];
```

#### Return Value

Returns an array of overlays. If there are no overlays at the point, the array is empty.

#### Discussion

If the point is above an overlay fill or stroke, MapKit JS returns the overlay. MapKit JS returns overlays in the order they display, with the first overlay in the array closest to the background, and the last overlay closest to the foreground.

Similar to overlay selection events, this method considers the overlay’s style at the point.

> **Note**:  The point needs to be above a non-`null` overlay fill or stroke to return the overlay.

For example, the following cases don’t return an overlay:

- The point is on an overlay’s fill, but the fill color is `null`.
- The point is on an overlay’s stroke, but the stroke color is `null`.
- The point is on an overlay’s stroke, but the line width is `0`.

Opacity isn’t a factor and can have any value. For example, if the point is on an overlay that has an opacity of `0`, MapKit JS returns that overlay.

## Parameters

- `point`: A point in the page’s coordinate system, such as  , when handling a mouse event.

## See Also

- [overlays](map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](map/selectedoverlay.md)
  The selected overlay on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/overlaysatpoint)*