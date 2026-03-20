# init(devicePlacement:deviceCapabilities:primaryAudioSourceDeviceIdentifier:secondaryAudioSourceDeviceIdentifier:)

**Framework**: AudioAccessoryKit  
**Kind**: init

Creates an audio accessory configuration.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(devicePlacement: AccessoryControlDevice.Placement? = nil, deviceCapabilities: AccessoryControlDevice.Capabilities, primaryAudioSourceDeviceIdentifier: Data? = nil, secondaryAudioSourceDeviceIdentifier: Data? = nil)
```

#### Discussion

For example, the following code creates a configuration for a device that’s not being worn and is using Bluetooth address `0x12356789ABC` as its primary audio source:

```swift
let configuration = Configuration(
    devicePlacement: .offHead,
    deviceCapabilities: [.placement, .audioSwitching],
    primaryAudioSourceDeviceIdentifier: Data([0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC]),
)
```

## Parameters

- `devicePlacement`: The current placement state of the accessory.
- `deviceCapabilities`: The capabilities the accessory supports.
- `primaryAudioSourceDeviceIdentifier`: The Bluetooth address of the primary audio source.
- `secondaryAudioSourceDeviceIdentifier`: The Bluetooth address of secondary audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/init(deviceplacement:devicecapabilities:primaryaudiosourcedeviceidentifier:secondaryaudiosourcedeviceidentifier:))*