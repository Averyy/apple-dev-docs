# init(center:span:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a coordinate region with a span around the specified center coordinate.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)
```

## Parameters

- `center`: The center of the coordinate region.
- `span`: The span around the center of the coordinate region.

## See Also

### Creating a region
- [init()](./init%28%29.md)
  Creates a coordinate region.
- [init(center: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)](./init%28center,latitudinalmeters,longitudinalmeters%29.md)
  Creates a new coordinate region from the specified coordinate and distance values.
- [init(MKMapRect)](./init%28_%29.md)
  Returns the region that corresponds to the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinateregion/init(center:span:))*