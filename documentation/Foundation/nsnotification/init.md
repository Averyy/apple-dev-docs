# init

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes an empty notification.

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
- (instancetype) init;
```

## See Also

### Creating Notifications
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](./init%28name,object%29.md)
  Returns a new notification object with a specified name and object.
- [+ notificationWithName:object:userInfo:](./notificationwithname_object_userinfo_.md)
  Returns a notification object with a specified name, object, and user information.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./init%28name,object,userinfo%29.md)
  Initializes a notification with a specified name, object, and user information.
- [NSNotification.Name](./name-swift.struct.md)
  A structure that defines the name of a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/init)*