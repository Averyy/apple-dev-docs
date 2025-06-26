# ellipsoidalAltitude

**Framework**: Core Location  
**Kind**: property

The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var ellipsoidalAltitude: CLLocationDistance { get }
```

#### Discussion

The [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) property represents the altitude above the WGS84 ellipsoid associated with a location. Use the [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) property when your geodetic application needs an altitude with respect to a standard reference frame. Use [`altitude`](cllocation/altitude.md) if your application needs an altitude with respect to the approximate mean sea level.

The [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) value is valid if [`verticalAccuracy`](cllocation/verticalaccuracy.md) is greater than `0`, and invalid if [`verticalAccuracy`](cllocation/verticalaccuracy.md) is `0` or below. If [`verticalAccuracy`](cllocation/verticalaccuracy.md) is `0` or below, [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) is invalid and contains the value `0.0`.

Valid values for [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) can be positive or negative. Positive values indicate altitudes above the ellipsoid. Negative values indicate altitudes below the ellipsoid.

## See Also

- [var coordinate: CLLocationCoordinate2D](cllocation/coordinate.md)
  The geographical coordinate information.
- [var altitude: CLLocationDistance](cllocation/altitude.md)
  The altitude above mean sea level associated with a location, measured in meters.
- [typealias CLLocationDistance](cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](cllocation/floor.md)
  The logical floor of the building in which the user is located.
- [var timestamp: Date](cllocation/timestamp.md)
  The time at which this location was determined.
- [var sourceInformation: CLLocationSourceInformation?](cllocation/sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/ellipsoidalaltitude)*