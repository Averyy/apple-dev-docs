# openApplication(for:)

**Framework**: LockedCameraCapture  
**Kind**: method

Initiates a request to open the extension’s containing app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
final func openApplication(for userActivity: NSUserActivity) async throws
```

#### Discussion

The system requests authentication before opening the app, if needed.

## Parameters

- `userActivity`: An   that contains relevant information   to benefit from universal link support. Use the    activity type to indicate when the app   launches from a locked camera capture extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession/openapplication(for:))*