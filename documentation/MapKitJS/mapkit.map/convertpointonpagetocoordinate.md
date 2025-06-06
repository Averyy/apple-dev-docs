# convertPointOnPageToCoordinate

**Framework**: MapKit JS  
**Kind**: method

Converts a point in page coordinates to the corresponding map coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.Coordinate convertPointOnPageToCoordinate(
	DOMPoint point
);
```

## Mentions

- [Handling map events](handling-map-events.md)

#### Return Value

A [`mapkit.Coordinate`](mapkit.coordinate.md) in the map at the provided point ([`DOMPoint`](https://developer.apple.com/documentation/webkitjs/dompoint)) of the page.

## Parameters

- `point`: A point in the page’s coordinate system, such as   when handling a mouse event.

## See Also

- [convertCoordinateToPointOnPage](mapkit.map/convertcoordinatetopointonpage.md)
  Converts a coordinate on the map to a point in the page’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/convertpointonpagetocoordinate)*