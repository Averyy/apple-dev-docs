# AVCustomRoutingController

**Framework**: AVRouting  
**Kind**: class

An object that manages the connection from a device to a destination.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVCustomRoutingController
```

#### Overview

A routing controller also informs its [`delegate`](avcustomroutingcontroller/delegate.md) object about which routes the user previously authorized, so it can reconnect, if appropriate.

## Topics

### Managing authorization
- [var authorizedRoutes: [AVCustomDeviceRoute]](avcustomroutingcontroller/authorizedroutes.md)
  A list of authorized routes.
- [class let authorizedRoutesDidChange: NSNotification.Name](avcustomroutingcontroller/authorizedroutesdidchange.md)
  A notification the system posts when the list of authorized routes changes.
- [func invalidateAuthorization(for: AVCustomDeviceRoute)](avcustomroutingcontroller/invalidateauthorization(for:).md)
  Revokes an app’s authorization to connect to a route.
### Configuring route addresses
- [var knownRouteIPs: [AVCustomRoutingPartialIP]](avcustomroutingcontroller/knownrouteips.md)
  An array of route addresses known to be on the local network.
- [class AVCustomRoutingPartialIP](avcustomroutingpartialip.md)
  An object that represents a full or partial IP address.
### Activating a route
- [func isRouteActive(AVCustomDeviceRoute) -> Bool](avcustomroutingcontroller/isrouteactive(_:).md)
  Returns a Boolean value that indicates whether a route is active.
- [func setActive(Bool, for: AVCustomDeviceRoute)](avcustomroutingcontroller/setactive(_:for:).md)
  Sets the active state of a route.
### Accessing the delegate
- [var delegate: (any AVCustomRoutingControllerDelegate)?](avcustomroutingcontroller/delegate.md)
  A delegate object for a routing controller.
### Customizing the user interface
- [var customActionItems: [AVCustomRoutingActionItem]](avcustomroutingcontroller/customactionitems.md)
  An array of custom action items to add to a route picker.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AVCustomRoutingControllerDelegate](avcustomroutingcontrollerdelegate.md)
  A protocol for delegates of a custom routing controller.
- [class AVCustomRoutingEvent](avcustomroutingevent.md)
  An object that represents an event that occurs on a route.
- [class AVCustomRoutingActionItem](avcustomroutingactionitem.md)
  An object that represents a custom action item to display in a device route picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller)*