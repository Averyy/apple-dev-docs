# AccessoryControlDevice.Configuration

**Framework**: AudioAccessoryKit  
**Kind**: struct  
**Role**: Structure

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
- [init(devicePlacement: AccessoryControlDevice.Placement?, deviceCapabilities: AccessoryControlDevice.Capabilities, primaryAudioSourceDeviceIdentifier: Data?, secondaryAudioSourceDeviceIdentifier: Data?)](./configuration-swift.struct/init%28deviceplacement,devicecapabilities,primaryaudiosourcedeviceidentifier,secondaryaudiosourcedeviceidentifier%29.md)
  Creates an audio accessory configuration.
### Accessing configuration options
- [var deviceCapabilities: AccessoryControlDevice.Capabilities](./configuration-swift.struct/devicecapabilities.md)
  The capabilities the accessory supports.
- [var devicePlacement: AccessoryControlDevice.Placement?](./configuration-swift.struct/deviceplacement.md)
  The physical position of the accessory.
- [var primaryAudioSourceDeviceIdentifier: Data?](./configuration-swift.struct/primaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the primary source of audio.
- [var secondaryAudioSourceDeviceIdentifier: Data?](./configuration-swift.struct/secondaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the secondary source of audio.
### Initializers
- [init(devicePlacement: AccessoryControlDevice.Placement?, deviceCapabilities: AccessoryControlDevice.Capabilities, primaryAudioSourceDeviceIdentifier: Data?, secondaryAudioSourceDeviceIdentifier: Data?, spatialExtensionDescription: AudioComponentDescription?)](./configuration-swift.struct/init%28deviceplacement,devicecapabilities,primaryaudiosourcedeviceidentifier,secondaryaudiosourcedeviceidentifier,spatialextensiondescription%29.md)
  Creates a new device configuration with spatial audio support.
### Instance Properties
- [var spatialExtensionDescription: AudioComponentDescription?](./configuration-swift.struct/spatialextensiondescription.md)
  The spatial audio component description.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Device characteristics
- [AccessoryControlDevice.Placement](./placement.md)
  The physical placement of an audio accessory.
- [AccessoryControlDevice.Capabilities](./capabilities.md)
  A set of capabilities that an audio accessory supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct)*