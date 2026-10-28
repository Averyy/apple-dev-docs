# dispatchQueue

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which to invoke handlers.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var dispatchQueue: dispatch_queue_t { get set }
```

```objc
@property (nonatomic, strong, readwrite) dispatch_queue_t dispatchQueue;
```

## Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

The default is the main queue.

## See Also

### Configuring the Manager
- [var exposureNotificationStatus: ENStatus](./exposurenotificationstatus.md)
  A property that indicates the status of exposure notifications.
- [var exposureNotificationEnabled: Bool](./exposurenotificationenabled.md)
  A property that indicates that a user enabled exposure notification.
- [class var authorizationStatus: ENAuthorizationStatus](./authorizationstatus.md)
  A property that reports the current authorization status of the app, and never prompts the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/dispatchqueue)*