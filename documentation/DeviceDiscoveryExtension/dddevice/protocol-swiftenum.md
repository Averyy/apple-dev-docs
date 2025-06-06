# DDDevice.Protocol

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum

An identifier for the manner in which an app interacts with a device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
enum `Protocol`
```

#### Overview

The device ([`DDDevice`](dddevice.md)) [`protocol`](dddevice/protocol-swift.property.md) property is of this type.

## Topics

### Indicating a device protocol
- [DDDevice.Protocol.dial](dddevice/protocol-swift.enum/dial.md)
  A protocol for client devices that stream media to a TV or set-top box.
- [DDDevice.Protocol.invalid](dddevice/protocol-swift.enum/invalid.md)
  A default value for a device protocol.
### Initializers
- [init?(rawValue: Int)](dddevice/protocol-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class DDDevice](dddevice.md)
  An object that describes a discovered device of interest.
- [DDDevice.Category](dddevice/category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.
- [enum DDDeviceState](dddevicestate.md)
  A state that represents the level of user interaction with the device.
- [func DDDeviceCategoryToString(DDDevice.Category) -> String](dddevicecategorytostring(_:).md)
  Returns human-readable text for the specified identifier that describes a device’s category.
- [func DDDeviceStateToString(DDDeviceState) -> String](dddevicestatetostring(_:).md)
  Returns human-readable text for the specified identifier that describes a device’s status.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](dddeviceprotocoltostring(_:).md)
  Returns human-readable text for the specified protocol identifier.
- [struct DDDeviceProtocolString](dddeviceprotocolstring.md)
  String values for the manner in which an app interacts with a device.
- [func DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String](dddevicemediaplaybackstatetostring(_:).md)
  Returns human-readable text for the specified media playback state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/protocol-swift.enum)*