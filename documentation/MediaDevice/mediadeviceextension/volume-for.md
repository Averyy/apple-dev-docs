# volume(for:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Gets the current volume level for the specified device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func volume(for device: MediaOutputDevice) -> Float
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Return Value

The current volume level in the range 0.0 to 1.0.

#### Discussion

Called when a device supports [`MediaOutputDevice.VolumeControl.absolute`](mediaoutputdevice/volumecontrol-swift.enum/absolute.md).

#### Grouping

For a group of devices, all devices in the group must support [`MediaOutputDevice.VolumeControl.absolute`](mediaoutputdevice/volumecontrol-swift.enum/absolute.md).

## Parameters

- `device`: The device for which to get the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/volume(for:))*