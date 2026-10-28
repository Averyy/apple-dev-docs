# init(points:count:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a polygon object from the specified set of map points.

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
convenience init(points: UnsafePointer<MKMapPoint>, count: Int)
```

```objc
+ (instancetype) polygonWithPoints:(const MKMapPoint *) points count:(NSUInteger) count;
```

## Return Value

A new polygon object.

## Parameters

- `points`: The array of map points defining the shape. The new object copy the data in this array.
- `count`: The number of items in the `points` array.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Creating a polygon overlay
- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int, interiorPolygons: [MKPolygon]?)](./init%28points,count,interiorpolygons%29.md)
  Creates and returns a polygon object from the specified set of map points and interior polygons.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int)](./init%28coordinates,count%29.md)
  Creates and returns a polygon object from the specified set of coordinates.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons: [MKPolygon]?)](./init%28coordinates,count,interiorpolygons%29.md)
  Creates and returns a polygon object from the specified set of coordinates and interior polygons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygon/init(points:count:))*