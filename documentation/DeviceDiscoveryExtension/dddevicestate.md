# DDDeviceState

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum

A state that represents the level of user interaction with the device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
enum DDDeviceState
```

#### Overview

The device ([`DDDevice`](dddevice.md)) [`state`](dddevice/state.md) property is of this type.

## Topics

### Communicating a device’s status
- [DDDeviceState.invalid](dddevicestate/invalid.md)
  A state that indicates the device is invalid or that the user disapproves of the device.
- [DDDeviceState.activating](dddevicestate/activating.md)
  A state that indicates when the user selects the device in the picker UI.
- [DDDeviceState.activated](dddevicestate/activated.md)
  A state that indicates when the user authorizes the device and the app connects to the device.
- [DDDeviceState.authorized](dddevicestate/authorized.md)
  A state that indicates when the user authorizes the device.
- [DDDeviceState.invalidating](dddevicestate/invalidating.md)
  A state that indicates that the device is soon to be invalid.
### Initializers
- [init?(rawValue: Int)](dddevicestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class DDDevice](dddevice.md)
  An object that describes a discovered device of interest.
- [DDDevice.Category](dddevice/category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.
- [func DDDeviceCategoryToString(DDDevice.Category) -> String](dddevicecategorytostring(_:).md)
  Returns human-readable text for the specified identifier that describes a device’s category.
- [func DDDeviceStateToString(DDDeviceState) -> String](dddevicestatetostring(_:).md)
  Returns human-readable text for the specified identifier that describes a device’s status.
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](dddeviceprotocoltostring(_:).md)
  Returns human-readable text for the specified protocol identifier.
- [struct DDDeviceProtocolString](dddeviceprotocolstring.md)
  String values for the manner in which an app interacts with a device.
- [func DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String](dddevicemediaplaybackstatetostring(_:).md)
  Returns human-readable text for the specified media playback state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevicestate)*