# foundDevice(_:)

**Framework**: Media Device  
**Kind**: method

Notifies the system of a new media device, so it can be included in device lists for users to select.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func foundDevice(_ device: MediaOutputDevice)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when a `MediaDeviceExtension` discovers a new device.

## Parameters

- `device`: The device that was discovered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/founddevice(_:))*