# convertPointOnPageToCoordinate(point)

**Framework**: MapKit JS  
**Kind**: method

Converts a point in page coordinates to the corresponding map coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
convertPointOnPageToCoordinate(point: DOMPoint): Coordinate;
```

#### Return Value

A [`Coordinate`](coordinate.md) in the map at the provided `DOMPoint` of the page.

## Parameters

- `point`: A point in the page’s coordinate system, such as   when handling a mouse event.

## See Also

- [convertCoordinateToPointOnPage(coordinate)](map/convertcoordinatetopointonpage.md)
  Converts a coordinate on the map to a point in the page’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/convertpointonpagetocoordinate)*