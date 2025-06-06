# init(_:)

**Framework**: MapKit  
**Kind**: init

Returns the region that corresponds to the specified map rectangle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(_ rect: MKMapRect)
```

#### Return Value

The region structure specifying the latitude, longitude, and span values for the specified rectangle.

## Parameters

- `rect`: The map rectangle that corresponds to the desired region on a two-dimensional map projection.

## See Also

- [init()](mkcoordinateregion/init.md)
  Creates a coordinate region.
- [init(center: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)](mkcoordinateregion/init(center:latitudinalmeters:longitudinalmeters:).md)
  Creates a new coordinate region from the specified coordinate and distance values.
- [init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)](mkcoordinateregion/init(center:span:).md)
  Creates a coordinate region with a span around the specified center coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinateregion/init(_:))*