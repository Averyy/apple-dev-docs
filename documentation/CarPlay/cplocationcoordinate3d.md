# CPLocationCoordinate3D

**Framework**: CarPlay  
**Kind**: struct

CPLocationCoordinate3D represents a three-dimensional coordinate with latitude, longitude, and altitude components.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct CPLocationCoordinate3D
```

## Topics

### Initializers
- [init()](cplocationcoordinate3d/init.md)
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees, altitude: CLLocationDistance)](cplocationcoordinate3d/init(latitude:longitude:altitude:).md)
### Instance Properties
- [var altitude: CLLocationDistance](cplocationcoordinate3d/altitude.md)
  altitude is the coordinate’s elevation above sea level in meters. If no altitude is available, use CLLocationDistanceMax.
- [var latitude: CLLocationDegrees](cplocationcoordinate3d/latitude.md)
  latitude is the coordinate’s latitude value in degrees.
- [var longitude: CLLocationDegrees](cplocationcoordinate3d/longitude.md)
  longitude is the coordinate’s longitude value in degrees.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplocationcoordinate3d)*