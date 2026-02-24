# devicePlacement

**Framework**: AudioAccessoryKit  
**Kind**: property

The physical position of the accessory.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var devicePlacement: AccessoryControlDevice.Placement?
```

## Mentions

- [Supporting automatic audio switching for third-party accessories](supporting-automatic-audio-switching.md)

#### Discussion

Update this property when your accessory detects a change in its position.

## See Also

- [var deviceCapabilities: AccessoryControlDevice.Capabilities](accessorycontroldevice/configuration-swift.struct/devicecapabilities.md)
  The capabilities the accessory supports.
- [var primaryAudioSourceDeviceIdentifier: Data?](accessorycontroldevice/configuration-swift.struct/primaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the primary source of audio.
- [var secondaryAudioSourceDeviceIdentifier: Data?](accessorycontroldevice/configuration-swift.struct/secondaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the secondary source of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/deviceplacement)*