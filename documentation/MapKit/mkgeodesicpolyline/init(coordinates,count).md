# init(coordinates:count:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a geodesic polyline using the specified coordinates.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count: Int)
```

```objc
+ (instancetype) polylineWithCoordinates:(const CLLocationCoordinate2D *) coords count:(NSUInteger) count;
```

#### Return Value

A new geodesic polyline object.

## Parameters

- `coords`: A pointer to the array of coordinates that define the path.
- `count`: The number of items in the `coords` array.

## See Also

### Creating a geodesic polyline overlay
- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int)](./init%28points,count%29.md)
  Creates and returns a geodesic polyline using the specified map points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/init(coordinates:count:))*