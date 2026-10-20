# centerCoordinateDistance

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The distance from the center point of the map to the camera, in meters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var centerCoordinateDistance: CLLocationDistance { get set }
```

```objc
@property (nonatomic) CLLocationDistance centerCoordinateDistance;
```

## See Also

### Configuring the viewing angle
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [var heading: CLLocationDirection](./heading.md)
  The heading of the camera (in degrees) relative to true north.
- [var pitch: CGFloat](./pitch.md)
  The viewing angle of the camera, in degrees.
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude above the ground, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/centercoordinatedistance)*