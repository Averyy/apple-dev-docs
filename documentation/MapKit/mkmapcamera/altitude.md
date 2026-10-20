# altitude

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The altitude above the ground, in meters.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`centerCoordinateDistance`](./centercoordinatedistance.md) instead.

## Declaration

```swift
var altitude: CLLocationDistance { get set }
```

```objc
@property (nonatomic) CLLocationDistance altitude;
```

#### Discussion

The value you specify for this property can’t be less than `0`.

Changing this property may also change the maximum pitch for the map. If the current pitch value exceeds the new maximum, the class clamps the [`pitch`](./pitch.md) property to the new maximum.

## See Also

### Configuring the viewing angle
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [var heading: CLLocationDirection](./heading.md)
  The heading of the camera (in degrees) relative to true north.
- [var centerCoordinateDistance: CLLocationDistance](./centercoordinatedistance.md)
  The distance from the center point of the map to the camera, in meters.
- [var pitch: CGFloat](./pitch.md)
  The viewing angle of the camera, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/altitude)*