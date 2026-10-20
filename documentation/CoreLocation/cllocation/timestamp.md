# timestamp

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSDate * timestamp;
```

#### Discussion

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting the location attributes
- [var coordinate: CLLocationCoordinate2D](./coordinate.md)
  The geographical coordinate information.
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude above mean sea level associated with a location, measured in meters.
- [var ellipsoidalAltitude: CLLocationDistance](./ellipsoidalaltitude.md)
  The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [typealias CLLocationDistance](../cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](./floor.md)
  The logical floor of the building in which the user is located.
- [var sourceInformation: CLLocationSourceInformation?](./sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/timestamp)*