# lostDevice(_:)

**Framework**: Media Device  
**Kind**: method

Removes a device from the system’s device lists so users can no longer select it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func lostDevice(_ device: MediaOutputDevice)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when a previously discovered [`MediaOutputDevice`](mediaoutputdevice.md) can no longer be found.

## Parameters

- `device`: The device that is no longer available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/lostdevice(_:))*