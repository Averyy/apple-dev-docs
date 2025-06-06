# altitude

**Framework**: MapKit  
**Kind**: property

The altitude above the ground, in meters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var altitude: CLLocationDistance { get set }
```

#### Discussion

The value you specify for this property can’t be less than `0`.

Changing this property may also change the maximum pitch for the map. If the current pitch value exceeds the new maximum, the class clamps the [`pitch`](mkmapcamera/pitch.md) property to the new maximum.

## See Also

- [var centerCoordinate: CLLocationCoordinate2D](mkmapcamera/centercoordinate.md)
  The map coordinate at the center of the map view.
- [var heading: CLLocationDirection](mkmapcamera/heading.md)
  The heading of the camera (in degrees) relative to true north.
- [var centerCoordinateDistance: CLLocationDistance](mkmapcamera/centercoordinatedistance.md)
  The distance from the center point of the map to the camera, in meters.
- [var pitch: CGFloat](mkmapcamera/pitch.md)
  The viewing angle of the camera, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/altitude)*