# DDDevice.Category

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum  
**Role**: Enumeration

An option that determines the icon for the device in the picker UI.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum Category
```

```c
enum DDDeviceCategory : NSInteger;
```

## Overview

The device ([`DDDevice`](../dddevice.md)) [`category`](./category-swift.property.md) property is of this type.

Each value in this enumeration determines a different icon that the picker UI ([`AVRoutePickerView`](../../AVKit/avroutepickerview.md)) displays, which helps the user visually confirm that their selection corresponds to the device they intend to stream media to.

## Topics

### Choosing an icon for the device picker
- [DDDevice.Category.desktopComputer](./category-swift.enum/desktopcomputer.md)
  An icon that depicts a desktop computer.
- [DDDevice.Category.hifiSpeaker](./category-swift.enum/hifispeaker.md)
  An icon that depicts a high-fidelity speaker.
- [DDDevice.Category.hifiSpeakerMultiple](./category-swift.enum/hifispeakermultiple.md)
  An icon that depicts multiple high-fidelity speakers.
- [DDDevice.Category.laptopComputer](./category-swift.enum/laptopcomputer.md)
  An icon that depicts a laptop computer.
- [DDDevice.Category.tv](./category-swift.enum/tv.md)
  An icon that depicts a television.
- [DDDevice.Category.tvWithMediaBox](./category-swift.enum/tvwithmediabox.md)
  An icon that depicts a TV with a set-top box.
### Enumeration Cases
- [DDDevice.Category.accessorySetup](./category-swift.enum/accessorysetup.md)
### Initializers
- [init?(rawValue: Int)](./category-swift.enum/init%28rawvalue%29.md)

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
- [enum DDDeviceState](../dddevicestate.md)
  A state that represents the level of user interaction with the device.
- [func DDDeviceCategoryToString(DDDevice.Category) -> String](../dddevicecategorytostring%28_%29.md)
  Returns human-readable text for the specified identifier that describes a device’s category.
- [func DDDeviceStateToString(DDDeviceState) -> String](../dddevicestatetostring%28_%29.md)
  Returns human-readable text for the specified identifier that describes a device’s status.
- [DDDevice.Protocol](./protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [func DDDeviceProtocolToString(DDDevice.Protocol) -> String](../dddeviceprotocoltostring%28_%29.md)
  Returns human-readable text for the specified protocol identifier.
- [struct DDDeviceProtocolString](../dddeviceprotocolstring.md)
  String values for the manner in which an app interacts with a device.
- [func DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String](../dddevicemediaplaybackstatetostring%28_%29.md)
  Returns human-readable text for the specified media playback state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/category-swift.enum)*