# ATTrackingManager.AuthorizationStatus.restricted

**Framework**: App Tracking Transparency  
**Kind**: case

The value that returns if authorization to access app-related data for tracking the user or the device has a restricted status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case restricted
```

#### Discussion

A restricted condition means the device does not prompt for tracking authorization when [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md) is called, nor is it displayed when the [`NSUserTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription) is triggered. Also, on restricted devices, the Allow Apps To Request To Track setting is disabled and cannot be changed. This setting allows users to opt in or out of allowing apps to request user consent to access app-related data that can be used for tracking the user or the device.

## See Also

- [ATTrackingManager.AuthorizationStatus.authorized](attrackingmanager/authorizationstatus/authorized.md)
  The value that returns if the user authorizes access to app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.denied](attrackingmanager/authorizationstatus/denied.md)
  The value that returns if the user denies authorization to access app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](attrackingmanager/authorizationstatus/notdetermined.md)
  The value that returns when the app can’t determine the user’s authorization status for access to app-related data for tracking the user or the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus/restricted)*