# init(coder:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a notification with the data from an unarchiver.

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
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating Notifications
- [convenience init(name: NSNotification.Name, object: Any?)](./init%28name,object%29.md)
  Returns a new notification object with a specified name and object.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./init%28name,object,userinfo%29.md)
  Initializes a notification with a specified name, object, and user information.
- [NSNotification.Name](./name-swift.struct.md)
  A structure that defines the name of a notification.
- [- init](./init.md)
  Initializes an empty notification.
- [+ notificationWithName:object:userInfo:](./notificationwithname_object_userinfo_.md)
  Returns a notification object with a specified name, object, and user information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/init(coder:))*