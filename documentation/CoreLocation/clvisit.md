# CLVisit

**Framework**: Core Location  
**Kind**: class

Information about the user’s location during a specific period of time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
class CLVisit
```

#### Overview

A [`CLVisit`](clvisit.md) object encapsulates information about places that the user has been. Visit objects are created by the system and delivered by the [`CLLocationManager`](cllocationmanager.md) object to its delegate after you start the delivery of events. The visit includes the location where the visit occurred and information about the arrival and departure times as relevant. You do not create visit objects directly, nor should you subclass [`CLVisit`](clvisit.md).

Visit objects contain as much information about the visit as possible but may not always include both the arrival and departure times. For example, when the user arrives at a location, the system may send an event with only an arrival time. When the user departs a location, the event can contain both the arrival time (if your app was monitoring visits prior to the user’s arrival) and the departure time.

## Topics

### Getting the location
- [var coordinate: CLLocationCoordinate2D](clvisit/coordinate.md)
  The geographical coordinate information.
- [var horizontalAccuracy: CLLocationAccuracy](clvisit/horizontalaccuracy.md)
  The horizontal accuracy (in meters) of the specified coordinate.
### Getting the visit duration
- [var arrivalDate: Date](clvisit/arrivaldate.md)
  The approximate time at which the user arrived at the specified location.
- [var departureDate: Date](clvisit/departuredate.md)
  The approximate time at which the user left the specified location.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a user’s location in response to a request from another user.
- [class CLLocation](cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [struct CLLocationCoordinate2D](cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [class CLFloor](clfloor.md)
  The floor of a building on which the user’s device is located.
- [class CLLocationSourceInformation](cllocationsourceinformation.md)
  Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
- [class CLServiceSession](clservicesession-pt7n.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clvisit)*