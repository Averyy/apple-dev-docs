# altitude

**Framework**: Core Location  
**Kind**: property

The altitude above mean sea level associated with a location, measured in meters.

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
var altitude: CLLocationDistance { get }
```

#### Discussion

The [`altitude`](cllocation/altitude.md) property represents an orthometric height, which is the height above the approximate mean sea level. Positive values indicate altitudes above mean sea level. Negative values indicate altitudes below mean sea level.

When [`verticalAccuracy`](cllocation/verticalaccuracy.md) contains `0` or a negative number, the value of [`altitude`](cllocation/altitude.md) is invalid. The value of [`altitude`](cllocation/altitude.md) is valid when [`verticalAccuracy`](cllocation/verticalaccuracy.md) contains a postive number.

In most cases, Core Location approximates mean sea level using the Earth Gravitational Model 2008 (EGM 2008) geoid associated with the World Geodetic System 1984 (WGS84) standard. In some rare cases, Core Location approximates mean sea level using the DMA 10x10 geoid grid. The discrepancy between these two geoids is typically less than 5 meters.

See [`ellipsoidalAltitude`](cllocation/ellipsoidalaltitude.md) if your application uses an altitude with respect to the WGS84 reference frame.

> **Note**:  In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

 In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

- [var coordinate: CLLocationCoordinate2D](cllocation/coordinate.md)
  The geographical coordinate information.
- [var ellipsoidalAltitude: CLLocationDistance](cllocation/ellipsoidalaltitude.md)
  The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [typealias CLLocationDistance](cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](cllocation/floor.md)
  The logical floor of the building in which the user is located.
- [var timestamp: Date](cllocation/timestamp.md)
  The time at which this location was determined.
- [var sourceInformation: CLLocationSourceInformation?](cllocation/sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/altitude)*