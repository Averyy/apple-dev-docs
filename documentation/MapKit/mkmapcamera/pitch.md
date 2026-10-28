# pitch

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The viewing angle of the camera, in degrees.

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
var pitch: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat pitch;
```

## Discussion

A value of `0` results in a camera that points straight down at the map. Angles greater than `0` result in a camera that pitches toward the horizon by the specified number of degrees. If the map type is [`MKMapType.satellite`](../mkmaptype/satellite.md) or [`MKMapType.hybrid`](../mkmaptype/hybrid.md), the object clamps the pitch value to `0`.

The class may clamp the value in this property to a maximum value to maintain map readability. There’s no fixed maximum value, though, because the actual maximum value is dependent on the altitude of the camera.

## See Also

### Configuring the viewing angle
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [var heading: CLLocationDirection](./heading.md)
  The heading of the camera (in degrees) relative to true north.
- [var centerCoordinateDistance: CLLocationDistance](./centercoordinatedistance.md)
  The distance from the center point of the map to the camera, in meters.
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude above the ground, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapcamera/pitch)*