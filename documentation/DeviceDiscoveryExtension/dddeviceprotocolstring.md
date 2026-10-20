# DDDeviceProtocolString

**Framework**: DeviceDiscoveryExtension  
**Kind**: struct  
**Role**: Structure

String values for the manner in which an app interacts with a device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
struct DDDeviceProtocolString
```

```c
typedef NSString * DDDeviceProtocolString;
```

#### Discussion

When an app creates a device discovery extension to stream content to a third-party media receiver, the protocol is Discovery and Launch (DIAL), as designated by the [`DDDevice.Protocol.dial`](./dddevice/protocol-swift.enum/dial.md) option.

## Topics

### Creating a device protocol string
- [init(rawValue: String)](./dddeviceprotocolstring/init%28rawvalue%29.md)
  Creates a string for the manner in which an app interacts with a device.
### Specifying a device protocol string
- [static let dial: DDDeviceProtocolString](./dddeviceprotocolstring/dial.md)
  A human-readable string for the Discovery and Launch protocol.
- [static let invalid: DDDeviceProtocolString](./dddeviceprotocolstring/invalid.md)
  A human-readable string for the default device protocol.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Device information
- [class DDDevice](./dddevice.md)
  An object that describes a discovered device of interest.
- [DDDevice.Category](./dddevice/category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.
- [enum DDDeviceState](./dddevicestate.md)
  A state that represents the level of user interaction with the device.
- [func DDDeviceCategoryToString(DDDevice.Category) -> String](./dddevicecategorytostring%28_%29.md)
  Returns human-readable text for the specified identifier that describes a device’s category.
- [func DDDeviceStateToString(DDDeviceState) -> String](./dddevicestatetostring%28_%29.md)
  Returns human-readable text for the specified identifier that describes a device’s status.
- [DDDevice.Protocol](./dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](./dddeviceprotocoltostring%28_%29.md)
  Returns human-readable text for the specified protocol identifier.
- [func DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String](./dddevicemediaplaybackstatetostring%28_%29.md)
  Returns human-readable text for the specified media playback state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceprotocolstring)*