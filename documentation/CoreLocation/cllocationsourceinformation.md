# CLLocationSourceInformation

**Framework**: Core Location  
**Kind**: class

Information about the source that provides a location.

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
class CLLocationSourceInformation
```

#### Overview

[`CLLocationSourceInformation`](cllocationsourceinformation.md) contains information about the source that provides a [`CLLocation`](cllocation.md) instance, such as instances that [`locationManager(_:didUpdateLocations:)`](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md) delivers. For example, an app may choose to check the source information and reject locations if the [`isSimulatedBySoftware`](cllocationsourceinformation/issimulatedbysoftware.md) property is `true` when the developer isn’t debugging or testing the app.

## Topics

### Creating a location source information object
- [init(softwareSimulationState: Bool, andExternalAccessoryState: Bool)](cllocationsourceinformation/init(softwaresimulationstate:andexternalaccessorystate:).md)
  Creates an instance of location source information.
### Identifying the source of location data
- [var isProducedByAccessory: Bool](cllocationsourceinformation/isproducedbyaccessory.md)
  A Boolean value that indicates whether the system receives the location from an external accessory.
- [var isSimulatedBySoftware: Bool](cllocationsourceinformation/issimulatedbysoftware.md)
  A Boolean value that indicates whether the system generates the location using on-device software simulation.

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
- [class CLVisit](clvisit.md)
  Information about the user’s location during a specific period of time.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
- [class CLServiceSession](clservicesession-pt7n.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationsourceinformation)*