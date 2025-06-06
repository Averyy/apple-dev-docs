# dispatchQueue

**Framework**: Exposure Notification  
**Kind**: property

The dispatch queue on which to invoke handlers.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var dispatchQueue: dispatch_queue_t { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

The default is the main queue.

## See Also

- [var exposureNotificationStatus: ENStatus](enmanager/exposurenotificationstatus.md)
  A property that indicates the status of exposure notifications.
- [var exposureNotificationEnabled: Bool](enmanager/exposurenotificationenabled.md)
  A property that indicates that a user enabled exposure notification.
- [class var authorizationStatus: ENAuthorizationStatus](enmanager/authorizationstatus.md)
  A property that reports the current authorization status of the app, and never prompts the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/dispatchqueue)*