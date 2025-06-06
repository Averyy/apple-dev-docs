# NotificationQueue

**Framework**: Foundation  
**Kind**: class

A notification center buffer.

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
class NotificationQueue
```

#### Overview

Whereas a notification center distributes notifications when posted, notifications placed into the queue can be delayed until the end of the current pass through the run loop or until the run loop is idle. Duplicate notifications can be coalesced so that only one notification is sent although multiple notifications are posted.

A notification queue maintains notifications in first in, first out (FIFO) order. When a notification moves to the front of the queue, the queue posts it to the notification center, which in turn dispatches the notification to all objects registered as observers.

Every thread has a default notification queue, which is associated with the default notification center for the process. You can create your own notification queues and have multiple queues per center and thread.

## Topics

### Creating Notification Queues
- [init(notificationCenter: NotificationCenter)](notificationqueue/init(notificationcenter:).md)
  Initializes and returns a notification queue for the specified notification center.
### Getting the Default Queue
- [class var `default`: NotificationQueue](notificationqueue/default.md)
  Returns the default notification queue for the current thread.
### Managing Notifications
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:).md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle)](notificationqueue/enqueue(_:postingstyle:).md)
  Adds a notification to the notification queue with a specified posting style.
- [func dequeueNotifications(matching: Notification, coalesceMask: Int)](notificationqueue/dequeuenotifications(matching:coalescemask:).md)
  Removes all notifications from the queue that match a provided notification using provided matching criteria.
### Constants
- [NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing.md)
  The constants that specify how notifications are coalesced.
- [NotificationQueue.PostingStyle](notificationqueue/postingstyle.md)
  The constants that specify when notifications are posted.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct Notification](notification.md)
  A container for information broadcast through a notification center to all registered observers.
- [class NotificationCenter](notificationcenter.md)
  A notification dispatch mechanism that enables the broadcast of information to registered observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue)*