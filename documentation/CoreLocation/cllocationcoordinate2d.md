# CLLocationCoordinate2D

**Framework**: Core Location  
**Kind**: struct

The latitude and longitude associated with a location, specified using the WGS 84 reference frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CLLocationCoordinate2D
```

## Topics

### Creating a location coordinate
- [init()](cllocationcoordinate2d/init.md)
  Creates a location coordinate object.
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](cllocationcoordinate2d/init(latitude:longitude:).md)
  Creates a location coordination object with the specified latitude and longitude values.
- [func CLLocationCoordinate2DMake(CLLocationDegrees, CLLocationDegrees) -> CLLocationCoordinate2D](cllocationcoordinate2dmake(_:_:).md)
  Formats a latitude and longitude value into a coordinate data structure format.
### Getting the geographic coordinates
- [var latitude: CLLocationDegrees](cllocationcoordinate2d/latitude.md)
  The latitude in degrees.
- [var longitude: CLLocationDegrees](cllocationcoordinate2d/longitude.md)
  The longitude in degrees.
### Validating a coordinate
- [func CLLocationCoordinate2DIsValid(CLLocationCoordinate2D) -> Bool](cllocationcoordinate2disvalid(_:).md)
  Returns a Boolean value indicating whether the specified coordinate is valid.
- [let kCLLocationCoordinate2DInvalid: CLLocationCoordinate2D](kcllocationcoordinate2dinvalid.md)
  An invalid coordinate value.

## Relationships

### Conforms To
- [Animatable](../SwiftUI/Animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a user’s location in response to a request from another user.
- [class CLLocation](cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [class CLFloor](clfloor.md)
  The floor of a building on which the user’s device is located.
- [class CLVisit](clvisit.md)
  Information about the user’s location during a specific period of time.
- [class CLLocationSourceInformation](cllocationsourceinformation.md)
  Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
- [class CLServiceSession](clservicesession-pt7n.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d)*