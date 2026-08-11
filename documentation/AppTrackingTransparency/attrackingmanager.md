# ATTrackingManager

**Framework**: App Tracking Transparency  
**Kind**: class

A class that provides a tracking authorization request and the tracking authorization status of the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ATTrackingManager
```

## Topics

### Requesting Authorization
- [class func requestTrackingAuthorization(completionHandler: (ATTrackingManager.AuthorizationStatus) -> Void)](attrackingmanager/requesttrackingauthorization(completionhandler:).md)
  The request for user authorization to access app-related data.
### Determining Tracking Authorization Status
- [class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus](attrackingmanager/trackingauthorizationstatus.md)
  The authorization status that is current for the calling application.
- [ATTrackingManager.AuthorizationStatus](attrackingmanager/authorizationstatus.md)
  The status values for app tracking authorization.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager)*