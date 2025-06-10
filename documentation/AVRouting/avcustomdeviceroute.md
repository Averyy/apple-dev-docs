# AVCustomDeviceRoute

**Framework**: AVRouting  
**Kind**: class

An object that represents a custom device route.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVCustomDeviceRoute
```

#### Overview

Use the value of a route’s [`networkEndpoint`](avcustomdeviceroute/networkendpoint.md) or [`bluetoothIdentifier`](avcustomdeviceroute/bluetoothidentifier.md) property to establish a connection to a device. Typically, only one of the properties provides a valid value, depending on the type of device. In certain cases, both properties may provide valid values, in which case your app determines which one to use.

## Topics

### Identifying routes
- [var bluetoothIdentifier: UUID?](avcustomdeviceroute/bluetoothidentifier.md)
  An identifier to use to establish a connection to a Bluetooth device.
- [var networkEndpoint: nw_endpoint_t?](avcustomdeviceroute/networkendpoint.md)
  A local or remote endpoint to connect to.

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

- [var route: AVCustomDeviceRoute](avcustomroutingevent/route.md)
  A route for the event.
- [var reason: AVCustomRoutingEventReason](avcustomroutingevent/reason.md)
  A reason for an event, such as a user request to activate or deactivate a route.
- [enum AVCustomRoutingEventReason](avcustomroutingeventreason.md)
  Values that indicate the reason for a routing event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomdeviceroute)*