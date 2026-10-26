# CLFloor

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

The floor of a building on which the user’s device is located.

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
class CLFloor
```

```objc
@interface CLFloor : NSObject
```

#### Overview

A [`CLFloor`](./clfloor.md) object specifies the floor of the building on which the device is located. In places where floor information can be determined, a [`CLLocation`](./cllocation.md) object may include a floor object along with the regular location data.

You do not create instances of this class directly, nor should you subclass it.

## Topics

### Getting the floor level
- [var level: Int](./clfloor/level.md)
  The logical floor of the building.
### Initializers
- [init?(coder: NSCoder)](./clfloor/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Location updates
- [Getting the current location of a device](./getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](./handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](./creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [class CLLocation](./cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [struct CLLocationCoordinate2D](./cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [class CLVisit](./clvisit.md)
  Information about the user’s location during a specific period of time.
- [class CLLocationSourceInformation](./cllocationsourceinformation.md)
  Information about the source that provides a location.
- [Monitoring location changes with Core Location](./monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
- [class CLServiceSession](./clservicesession-pt7n.md)
  An object that provides diagnostics about an app’s authorization to use location services.
- [CLServiceSession](./clservicesession-2ddhd.md)
- [CLServiceSessionDiagnostic](./clservicesessiondiagnostic.md)
- [CLBackgroundActivitySessionDiagnostic](./clbackgroundactivitysessiondiagnostic.md)
- [CLLocationUpdater](./cllocationupdater.md)
  An object that provides device location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clfloor)*