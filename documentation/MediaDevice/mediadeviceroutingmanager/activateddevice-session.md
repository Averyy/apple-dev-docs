# activatedDevice(_:session:)

**Framework**: Media Device  
**Kind**: method

Notifies the system that a device has been successfully activated and is ready for use.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func activatedDevice(_ device: MediaOutputDevice, session: MediaOutputSession)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when activation has completed for a device.

## Parameters

- `device`: The device that activation completed for.
- `session`: The session associated with the activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/activateddevice(_:session:))*