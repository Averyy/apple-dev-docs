# secondaryAudioSourceDeviceIdentifier

**Framework**: AudioAccessoryKit  
**Kind**: property  
**Role**: Instance Property

The Bluetooth address of the device providing the secondary source of audio.

**Availability**:
- iOS 26.4+

## Declaration

```swift
var secondaryAudioSourceDeviceIdentifier: Data?
```

## Discussion

If there’s only one device connected, set it as the primary device. If the accessory doesn’t support the [`audioSwitching`](../capabilities/audioswitching.md) capability, the value of this property is always `nil`.

## See Also

### Accessing configuration options
- [var deviceCapabilities: AccessoryControlDevice.Capabilities](./devicecapabilities.md)
  The capabilities the accessory supports.
- [var devicePlacement: AccessoryControlDevice.Placement?](./deviceplacement.md)
  The physical position of the accessory.
- [var primaryAudioSourceDeviceIdentifier: Data?](./primaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the primary source of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/secondaryaudiosourcedeviceidentifier)*