# timestamp

**Framework**: Core Location  
**Kind**: property

The time at which this location was determined.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timestamp: Date { get }
```

#### Discussion

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

- [var coordinate: CLLocationCoordinate2D](cllocation/coordinate.md)
  The geographical coordinate information.
- [var altitude: CLLocationDistance](cllocation/altitude.md)
  The altitude above mean sea level associated with a location, measured in meters.
- [var ellipsoidalAltitude: CLLocationDistance](cllocation/ellipsoidalaltitude.md)
  The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [typealias CLLocationDistance](cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](cllocation/floor.md)
  The logical floor of the building in which the user is located.
- [var sourceInformation: CLLocationSourceInformation?](cllocation/sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/timestamp)*