# failedToActivateDevice(_:session:error:)

**Framework**: Media Device  
**Kind**: method

Reports a device activation failure to the system so it can inform the user and clean up the session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func failedToActivateDevice(_ device: MediaOutputDevice, session: MediaOutputSession, error: MediaDeviceError)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when activation has failed for a device.

## Parameters

- `device`: The device that activation failed for.
- `session`: The session associated with the activation.
- `error`: The error that occurred during activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/failedtoactivatedevice(_:session:error:))*