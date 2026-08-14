# AccessoryControlDevice.Configuration

**Framework**: AudioAccessoryKit  
**Kind**: struct

The configuration for an accessory.

**Availability**:
- iOS 26.4+

## Declaration

```swift
struct Configuration
```

#### Overview

Use this structure to define the characteristics and capabilities of your audio accessory.

## Topics

### Creating a configuration
- [init(devicePlacement: AccessoryControlDevice.Placement?, deviceCapabilities: AccessoryControlDevice.Capabilities, primaryAudioSourceDeviceIdentifier: Data?, secondaryAudioSourceDeviceIdentifier: Data?)](accessorycontroldevice/configuration-swift.struct/init(deviceplacement:devicecapabilities:primaryaudiosourcedeviceidentifier:secondaryaudiosourcedeviceidentifier:).md)
  Creates an audio accessory configuration.
### Accessing configuration options
- [var deviceCapabilities: AccessoryControlDevice.Capabilities](accessorycontroldevice/configuration-swift.struct/devicecapabilities.md)
  The capabilities the accessory supports.
- [var devicePlacement: AccessoryControlDevice.Placement?](accessorycontroldevice/configuration-swift.struct/deviceplacement.md)
  The physical position of the accessory.
- [var primaryAudioSourceDeviceIdentifier: Data?](accessorycontroldevice/configuration-swift.struct/primaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the primary source of audio.
- [var secondaryAudioSourceDeviceIdentifier: Data?](accessorycontroldevice/configuration-swift.struct/secondaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the secondary source of audio.
### Initializers
- [init(devicePlacement: AccessoryControlDevice.Placement?, deviceCapabilities: AccessoryControlDevice.Capabilities, primaryAudioSourceDeviceIdentifier: Data?, secondaryAudioSourceDeviceIdentifier: Data?, spatialExtensionDescription: AudioComponentDescription?)](accessorycontroldevice/configuration-swift.struct/init(deviceplacement:devicecapabilities:primaryaudiosourcedeviceidentifier:secondaryaudiosourcedeviceidentifier:spatialextensiondescription:).md)
  Creates a new device configuration with spatial audio support.
### Instance Properties
- [var spatialExtensionDescription: AudioComponentDescription?](accessorycontroldevice/configuration-swift.struct/spatialextensiondescription.md)
  The spatial audio component description.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [AccessoryControlDevice.Placement](accessorycontroldevice/placement.md)
  The physical placement of an audio accessory.
- [AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities.md)
  A set of capabilities that an audio accessory supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct)*