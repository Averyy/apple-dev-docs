# floor

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The logical floor of the building in which the user is located.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var floor: CLFloor? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) CLFloor * floor;
```

#### Discussion

If floor information is not available for the current location, the value of this property is `nil`.

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
- [var timestamp: Date](./timestamp.md)
  The time at which this location was determined.
- [var sourceInformation: CLLocationSourceInformation?](./sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/floor)*