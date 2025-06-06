# DDEventTypeToString(_:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: func

Returns human-readable text for the specified event identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
func DDEventTypeToString(_ inValue: DDDeviceEvent.EventType) -> String
```

#### Return Value

A textual value for the specified event type.

#### Discussion

Your extension can use this function for logging.

## Parameters

- `inValue`: An event identifier to convert to text.

## See Also

- [class DDDeviceEvent](dddeviceevent.md)
  An object that provides a device or communicates its change in status.
- [DDDeviceEvent.EventType](dddeviceevent/eventtype-swift.enum.md)
  Identifiers for the types of events that occur in the device discovery life cycle.
- [typealias DDEventHandler](ddeventhandler.md)
  A function that the extension invokes to signal an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/ddeventtypetostring(_:))*