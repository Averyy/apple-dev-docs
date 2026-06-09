# muteDevice(_:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Mutes the audio output for the specified device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func muteDevice(_ device: MediaOutputDevice)
```

#### Discussion

Called when a device reports `true` for [`canMute`](mediaoutputdevice/canmute.md).

#### Grouping

For a group of devices, individual device volume mute should influence the group mute. For a group of devices, all devices in the group must report `true` for [`canMute`](mediaoutputdevice/canmute.md).

## Parameters

- `device`: The device to mute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/mutedevice(_:))*