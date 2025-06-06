# DDDeviceMediaPlaybackStateToString(_:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: func

Returns human-readable text for the specified media playback state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
func DDDeviceMediaPlaybackStateToString(_ inValue: DDDevice.MediaPlaybackState) -> String
```

#### Return Value

A textual value for the specified device protocol.

#### Discussion

Your extension can use this function for logging.

## Parameters

- `inValue`: A media playback state to convert to text.

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
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](dddeviceprotocoltostring(_:).md)
  Returns human-readable text for the specified protocol identifier.
- [struct DDDeviceProtocolString](dddeviceprotocolstring.md)
  String values for the manner in which an app interacts with a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevicemediaplaybackstatetostring(_:))*