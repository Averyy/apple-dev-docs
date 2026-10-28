# devicePlacement

**Framework**: AudioAccessoryKit  
**Kind**: property  
**Role**: Instance Property

The physical position of the accessory.

**Availability**:
- iOS 26.4+

## Declaration

```swift
var devicePlacement: AccessoryControlDevice.Placement?
```

## Mentions

- [Supporting automatic audio switching for third-party accessories](../../supporting-automatic-audio-switching.md)

## Discussion

Update this property when your accessory detects a change in its position. If the accessory doesn’t support the [`placement`](../capabilities/placement.md) capability, the value of this property is always `nil`.

## See Also

### Accessing configuration options
- [var deviceCapabilities: AccessoryControlDevice.Capabilities](./devicecapabilities.md)
  The capabilities the accessory supports.
- [var primaryAudioSourceDeviceIdentifier: Data?](./primaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the primary source of audio.
- [var secondaryAudioSourceDeviceIdentifier: Data?](./secondaryaudiosourcedeviceidentifier.md)
  The Bluetooth address of the device providing the secondary source of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/deviceplacement)*