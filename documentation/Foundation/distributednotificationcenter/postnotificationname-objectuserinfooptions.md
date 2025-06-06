# postNotificationName(_:object:userInfo:options:)

**Framework**: Foundation  
**Kind**: method

Creates a notification with information, and posts it to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func postNotificationName(_ name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]? = nil, options: DistributedNotificationCenter.Options = [])
```

#### Discussion

The `userInfo` dictionary is serialized as a property list, so it can be passed to another task. In the receiving task, it is deserialized back into a dictionary. This serialization imposes some restrictions on the objects that can be placed in the `userInfo` dictionary. See XML Property Lists for details.

## Parameters

- `name`: Name of the notification to post. Must not be  .
- `object`: Sender of the notification. May be  .
- `userInfo`: Dictionary containing additional information. May be  .
- `options`: Specifies how the notification is posted to the task and when to deliver it to its observers. See   for details.

## See Also

- [func post(name: NSNotification.Name, object: String?)](distributednotificationcenter/post(name:object:).md)
  Creates a notification, and posts it to the receiver.
- [func post(name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?)](distributednotificationcenter/post(name:object:userinfo:).md)
  Creates a notification with information, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/postnotificationname(_:object:userinfo:options:))*