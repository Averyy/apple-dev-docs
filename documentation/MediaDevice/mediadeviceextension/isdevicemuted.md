# isDeviceMuted(_:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Gets the current mute state for the specified device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func isDeviceMuted(_ device: MediaOutputDevice) -> Bool
```

#### Return Value

`true` if the device is muted, `false` otherwise.

#### Discussion

Called when a device reports `true` for [`canMute`](mediaoutputdevice/canmute.md).

#### Grouping

For a group of devices, all devices in the group must report `true` for [`canMute`](mediaoutputdevice/canmute.md).

## Parameters

- `device`: The device for which to check the mute state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/isdevicemuted(_:))*