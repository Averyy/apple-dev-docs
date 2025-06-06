# DDDeviceEvent.EventType.deviceChanged

**Framework**: DeviceDiscoveryExtension  
**Kind**: case

A status that indicates when the device of interest changes configuration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
case deviceChanged
```

#### Discussion

Report an event of this type to notify the system when information about a discovered device changes, for example, when:

- Adding or losing a communication protocol.
- Updating information about the current media that the device plays.

## See Also

- [DDDeviceEvent.EventType.unknown](dddeviceevent/eventtype-swift.enum/unknown.md)
  A value for uninitialized event types.
- [DDDeviceEvent.EventType.deviceFound](dddeviceevent/eventtype-swift.enum/devicefound.md)
  A status that indicates when the extension finds the device of interest.
- [DDDeviceEvent.EventType.deviceLost](dddeviceevent/eventtype-swift.enum/devicelost.md)
  A status that indicates when the extension loses a connection to the device of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent/eventtype-swift.enum/devicechanged)*