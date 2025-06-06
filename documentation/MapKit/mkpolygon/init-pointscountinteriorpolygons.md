# init(points:count:interiorPolygons:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a polygon object from the specified set of map points and interior polygons.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
convenience init(points: UnsafePointer<MKMapPoint>, count: Int, interiorPolygons: [MKPolygon]?)
```

#### Return Value

A new polygon object.

## Parameters

- `points`: The array of map points defining the shape. The new object copy the data in this array.
- `count`: The number of items in the   array.
- `interiorPolygons`: An array of   objects that define one or more cutout regions for the receiver’s polygon.

## See Also

- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int)](mkpolygon/init(points:count:).md)
  Creates and returns a polygon object from the specified set of map points.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int)](mkpolygon/init(coordinates:count:).md)
  Creates and returns a polygon object from the specified set of coordinates.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons: [MKPolygon]?)](mkpolygon/init(coordinates:count:interiorpolygons:).md)
  Creates and returns a polygon object from the specified set of coordinates and interior polygons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygon/init(points:count:interiorpolygons:))*