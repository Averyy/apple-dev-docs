# centerCoordinate

**Framework**: MapKit  
**Kind**: property

The map coordinate at the center of the map view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var centerCoordinate: CLLocationCoordinate2D { get set }
```

#### Discussion

This point represents the coordinate on which the framework centers the map. When the camera pitch is `0`, this property also corresponds to the geographic position of the camera. Changing the pitch to a nonzero value moves the camera, but doesn’t affect this property.

## See Also

- [var heading: CLLocationDirection](mkmapcamera/heading.md)
  The heading of the camera (in degrees) relative to true north.
- [var centerCoordinateDistance: CLLocationDistance](mkmapcamera/centercoordinatedistance.md)
  The distance from the center point of the map to the camera, in meters.
- [var pitch: CGFloat](mkmapcamera/pitch.md)
  The viewing angle of the camera, in degrees.
- [var altitude: CLLocationDistance](mkmapcamera/altitude.md)
  The altitude above the ground, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/centercoordinate)*