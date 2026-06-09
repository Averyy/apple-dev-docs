# changeVolume(by:for:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Changes the volume by a specified number of increments for the specified device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func changeVolume(by increments: Int, for device: MediaOutputDevice)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

For a group of devices, individual device volume changes should influence the group volume.

Called when a device supports [`MediaOutputDevice.VolumeControl.relative`](mediaoutputdevice/volumecontrol-swift.enum/relative.md).

#### Grouping

For a group of devices, all devices in the group must support [`MediaOutputDevice.VolumeControl.relative`](mediaoutputdevice/volumecontrol-swift.enum/relative.md).

## Parameters

- `increments`: The number of volume increments to increase or decrease by.
- `device`: The device for which to change the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/changevolume(by:for:))*