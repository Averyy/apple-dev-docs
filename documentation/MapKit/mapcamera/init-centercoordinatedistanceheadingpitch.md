# init(centerCoordinate:distance:heading:pitch:)

**Framework**: MapKit  
**Kind**: init

Creates a camera using the specified distance, pitch, and heading information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
init(centerCoordinate: CLLocationCoordinate2D, distance: Double, heading: Double = 0, pitch: Double = 0)
```

## Parameters

- `centerCoordinate`: The map coordinate at the center of the map view.
- `distance`: The distance from the center point of the map to the camera, in meters.
- `heading`: The heading of the camera, in degrees, relative to true North.
- `pitch`: The viewing angle of the camera, in degrees.

## See Also

- [init(MKMapCamera)](mapcamera/init(_:).md)
  Creates a map camera from the given MapKit camera object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcamera/init(centercoordinate:distance:heading:pitch:))*