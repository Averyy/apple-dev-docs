# sessionFailed(_:error:)

**Framework**: Media Device  
**Kind**: method

Reports an unrecoverable session error to the system so it can end the session and inform the user.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func sessionFailed(_ session: MediaOutputSession, error: MediaDeviceError)
```

#### Discussion

Call this function when an unrecoverable error is encountered during the session.

## Parameters

- `session`: The session associated with the failure.
- `error`: The error that occurred during the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/sessionfailed(_:error:))*