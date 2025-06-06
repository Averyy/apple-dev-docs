# DDDeviceEvent

**Framework**: DeviceDiscoveryExtension  
**Kind**: class

An object that provides a device or communicates its change in status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class DDDeviceEvent
```

#### Overview

The extension creates and configures an instance of this class to represent a moment of interest in the device discovery life cycle. The event’s `eventType` ([`DDDeviceEvent.EventType`](dddeviceevent/eventtype-swift.enum.md)) describes a particular status.

For example, when the extension discovers a device of interest, it instantiates an instance of this class with the type [`DDDeviceEvent.EventType.deviceFound`](dddeviceevent/eventtype-swift.enum/devicefound.md).

```swift
var session: DDDiscoverySession?
...
var deviceEvent = DDDeviceEvent(eventType: .deviceFound, device: ddDevice)
```

Then, the extension provides the discovered device to the system using [`report(_:)`](dddiscoverysession/report(_:).md) for eventual display in the route picker view ([`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView)).

```swift
session?.report(deviceEvent)
```

## Topics

### Creating a device event
- [init(eventType: DDDeviceEvent.EventType, device: DDDevice)](dddeviceevent/init(eventtype:device:).md)
  Creates an event object that conveys status for a discovered device of interest.
### Configuring a device event
- [var eventType: DDDeviceEvent.EventType](dddeviceevent/eventtype-swift.property.md)
  A type for the event that describes the discovery status.
- [DDDeviceEvent.EventType](dddeviceevent/eventtype-swift.enum.md)
  Identifiers for the types of events that occur in the device discovery life cycle.
- [var device: DDDevice](dddeviceevent/device.md)
  An object that describes a third-party media receiver.

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

- [DDDeviceEvent.EventType](dddeviceevent/eventtype-swift.enum.md)
  Identifiers for the types of events that occur in the device discovery life cycle.
- [func DDEventTypeToString(DDDeviceEvent.EventType) -> String](ddeventtypetostring(_:).md)
  Returns human-readable text for the specified event identifier.
- [typealias DDEventHandler](ddeventhandler.md)
  A function that the extension invokes to signal an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent)*