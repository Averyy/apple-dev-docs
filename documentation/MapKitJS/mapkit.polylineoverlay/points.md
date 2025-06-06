# points

**Framework**: MapKit JS  
**Kind**: property

An array of coordinate points that define the polyline overlay’s shape.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Coordinate[] points;
```

#### Discussion

MapKit JS defines the points in the polyline as an array of [`mapkit.Coordinate`](mapkit.coordinate.md) points. A copy of the overlay’s array returns on read, so changing the array’s elements has no effect on the overlay. To change the overlay’s points, assign a new array. MapKit JS doesn’t draw a polyline with fewer than two points on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.polylineoverlay/points)*