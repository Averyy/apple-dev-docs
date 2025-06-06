# exposureNotificationStatus

**Framework**: Exposure Notification  
**Kind**: property

A property that indicates the status of exposure notifications.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var exposureNotificationStatus: ENStatus { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

You can use key value observing to monitor for changes. The value of this property will be [`ENStatus.unknown`](enstatus/unknown.md) until [`activate(completionHandler:)`](enmanager/activate(completionhandler:).md) completes successfully.

This status can be affected by the user disabling exposure notifications, disabling bluetooth, or restricting the feature through parental controls.

## See Also

- [var exposureNotificationEnabled: Bool](enmanager/exposurenotificationenabled.md)
  A property that indicates that a user enabled exposure notification.
- [class var authorizationStatus: ENAuthorizationStatus](enmanager/authorizationstatus.md)
  A property that reports the current authorization status of the app, and never prompts the user.
- [var dispatchQueue: dispatch_queue_t](enmanager/dispatchqueue.md)
  The dispatch queue on which to invoke handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/exposurenotificationstatus)*