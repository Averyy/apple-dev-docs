# init(name:object:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a new notification object with a specified name and object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(name aName: NSNotification.Name, object anObject: Any?)
```

```objc
+ (instancetype) notificationWithName:(NSNotificationName) aName object:(id) anObject;
```

## Parameters

- `aName`: The name for the new notification. May not be `nil`.
- `anObject`: The object for the new notification.

## See Also

### Related Documentation
- [func post(name: NSNotification.Name, object: Any?)](../notificationcenter/post%28name,object%29.md)
  Creates a notification with a given name and sender and posts it to the notification center.
- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
### Creating Notifications
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a notification with the data from an unarchiver.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./init%28name,object,userinfo%29.md)
  Initializes a notification with a specified name, object, and user information.
- [NSNotification.Name](./name-swift.struct.md)
  A structure that defines the name of a notification.
- [- init](./init.md)
  Initializes an empty notification.
- [+ notificationWithName:object:userInfo:](./notificationwithname_object_userinfo_.md)
  Returns a notification object with a specified name, object, and user information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/init(name:object:))*