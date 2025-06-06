# DDDeviceEvent.EventType

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum

Identifiers for the types of events that occur in the device discovery life cycle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
enum EventType
```

#### Overview

An event (`DDEvent`) `eventType` is of this type.

## Topics

### Distinguishing event types
- [DDDeviceEvent.EventType.unknown](dddeviceevent/eventtype-swift.enum/unknown.md)
  A value for uninitialized event types.
- [DDDeviceEvent.EventType.deviceFound](dddeviceevent/eventtype-swift.enum/devicefound.md)
  A status that indicates when the extension finds the device of interest.
- [DDDeviceEvent.EventType.deviceLost](dddeviceevent/eventtype-swift.enum/devicelost.md)
  A status that indicates when the extension loses a connection to the device of interest.
- [DDDeviceEvent.EventType.deviceChanged](dddeviceevent/eventtype-swift.enum/devicechanged.md)
  A status that indicates when the device of interest changes configuration.
### Initializers
- [init?(rawValue: Int)](dddeviceevent/eventtype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class DDDeviceEvent](dddeviceevent.md)
  An object that provides a device or communicates its change in status.
- [func DDEventTypeToString(DDDeviceEvent.EventType) -> String](ddeventtypetostring(_:).md)
  Returns human-readable text for the specified event identifier.
- [typealias DDEventHandler](ddeventhandler.md)
  A function that the extension invokes to signal an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent/eventtype-swift.enum)*