# init(devicePlacement:deviceCapabilities:primaryAudioSourceDeviceIdentifier:secondaryAudioSourceDeviceIdentifier:spatialExtensionDescription:)

**Framework**: AudioAccessoryKit  
**Kind**: init

Creates a new device configuration with spatial audio support.

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
init(devicePlacement: AccessoryControlDevice.Placement? = nil, deviceCapabilities: AccessoryControlDevice.Capabilities, primaryAudioSourceDeviceIdentifier: Data? = nil, secondaryAudioSourceDeviceIdentifier: Data? = nil, spatialExtensionDescription: AudioComponentDescription?)
```

## Parameters

- `devicePlacement`: The current placement state (e.g., `.offHead`, `.onHead`, `.inEar`) - only applicable with `.placement` capability
- `deviceCapabilities`: The capabilities supported by the device (e.g., `[.placement, .audioSpatialization]`)
- `primaryAudioSourceDeviceIdentifier`: Bluetooth address of the primary audio source (only applicable with `.audioSwitching` capability)
- `secondaryAudioSourceDeviceIdentifier`: Bluetooth address of secondary audio source (only applicable with `.audioSwitching` capability)
- `spatialExtensionDescription`: The audio component description for the spatial audio rendering extension (only applicable with `.audioSpatialization` capability)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/init(deviceplacement:devicecapabilities:primaryaudiosourcedeviceidentifier:secondaryaudiosourcedeviceidentifier:spatialextensiondescription:))*