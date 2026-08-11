# trackingAuthorizationStatus

**Framework**: App Tracking Transparency  
**Kind**: property

The authorization status that is current for the calling application.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus { get }
```

#### Return Value

Information about your application’s tracking authorization status. Users are able to grant or deny developers tracking privileges on a per-app basis. Application developers must call `requestTrackingAuthorizationWithCompletionHandler:` for the ability to track users.

#### Discussion

If the user has not yet been prompted to approve access, the return value will either be `ATTrackingManagerAuthorizationStatusNotDetermined`, or `ATTrackingManagerAuthorizationStatusRestricted` if this value is managed. Once the user has been prompted, the return value will be either `ATTrackingManagerAuthorizationStatusDenied` or `ATTrackingManagerAuthorizationStatusAuthorized`.

Use the [`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) property to check authorization status.

## See Also

- [ATTrackingManager.AuthorizationStatus](attrackingmanager/authorizationstatus.md)
  The status values for app tracking authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/trackingauthorizationstatus)*