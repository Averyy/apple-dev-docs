# init(points:count:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a geodesic polyline using the specified map points.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
convenience init(points: UnsafePointer<MKMapPoint>, count: Int)
```

#### Return Value

A new geodesic polyline object.

## Parameters

- `points`: A pointer to the array of map points that define the path.
- `count`: The number of items in the   array.

## See Also

- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int)](mkgeodesicpolyline/init(coordinates:count:).md)
  Creates and returns a geodesic polyline using the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/init(points:count:))*