# init(name:object:)

**Framework**: Foundation  
**Kind**: init

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

## Parameters

- `aName`: The name for the new notification. May not be  .
- `anObject`: The object for the new notification.

## See Also

- [func post(name: NSNotification.Name, object: Any?)](notificationcenter/post(name:object:).md)
  Creates a notification with a given name and sender and posts it to the notification center.
- [Notification Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
- [init?(coder: NSCoder)](nsnotification/init(coder:).md)
  Initializes a notification with the data from an unarchiver.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](nsnotification/init(name:object:userinfo:).md)
  Initializes a notification with a specified name, object, and user information.
- [NSNotification.Name](nsnotification/name-swift.struct.md)
  A structure that defines the name of a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/init(name:object:))*