# secondaryAudioSourceDeviceIdentifier

**Framework**: AudioAccessoryKit  
**Kind**: property

The Bluetooth address of the device providing the secondary source of audio.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var secondaryAudioSourceDeviceIdentifier: Data?
```

#### Discussion

If there’s only one device connected, set it as the primary device. If the accessory doesn’t support the `.audioSwitching` capability, the value of this property is always `nil`.

## See Also

- [var deviceCapabilities: AccessoryControlDevice.Capabilities](accessorycontroldevice/configuration-swift.struct/devicecapabilities.md)
  The capabilities the accessory supports.
- [var devicePlacement: AccessoryControlDevice.Placement?](accessorycontroldevice/configuration-swift.struct/deviceplacement.md)
  The physical position of the accessory.
- [var primaryAudioSourceDeviceIdentifier: Data?](accessorycontroldevice/configuration-swift.struct/primaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the primary source of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/secondaryaudiosourcedeviceidentifier)*