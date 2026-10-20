# DDDeviceEvent.EventType

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum  
**Role**: Enumeration

Identifiers for the types of events that occur in the device discovery life cycle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum EventType
```

```c
enum DDEventType : NSInteger;
```

#### Overview

An event (`DDEvent`) `eventType` is of this type.

## Topics

### Distinguishing event types
- [DDDeviceEvent.EventType.unknown](./eventtype-swift.enum/unknown.md)
  A value for uninitialized event types.
- [DDDeviceEvent.EventType.deviceFound](./eventtype-swift.enum/devicefound.md)
  A status that indicates when the extension finds the device of interest.
- [DDDeviceEvent.EventType.deviceLost](./eventtype-swift.enum/devicelost.md)
  A status that indicates when the extension loses a connection to the device of interest.
- [DDDeviceEvent.EventType.deviceChanged](./eventtype-swift.enum/devicechanged.md)
  A status that indicates when the device of interest changes configuration.
### Initializers
- [init?(rawValue: Int)](./eventtype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Life cycle
- [class DDDeviceEvent](../dddeviceevent.md)
  An object that provides a device or communicates its change in status.
- [func DDEventTypeToString(DDDeviceEvent.EventType) -> String](../ddeventtypetostring%28_%29.md)
  Returns human-readable text for the specified event identifier.
- [typealias DDEventHandler](../ddeventhandler.md)
  A function that the extension invokes to signal an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent/eventtype-swift.enum)*