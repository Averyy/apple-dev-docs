# coordinate

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The geographical coordinate information.

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
var coordinate: CLLocationCoordinate2D { get }
```

```objc
@property (nonatomic, readonly) CLLocationCoordinate2D coordinate;
```

## Discussion

When running in the simulator, Core Location uses the values provided to it by the simulator. You must run your application on an iOS-based device to get the actual location of that device.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting the location attributes
- [var altitude: CLLocationDistance](./altitude.md)
  The altitude above mean sea level associated with a location, measured in meters.
- [var ellipsoidalAltitude: CLLocationDistance](./ellipsoidalaltitude.md)
  The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [typealias CLLocationDistance](../cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](./floor.md)
  The logical floor of the building in which the user is located.
- [var timestamp: Date](./timestamp.md)
  The time at which this location was determined.
- [var sourceInformation: CLLocationSourceInformation?](./sourceinformation.md)
  Information about the source that provides the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/coordinate)*