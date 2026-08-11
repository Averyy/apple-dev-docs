# ATTrackingManager.AuthorizationStatus

**Framework**: App Tracking Transparency  
**Kind**: enum

The status values for app tracking authorization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum AuthorizationStatus
```

#### Overview

After a device receives an authorization request to approve access to app-related data that can be used for tracking the user or the device, the returned value is either:

- [`ATTrackingManager.AuthorizationStatus.authorized`](attrackingmanager/authorizationstatus/authorized.md), or
- [`ATTrackingManager.AuthorizationStatus.denied`](attrackingmanager/authorizationstatus/denied.md).

Before a device receives an authorization request to approve access to app-related data that can be used for tracking the user or the device, the returned value is: [`ATTrackingManager.AuthorizationStatus.notDetermined`](attrackingmanager/authorizationstatus/notdetermined.md).

If authorization to use app tracking data is restricted, the value is: [`ATTrackingManager.AuthorizationStatus.restricted`](attrackingmanager/authorizationstatus/restricted.md).

## Topics

### Cases
- [ATTrackingManager.AuthorizationStatus.authorized](attrackingmanager/authorizationstatus/authorized.md)
  The value that returns if the user authorizes access to app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.denied](attrackingmanager/authorizationstatus/denied.md)
  The value that returns if the user denies authorization to access app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](attrackingmanager/authorizationstatus/notdetermined.md)
  The value that returns when the app can’t determine the user’s authorization status for access to app-related data for tracking the user or the device.
- [ATTrackingManager.AuthorizationStatus.restricted](attrackingmanager/authorizationstatus/restricted.md)
  The value that returns if authorization to access app-related data for tracking the user or the device has a restricted status.
### Initializers
- [init?(rawValue: UInt)](attrackingmanager/authorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus](attrackingmanager/trackingauthorizationstatus.md)
  The authorization status that is current for the calling application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus)*