# ATTrackingManager.AuthorizationStatus

**Framework**: App Tracking Transparency  
**Kind**: enum

A type that represents the tracking-authorization status of an app.

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

[`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) returns this type, and [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md) passes an instance of this type to your completion handler when a person answers the system alert.

## Topics

### Determining the status
- [ATTrackingManager.AuthorizationStatus.authorized](attrackingmanager/authorizationstatus/authorized.md)
  A value that indicates someone grants your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.denied](attrackingmanager/authorizationstatus/denied.md)
  A value that indicates someone denies your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](attrackingmanager/authorizationstatus/notdetermined.md)
  A value that indicates the person hasn’t responded to a tracking authorization request.
- [ATTrackingManager.AuthorizationStatus.restricted](attrackingmanager/authorizationstatus/restricted.md)
  A value that indicates the system restricts tracking authorization.
### Creating a status
- [init?(rawValue: UInt)](attrackingmanager/authorizationstatus/init(rawvalue:).md)
  Initializes an authorization status.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus](attrackingmanager/trackingauthorizationstatus.md)
  A value that indicates the status of the app’s tracking authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus)*