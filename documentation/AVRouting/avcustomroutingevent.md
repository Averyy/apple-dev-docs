# AVCustomRoutingEvent

**Framework**: AVRouting  
**Kind**: class

An object that represents an event that occurs on a route.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVCustomRoutingEvent
```

#### Overview

Depending on the route’s reason, apps establish or tear down a connection to a specified route.

## Topics

### Inspecting an event
- [var route: AVCustomDeviceRoute](avcustomroutingevent/route.md)
  A route for the event.
- [class AVCustomDeviceRoute](avcustomdeviceroute.md)
  An object that represents a custom device route.
- [var reason: AVCustomRoutingEventReason](avcustomroutingevent/reason.md)
  A reason for an event, such as a user request to activate or deactivate a route.
- [enum AVCustomRoutingEventReason](avcustomroutingeventreason.md)
  Values that indicate the reason for a routing event.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVCustomRoutingController](avcustomroutingcontroller.md)
  An object that manages the connection from a device to a destination.
- [protocol AVCustomRoutingControllerDelegate](avcustomroutingcontrollerdelegate.md)
  A protocol for delegates of a custom routing controller.
- [class AVCustomRoutingActionItem](avcustomroutingactionitem.md)
  An object that represents a custom action item to display in a device route picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingevent)*