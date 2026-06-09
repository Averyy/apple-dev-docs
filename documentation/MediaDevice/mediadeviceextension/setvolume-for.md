# setVolume(_:for:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Sets the volume level for the specified device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func setVolume(_ volume: Float, for device: MediaOutputDevice)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

For a group of devices, individual device volume changes should influence the group volume.

Called when a device supports [`MediaOutputDevice.VolumeControl.absolute`](mediaoutputdevice/volumecontrol-swift.enum/absolute.md).

#### Grouping

For a group of devices, all devices in the group must support [`MediaOutputDevice.VolumeControl.absolute`](mediaoutputdevice/volumecontrol-swift.enum/absolute.md).

## Parameters

- `volume`: The volume level to set, typically in the range 0.0 to 1.0.
- `device`: The device for which to set the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/setvolume(_:for:))*