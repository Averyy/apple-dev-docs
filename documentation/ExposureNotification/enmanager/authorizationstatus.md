# authorizationStatus

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Type Property

A property that reports the current authorization status of the app, and never prompts the user.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
class var authorizationStatus: ENAuthorizationStatus { get }
```

```objc
@property (class, nonatomic, assign, readonly) ENAuthorizationStatus authorizationStatus;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

This property can be used by the app to preflight authorization in order to determine if the user may be prompted.

## See Also

### Configuring the Manager
- [var exposureNotificationStatus: ENStatus](./exposurenotificationstatus.md)
  A property that indicates the status of exposure notifications.
- [var exposureNotificationEnabled: Bool](./exposurenotificationenabled.md)
  A property that indicates that a user enabled exposure notification.
- [var dispatchQueue: dispatch_queue_t](./dispatchqueue.md)
  The dispatch queue on which to invoke handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/authorizationstatus)*