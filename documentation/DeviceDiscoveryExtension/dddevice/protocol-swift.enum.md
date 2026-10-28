# DDDevice.Protocol

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum  
**Role**: Enumeration

An identifier for the manner in which an app interacts with a device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum `Protocol`
```

```c
enum DDDeviceProtocol : NSInteger;
```

## Overview

The device ([`DDDevice`](../dddevice.md)) [`protocol`](./protocol-swift.property.md) property is of this type.

## Topics

### Indicating a device protocol
- [DDDevice.Protocol.dial](./protocol-swift.enum/dial.md)
  A protocol for client devices that stream media to a TV or set-top box.
- [DDDevice.Protocol.invalid](./protocol-swift.enum/invalid.md)
  A default value for a device protocol.
### Initializers
- [init?(rawValue: Int)](./protocol-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Device information
- [class DDDevice](../dddevice.md)
  An object that describes a discovered device of interest.
- [DDDevice.Category](./category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.
- [enum DDDeviceState](../dddevicestate.md)
  A state that represents the level of user interaction with the device.
- [func DDDeviceCategoryToString(DDDevice.Category) -> String](../dddevicecategorytostring%28_%29.md)
  Returns human-readable text for the specified identifier that describes a device’s category.
- [func DDDeviceStateToString(DDDeviceState) -> String](../dddevicestatetostring%28_%29.md)
  Returns human-readable text for the specified identifier that describes a device’s status.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](../dddeviceprotocoltostring%28_%29.md)
  Returns human-readable text for the specified protocol identifier.
- [struct DDDeviceProtocolString](../dddeviceprotocolstring.md)
  String values for the manner in which an app interacts with a device.
- [func DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String](../dddevicemediaplaybackstatetostring%28_%29.md)
  Returns human-readable text for the specified media playback state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/protocol-swift.enum)*