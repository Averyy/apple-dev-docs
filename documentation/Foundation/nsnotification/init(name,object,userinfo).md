# init(name:object:userInfo:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a notification with a specified name, object, and user information.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]? = nil)
```

```objc
- (instancetype) initWithName:(NSNotificationName) name object:(id) object userInfo:(NSDictionary *) userInfo;
```

## Parameters

- `name`: The name for the new notification. May not be `nil`.
- `object`: The object for the new notification.
- `userInfo`: The user information dictionary for the new notification. May be `nil`.

## See Also

### Creating Notifications
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](./init%28name,object%29.md)
  Returns a new notification object with a specified name and object.
- [NSNotification.Name](./name-swift.struct.md)
  A structure that defines the name of a notification.
- [- init](./init.md)
  Initializes an empty notification.
- [+ notificationWithName:object:userInfo:](./notificationwithname_object_userinfo_.md)
  Returns a notification object with a specified name, object, and user information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/init(name:object:userinfo:))*