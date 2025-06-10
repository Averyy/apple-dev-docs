# init(coordinates:count:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a polygon object from the specified set of coordinates.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count: Int)
```

#### Return Value

A new polygon object.

## Parameters

- `coords`: The array of coordinates defining the shape. The new object copies the data in this array.
- `count`: The number of items in the   array.

## See Also

- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int)](mkpolygon/init(points:count:).md)
  Creates and returns a polygon object from the specified set of map points.
- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int, interiorPolygons: [MKPolygon]?)](mkpolygon/init(points:count:interiorpolygons:).md)
  Creates and returns a polygon object from the specified set of map points and interior polygons.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons: [MKPolygon]?)](mkpolygon/init(coordinates:count:interiorpolygons:).md)
  Creates and returns a polygon object from the specified set of coordinates and interior polygons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygon/init(coordinates:count:))*