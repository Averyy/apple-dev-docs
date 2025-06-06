# dequeueNotifications(matching:coalesceMask:)

**Framework**: Foundation  
**Kind**: method

Removes all notifications from the queue that match a provided notification using provided matching criteria.

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
func dequeueNotifications(matching notification: Notification, coalesceMask: Int)
```

## Parameters

- `notification`: The notification used for matching notifications to remove from the notification queue.
- `coalesceMask`: A mask indicating what criteria to use when matching attributes of   to attributes of notifications in the queue. The mask is created by combining any of the constants  ,  , and  .

## See Also

- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:).md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle)](notificationqueue/enqueue(_:postingstyle:).md)
  Adds a notification to the notification queue with a specified posting style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/dequeuenotifications(matching:coalescemask:))*