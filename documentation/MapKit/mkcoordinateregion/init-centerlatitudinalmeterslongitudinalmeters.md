# init(center:latitudinalMeters:longitudinalMeters:)

**Framework**: MapKit  
**Kind**: init

Creates a new coordinate region from the specified coordinate and distance values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS 9.2+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(center centerCoordinate: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)
```

#### Return Value

A region with the specified values.

## Parameters

- `centerCoordinate`: The center point of the new coordinate region.
- `latitudinalMeters`: The north-to-south span of the region (measured in meters) specified as the distance from the center point to the bounds along the north-to-south axis.
- `longitudinalMeters`: The east-to-west span of the region (measured in meters) specified as the distance from the center point to the bounds along the east-to-west axis.

## See Also

- [init()](mkcoordinateregion/init.md)
  Creates a coordinate region.
- [init(MKMapRect)](mkcoordinateregion/init(_:).md)
  Returns the region that corresponds to the specified map rectangle.
- [init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)](mkcoordinateregion/init(center:span:).md)
  Creates a coordinate region with a span around the specified center coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinateregion/init(center:latitudinalmeters:longitudinalmeters:))*