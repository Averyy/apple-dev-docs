# post(name:object:userInfo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a notification with information, and posts it to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func post(name aName: NSNotification.Name, object anObject: String?, userInfo aUserInfo: [AnyHashable : Any]? = nil)
```

```objc
- (void) postNotificationName:(NSNotificationName) aName object:(NSString *) anObject userInfo:(NSDictionary *) aUserInfo;
```

## Discussion

This method invokes [`postNotificationName(_:object:userInfo:deliverImmediately:)`](./postnotificationname%28_,object,userinfo,deliverimmediately%29.md) with `deliverImmediately:NO`.

## Parameters

- `aName`: Name of the notification to post. Must not be `nil`.
- `anObject`: Sender of the notification. May be `nil`.
- `aUserInfo`: Dictionary containing additional information. May be `nil`.

  > ❗ **Important**:  Sandboxed apps can send notifications only if they do not contain a dictionary. If the sending application is in an App Sandbox, `notificationInfo` *must* be `nil`.

## See Also

### Posting Notifications
- [func post(name: NSNotification.Name, object: String?)](./post%28name,object%29.md)
  Creates a notification, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](./postnotificationname%28_,object,userinfo,deliverimmediately%29.md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, options: DistributedNotificationCenter.Options)](./postnotificationname%28_,object,userinfo,options%29.md)
  Creates a notification with information, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/post(name:object:userinfo:))*