# init(points:count:)

**Framework**: MapKit  
**Kind**: init

Creates a polyline object from the specified set of map points.

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

#### Return Value

A new polyline object.

## Parameters

- `points`: The array of map points defining the shape. The initializer copies the data in this array to the new object.
- `count`: The number of items in the   array.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int)](mkpolyline/init(coordinates:count:).md)
  Creates a polyline object from the specified set of coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolyline/init(points:count:))*