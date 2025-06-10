# init(coordinates:count:)

**Framework**: MapKit  
**Kind**: init

Creates a polyline object from the specified set of coordinates.

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

A new polyline object.

## Parameters

- `coords`: The array of coordinates defining the shape. The initializer copies the data in this array to the new object.
- `count`: The number of items in the   array.

## See Also

- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int)](mkpolyline/init(points:count:).md)
  Creates a polyline object from the specified set of map points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolyline/init(coordinates:count:))*