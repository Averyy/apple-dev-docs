# DDEventHandler

**Framework**: DeviceDiscoveryExtension  
**Kind**: typealias  
**Role**: Type Alias

A function that the extension invokes to signal an event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
typealias DDEventHandler = (DDDeviceEvent) -> Void
```

```c
typedef void (^)(DDDeviceEvent *) DDEventHandler;
```

## Discussion

A device discovery extension implements a closure of this format and calls it after creating argument events. In the implementation, the extension creates device events (`DDEvent`) and passes them to the system by calling [`report(_:)`](./dddiscoverysession/report%28_%29.md).

For an example event handler, see `Appex.swift` in [Discovering a third-party media-streaming device](./discovering-a-third-party-media-streaming-device.md).

## Parameters

- `inEvent`: An event that the extension creates for the event handler.

## See Also

### Life cycle
- [class DDDeviceEvent](./dddeviceevent.md)
  An object that provides a device or communicates its change in status.
- [DDDeviceEvent.EventType](./dddeviceevent/eventtype-swift.enum.md)
  Identifiers for the types of events that occur in the device discovery life cycle.
- [func DDEventTypeToString(DDDeviceEvent.EventType) -> String](./ddeventtypetostring%28_%29.md)
  Returns human-readable text for the specified event identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/ddeventhandler)*