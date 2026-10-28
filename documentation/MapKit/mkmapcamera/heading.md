# heading

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The heading of the camera (in degrees) relative to true north.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var heading: CLLocationDirection { get set }
```

```objc
@property (nonatomic) CLLocationDirection heading;
```

## Discussion

The value `0` means that the top edge of the map view corresponds to true north. The value `90` means the top of the map is pointing due east. The value `180` means the top of the map points due south, and so on.

## See Also

### Configuring the viewing angle
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [var centerCoordinateDistance: CLLocationDistance](./centercoordinatedistance.md)
  The distance from the center point of the map to the camera, in meters.
- [var pitch: CGFloat](./pitch.md)
  The viewing angle of the camera, in degrees.
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude above the ground, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/heading)*