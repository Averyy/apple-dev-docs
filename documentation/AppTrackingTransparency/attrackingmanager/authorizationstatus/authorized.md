# ATTrackingManager.AuthorizationStatus.authorized

**Framework**: App Tracking Transparency  
**Kind**: case

The value that returns if the user authorizes access to app-related data for tracking the user or the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case authorized
```

#### Discussion

This setting allows users to opt in or out of allowing apps to request user consent to access app-related data for tracking the user or the device. End users can revoke permission at any time through the Allow Apps to Request to Track privacy setting on the device.

## See Also

- [ATTrackingManager.AuthorizationStatus.denied](attrackingmanager/authorizationstatus/denied.md)
  The value that returns if the user denies authorization to access app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](attrackingmanager/authorizationstatus/notdetermined.md)
  The value that returns when the app can’t determine the user’s authorization status for access to app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.restricted](attrackingmanager/authorizationstatus/restricted.md)
  The value that returns if authorization to access app-related data for tracking the user or the device has a restricted status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus/authorized)*