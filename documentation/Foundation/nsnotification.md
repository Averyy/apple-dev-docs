# NSNotification

**Framework**: Foundation  
**Kind**: class

A container for information broadcast through a notification center to all registered observers.

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
class NSNotification
```

#### Overview

In Swift, this object bridges to [`Notification`](notification.md); use [`NSNotification`](nsnotification.md) when you need reference semantics or other Foundation-specific behavior.

A notification contains a name, an object, and an optional dictionary, and is broadcast to by instances of  [`NotificationCenter`](notificationcenter.md) or [`DistributedNotificationCenter`](distributednotificationcenter.md). The name is a tag identifying the notification. The object is any object that the poster of the notification wants to send to observers of that notification (typically, the object posting the notification). The dictionary stores other related objects, if any. [`NSNotification`](nsnotification.md) objects are immutable.

You don’t usually create your own notifications directly, but instead call the [`NotificationCenter`](notificationcenter.md) methods [`post(name:object:)`](notificationcenter/post(name:object:).md) and [`post(name:object:userInfo:)`](notificationcenter/post(name:object:userinfo:).md).

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Notification`](notification.md) structure, which bridges to the [`NSNotification`](nsnotification.md) class. For more information about value types, see [`Working with Foundation Types`](https://developer.apple.com/documentation/swift/working-with-foundation-types).

##### Object Comparison

The objects of a notification are compared using pointer equality for local notifications. Distributed notifications use strings as their objects, and those strings are compared using [`isEqual(_:)`](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isequal(_:)), because pointer equality doesn’t make sense across process boundaries.

##### Creating Subclasses

You can subclass [`NSNotification`](nsnotification.md) to contain information in addition to the notification name, object, and dictionary. This extra data must be agreed upon between notifiers and observers.

[`NotificationCenter`](notificationcenter.md) is a class cluster with no instance variables. As such, you must subclass [`NSNotification`](nsnotification.md) and override the primitive methods [`name`](nsnotification/name-swift.property.md), [`object`](nsnotification/object.md), and [`userInfo`](nsnotification/userinfo.md). You can choose any designated initializer you like, but be sure that your initializer does not call [`init`](nsnotification/init.md) on `super` ([`NSNotification`](nsnotification.md) is not meant to be instantiated directly, and its `init` method raises an exception).

## Topics

### Creating Notifications
- [init?(coder: NSCoder)](nsnotification/init(coder:).md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](nsnotification/init(name:object:).md)
  Returns a new notification object with a specified name and object.
- [init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](nsnotification/init(name:object:userinfo:).md)
  Initializes a notification with a specified name, object, and user information.
- [NSNotification.Name](nsnotification/name-swift.struct.md)
  A structure that defines the name of a notification.
### Getting Notification Information
- [var name: NSNotification.Name](nsnotification/name-swift.property.md)
  The name of the notification.
- [var object: Any?](nsnotification/object.md)
  The object associated with the notification.
- [var userInfo: [AnyHashable : Any]?](nsnotification/userinfo.md)
  The user information dictionary associated with the notification.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Notification Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification)*