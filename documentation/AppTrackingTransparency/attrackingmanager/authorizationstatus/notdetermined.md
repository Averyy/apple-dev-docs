# ATTrackingManager.AuthorizationStatus.notDetermined

**Framework**: App Tracking Transparency  
**Kind**: case

A value that indicates the person hasn’t responded to a tracking authorization request.

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

> **Note**: On macOS, [`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) always returns this value.

## See Also

- [ATTrackingManager.AuthorizationStatus.authorized](attrackingmanager/authorizationstatus/authorized.md)
  A value that indicates someone grants your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.denied](attrackingmanager/authorizationstatus/denied.md)
  A value that indicates someone denies your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.restricted](attrackingmanager/authorizationstatus/restricted.md)
  A value that indicates the system restricts tracking authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus/notdetermined)*