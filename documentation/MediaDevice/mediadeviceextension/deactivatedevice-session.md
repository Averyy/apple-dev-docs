# deactivateDevice(_:session:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when the user deactivates a device via a user interface.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func deactivateDevice(_ device: MediaOutputDevice, session: MediaOutputSession)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Grouping

The device should be removed from its modifiable group. [`updateDevices(_:)`](mediadeviceroutingmanager/updatedevices(_:).md) should be called to update the state of group information.

## Parameters

- `device`: The device to deactivate.
- `session`: The session associated with the deactivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/deactivatedevice(_:session:))*