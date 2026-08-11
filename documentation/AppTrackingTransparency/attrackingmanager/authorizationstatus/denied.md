# ATTrackingManager.AuthorizationStatus.denied

**Framework**: App Tracking Transparency  
**Kind**: case

The value that returns if the user denies authorization to access app-related data for tracking the user or the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case denied
```

#### Discussion

The end user has denied the authorization request to access app-related data that can be used for tracking the user or the device.

## See Also

- [ATTrackingManager.AuthorizationStatus.authorized](attrackingmanager/authorizationstatus/authorized.md)
  The value that returns if the user authorizes access to app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](attrackingmanager/authorizationstatus/notdetermined.md)
  The value that returns when the app can’t determine the user’s authorization status for access to app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.restricted](attrackingmanager/authorizationstatus/restricted.md)
  The value that returns if authorization to access app-related data for tracking the user or the device has a restricted status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus/denied)*