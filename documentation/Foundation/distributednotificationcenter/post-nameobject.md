# post(name:object:)

**Framework**: Foundation  
**Kind**: method

Creates a notification, and posts it to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func post(name aName: NSNotification.Name, object anObject: String?)
```

#### Discussion

This method invokes [`postNotificationName(_:object:userInfo:deliverImmediately:)`](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md) with `userInfo:nil deliverImmediately:NO`.

## Parameters

- `aName`: Name of the notification to post. Must not be  .
- `anObject`: Sender of the notification. May be  .

## See Also

- [func post(name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?)](distributednotificationcenter/post(name:object:userinfo:).md)
  Creates a notification with information, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, options: DistributedNotificationCenter.Options)](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md)
  Creates a notification with information, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/post(name:object:))*