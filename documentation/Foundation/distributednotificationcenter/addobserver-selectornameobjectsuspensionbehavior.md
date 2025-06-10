# addObserver(_:selector:name:object:suspensionBehavior:)

**Framework**: Foundation  
**Kind**: method

Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addObserver(_ observer: Any, selector: Selector, name: NSNotification.Name?, object: String?, suspensionBehavior: DistributedNotificationCenter.SuspensionBehavior)
```

#### Discussion

The receiver does not retain `notificationObserver`. Therefore, you should always send `NotificationCenter/removeObserver(_:)` or [`removeObserver(_:name:object:)`](distributednotificationcenter/removeobserver(_:name:object:).md) to the receiver before releasing `notificationObserver`.

## Parameters

- `observer`: Object registering as an observer. Must not be  .
- `selector`: Selector that specifies the message the receiver sends   to notify it of the notification posting. Must not be  .
- `name`: The name of the notification for which to register the observer; that is, only notifications with this name are delivered to the observer. When  , the notification center doesn’t use a notification’s name to decide whether to deliver it to the observer.
- `object`: The object whose notifications the observer wants to receive; that is, only notifications sent by this sender are delivered to the observer. When  , the notification center doesn’t use a notification’s sender to decide whether to deliver it to the observer.
- `suspensionBehavior`: Notification posting behavior when notification delivery is suspended.

## See Also

- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: String?)](distributednotificationcenter/addobserver(_:selector:name:object:).md)
  Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.
- [func removeObserver(Any, name: NSNotification.Name?, object: String?)](distributednotificationcenter/removeobserver(_:name:object:).md)
  Removes matching entries from the receiver’s dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/addobserver(_:selector:name:object:suspensionbehavior:))*