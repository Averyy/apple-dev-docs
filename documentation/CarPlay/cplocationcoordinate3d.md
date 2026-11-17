# CPLocationCoordinate3D

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

CPLocationCoordinate3D represents a three-dimensional coordinate with latitude, longitude, and altitude components.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct CPLocationCoordinate3D
```

```c
typedef struct { ... } CPLocationCoordinate3D;
```

## Topics

### Initializers
- [init()](./cplocationcoordinate3d/init%28%29.md)
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees, altitude: CLLocationDistance)](./cplocationcoordinate3d/init%28latitude,longitude,altitude%29.md)
### Instance Properties
- [var altitude: CLLocationDistance](./cplocationcoordinate3d/altitude.md)
  altitude is the coordinate’s elevation above sea level in meters. If no altitude is available, use CLLocationDistanceMax.
- [var latitude: CLLocationDegrees](./cplocationcoordinate3d/latitude.md)
  latitude is the coordinate’s latitude value in degrees.
- [var longitude: CLLocationDegrees](./cplocationcoordinate3d/longitude.md)
  longitude is the coordinate’s longitude value in degrees.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Maneuvers
- [class CPManeuver](./cpmaneuver.md)
  An object that describes a single navigation instruction.
- [enum CPManeuverState](./cpmaneuverstate.md)
  Values that describe the state of a maneuver.
- [enum CPManeuverType](./cpmaneuvertype.md)
  Values that describe types of navigation maneuvers.
- [class CPTravelEstimates](./cptravelestimates.md)
  An object that describes the time and distance remaining for a maneuver in a navigation session.
- [class CPTripPreviewTextConfiguration](./cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.
- [func NSStringFromCPManeuverType(CPManeuverType) -> String!](./nsstringfromcpmaneuvertype%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplocationcoordinate3d)*