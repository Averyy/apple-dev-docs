# Notification

**Framework**: Foundation  
**Kind**: struct

A container for information broadcast through a notification center to all registered observers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Notification
```

## Topics

### Creating a Notification
- [init(name: Notification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](notification/init(name:object:userinfo:).md)
  Initializes a new notification.
- [Notification.Name](notification/name-swift.typealias.md)
  An alias for a type used to represent the name of a notification.
- [NSNotification.Name](nsnotification/name-swift.struct.md)
  A structure that defines the name of a notification.
### Getting Notification Information
- [var name: Notification.Name](notification/name-swift.property.md)
  A tag identifying the notification.
- [var object: Any?](notification/object.md)
  An object that the poster wishes to send to observers.
- [var userInfo: [AnyHashable : Any]?](notification/userinfo.md)
  Storage for values or objects related to this notification.
### Using Reference Types
- [class NSNotification](nsnotification.md)
  A container for information broadcast through a notification center to all registered observers.
### Operators
- [static func == (Notification, Notification) -> Bool](notification/==(_:_:).md)
  Compare two notifications for equality.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)

## See Also

- [class NotificationCenter](notificationcenter.md)
  A notification dispatch mechanism that enables the broadcast of information to registered observers.
- [class NotificationQueue](notificationqueue.md)
  A notification center buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notification)*