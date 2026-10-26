# notificationWithName:object:userInfo:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a notification object with a specified name, object, and user information.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) notificationWithName:(NSNotificationName) aName object:(id) anObject userInfo:(NSDictionary *) aUserInfo;
```

## Parameters

- `aName`: The name for the new notification. May not be `nil`.
- `anObject`: The object for the new notification.
- `aUserInfo`: The user information dictionary for the new notification. May be `nil`.

## See Also

### Related Documentation
- [func post(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](../notificationcenter/post%28name,object,userinfo%29.md)
  Creates a notification with a given name, sender, and information and posts it to the notification center.
### Creating Notifications
- [- init](./init.md)
  Initializes an empty notification.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](./init%28name,object%29.md)
  Returns a new notification object with a specified name and object.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./init%28name,object,userinfo%29.md)
  Initializes a notification with a specified name, object, and user information.
- [NSNotification.Name](./name-swift.struct.md)
  A structure that defines the name of a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/notificationwithname:object:userinfo:)*