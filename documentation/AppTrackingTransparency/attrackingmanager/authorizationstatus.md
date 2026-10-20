# ATTrackingManager.AuthorizationStatus

**Framework**: App Tracking Transparency  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ATTrackingManagerAuthorizationStatus : NSUInteger;
```

#### Overview

[`trackingAuthorizationStatus`](./trackingauthorizationstatus.md) returns this type, and [`requestTrackingAuthorization(completionHandler:)`](./requesttrackingauthorization%28completionhandler%29.md) passes an instance of this type to your completion handler when a person answers the system alert.

## Topics

### Determining the status
- [ATTrackingManager.AuthorizationStatus.authorized](./authorizationstatus/authorized.md)
  A value that indicates someone grants your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.denied](./authorizationstatus/denied.md)
  A value that indicates someone denies your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](./authorizationstatus/notdetermined.md)
  A value that indicates the person hasn’t responded to a tracking authorization request.
- [ATTrackingManager.AuthorizationStatus.restricted](./authorizationstatus/restricted.md)
  A value that indicates the system restricts tracking authorization.
### Creating a status
- [init?(rawValue: UInt)](./authorizationstatus/init%28rawvalue%29.md)
  Initializes an authorization status.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Authorization status and results
- [class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus](./trackingauthorizationstatus.md)
  A value that indicates the status of the app’s tracking authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus)*