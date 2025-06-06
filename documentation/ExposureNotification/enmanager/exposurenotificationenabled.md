# exposureNotificationEnabled

**Framework**: Exposure Notification  
**Kind**: property

A property that indicates that a user enabled exposure notification.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var exposureNotificationEnabled: Bool { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

You can use key value observing to monitor for changes. The value of this property will be `NO` until [`activate(completionHandler:)`](enmanager/activate(completionhandler:).md) completes successfully.

Note that even if the user enables exposure notifications, they may be inactive for other reasons, such as if the user turns off Bluetooth service. The [`exposureNotificationStatus`](enmanager/exposurenotificationstatus.md) property can be monitored for the status of exposure notifications.

## See Also

- [var exposureNotificationStatus: ENStatus](enmanager/exposurenotificationstatus.md)
  A property that indicates the status of exposure notifications.
- [class var authorizationStatus: ENAuthorizationStatus](enmanager/authorizationstatus.md)
  A property that reports the current authorization status of the app, and never prompts the user.
- [var dispatchQueue: dispatch_queue_t](enmanager/dispatchqueue.md)
  The dispatch queue on which to invoke handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/exposurenotificationenabled)*