# dequeueNotifications(matching:coalesceMask:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) dequeueNotificationsMatching:(NSNotification *) notification coalesceMask:(NSUInteger) coalesceMask;
```

## Parameters

- `notification`: The notification used for matching notifications to remove from the notification queue.
- `coalesceMask`: A mask indicating what criteria to use when matching attributes of `notification` to attributes of notifications in the queue. The mask is created by combining any of the constants [`none`](./notificationcoalescing/none.md), [`onName`](./notificationcoalescing/onname.md), and [`onSender`](./notificationcoalescing/onsender.md).

## See Also

### Managing Notifications
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](./enqueue%28_,postingstyle,coalescemask,formodes%29.md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle)](./enqueue%28_,postingstyle%29.md)
  Adds a notification to the notification queue with a specified posting style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/dequeuenotifications(matching:coalescemask:))*