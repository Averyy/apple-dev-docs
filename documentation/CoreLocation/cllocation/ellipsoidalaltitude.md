# ellipsoidalAltitude

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CLLocationDistance ellipsoidalAltitude;
```

## Discussion

The [`ellipsoidalAltitude`](./ellipsoidalaltitude.md) property represents the altitude above the WGS84 ellipsoid associated with a location. Use the [`ellipsoidalAltitude`](./ellipsoidalaltitude.md) property when your geodetic application needs an altitude with respect to a standard reference frame. Use [`altitude`](./altitude.md) if your application needs an altitude with respect to the approximate mean sea level.

The [`ellipsoidalAltitude`](./ellipsoidalaltitude.md) value is valid if [`verticalAccuracy`](./verticalaccuracy.md) is greater than `0`, and invalid if [`verticalAccuracy`](./verticalaccuracy.md) is `0` or below. If [`verticalAccuracy`](./verticalaccuracy.md) is `0` or below, [`ellipsoidalAltitude`](./ellipsoidalaltitude.md) is invalid and contains the value `0.0`.

Valid values for [`ellipsoidalAltitude`](./ellipsoidalaltitude.md) can be positive or negative. Positive values indicate altitudes above the ellipsoid. Negative values indicate altitudes below the ellipsoid.

## See Also

### Getting the location attributes
- [var coordinate: CLLocationCoordinate2D](./coordinate.md)
  The geographical coordinate information.
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude above mean sea level associated with a location, measured in meters.
- [typealias CLLocationDistance](../cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](./floor.md)
  The logical floor of the building in which the user is located.
- [var timestamp: Date](./timestamp.md)
  The time at which this location was determined.
- [var sourceInformation: CLLocationSourceInformation?](./sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/ellipsoidalaltitude)*