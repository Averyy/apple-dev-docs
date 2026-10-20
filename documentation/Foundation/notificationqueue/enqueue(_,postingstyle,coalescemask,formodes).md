# enqueue(_:postingStyle:coalesceMask:forModes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) enqueueNotification:(NSNotification *) notification postingStyle:(NSPostingStyle) postingStyle coalesceMask:(NSNotificationCoalescing) coalesceMask forModes:(NSArray<NSString *> *) modes;
```

## Parameters

- `notification`: The notification to add to the queue.
- `postingStyle`: The posting style for the notification. The posting style indicates when the notification queue should post the notification to its notification center.
- `coalesceMask`: A mask indicating what criteria to use when matching attributes of `notification` to attributes of notifications in the queue. The mask is created by combining any of the constants [`none`](./notificationcoalescing/none.md), [`onName`](./notificationcoalescing/onname.md), and [`onSender`](./notificationcoalescing/onsender.md).
- `modes`: The list of modes the notification may be posted in. The notification queue will only post the notification to its notification center if the run loop is in one of the modes provided in the array.

  This parameter may be `nil`, in which case it defaults to [`default`](../runloop/mode/default.md).

## See Also

### Managing Notifications
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle)](./enqueue%28_,postingstyle%29.md)
  Adds a notification to the notification queue with a specified posting style.
- [func dequeueNotifications(matching: Notification, coalesceMask: Int)](./dequeuenotifications%28matching,coalescemask%29.md)
  Removes all notifications from the queue that match a provided notification using provided matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:))*