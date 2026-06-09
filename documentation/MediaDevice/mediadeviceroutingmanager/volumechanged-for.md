# volumeChanged(for:)

**Framework**: Media Device  
**Kind**: method

Notifies the system that the volume state has changed on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func volumeChanged(for device: MediaOutputDevice)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when the remote device’s volume level or mute state changes independently of system-initiated volume control calls. This is typically needed when:

- The device’s physical volume buttons are pressed
- The device’s volume is changed through its own interface or remote control
- Another application or service modifies the device’s volume
- The device automatically adjusts volume (for example, due to content normalization)

After calling this function, the system will query the current volume state by calling the appropriate getter based on the device’s [`volumeControl`](mediaoutputdevice/volumecontrol-swift.property.md):

- For [`MediaOutputDevice.VolumeControl.absolute`](mediaoutputdevice/volumecontrol-swift.enum/absolute.md) devices: [`volume(for:)`](mediadeviceextension/volume(for:).md) and/or [`isDeviceMuted(_:)`](mediadeviceextension/isdevicemuted(_:).md) will be called (if [`canMute`](mediaoutputdevice/canmute.md) is `true`)
- For [`MediaOutputDevice.VolumeControl.relative`](mediaoutputdevice/volumecontrol-swift.enum/relative.md) devices: [`isDeviceMuted(_:)`](mediadeviceextension/isdevicemuted(_:).md) will be called (if [`canMute`](mediaoutputdevice/canmute.md) is `true`)

> ❗ **Important**: Do not call this function in response to system-initiated volume changes (for example, when [`setVolume(_:for:)`](mediadeviceextension/setvolume(_:for:).md), [`changeVolume(by:for:)`](mediadeviceextension/changevolume(by:for:).md), or [`muteDevice(_:)`](mediadeviceextension/mutedevice(_:).md) are called). Only call it for external or device-initiated volume changes.

> **Note**: For device groups, call this function once for the group rather than for each individual member device, unless individual devices can have independent volume changes.

> **Note**: [`MediaOutputDevice.VolumeControl`](mediaoutputdevice/volumecontrol-swift.enum.md)

> **Note**: [`volume(for:)`](mediadeviceextension/volume(for:).md)

> **Note**: [`isDeviceMuted(_:)`](mediadeviceextension/isdevicemuted(_:).md)

## Parameters

- `device`: The device whose volume state has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/volumechanged(for:))*