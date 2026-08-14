# primaryAudioSourceDeviceIdentifier

**Framework**: AudioAccessoryKit  
**Kind**: property

The Bluetooth address of the device providing the primary source of audio.

**Availability**:
- iOS 26.4+

## Declaration

```swift
var primaryAudioSourceDeviceIdentifier: Data?
```

#### Discussion

If the accessory is connected to only one device, set it as the primary device. If the accessory doesn’t support the [`audioSwitching`](accessorycontroldevice/capabilities/audioswitching.md) capability, the value of this property is always `nil`.

## See Also

- [var deviceCapabilities: AccessoryControlDevice.Capabilities](accessorycontroldevice/configuration-swift.struct/devicecapabilities.md)
  The capabilities the accessory supports.
- [var devicePlacement: AccessoryControlDevice.Placement?](accessorycontroldevice/configuration-swift.struct/deviceplacement.md)
  The physical position of the accessory.
- [var secondaryAudioSourceDeviceIdentifier: Data?](accessorycontroldevice/configuration-swift.struct/secondaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the secondary source of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/primaryaudiosourcedeviceidentifier)*