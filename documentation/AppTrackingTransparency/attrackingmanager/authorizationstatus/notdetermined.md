# ATTrackingManager.AuthorizationStatus.notDetermined

**Framework**: App Tracking Transparency  
**Kind**: case

The value that returns when the app can’t determine the user’s authorization status for access to app-related data for tracking the user or the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case notDetermined
```

#### Discussion

> **Note**: If you call `ATTrackingManager.trackingAuthorizationStatus` in macOS, the result is always `ATTrackingManager.AuthorizationStatus.notDetermined`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus/notdetermined)*