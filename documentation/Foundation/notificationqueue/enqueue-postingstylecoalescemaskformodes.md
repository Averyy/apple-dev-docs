# enqueue(_:postingStyle:coalesceMask:forModes:)

**Framework**: Foundation  
**Kind**: method

Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.

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
func enqueue(_ notification: Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes modes: [RunLoop.Mode]?)
```

## Parameters

- `notification`: The notification to add to the queue.
- `postingStyle`: The posting style for the notification. The posting style indicates when the notification queue should post the notification to its notification center.
- `coalesceMask`: A mask indicating what criteria to use when matching attributes of   to attributes of notifications in the queue. The mask is created by combining any of the constants  ,  , and  .
- `modes`: This parameter may be  , in which case it defaults to  .

## See Also

- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle)](notificationqueue/enqueue(_:postingstyle:).md)
  Adds a notification to the notification queue with a specified posting style.
- [func dequeueNotifications(matching: Notification, coalesceMask: Int)](notificationqueue/dequeuenotifications(matching:coalescemask:).md)
  Removes all notifications from the queue that match a provided notification using provided matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:))*