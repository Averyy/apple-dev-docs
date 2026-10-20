# enqueue(_:postingStyle:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a notification to the notification queue with a specified posting style.

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
func enqueue(_ notification: Notification, postingStyle: NotificationQueue.PostingStyle)
```

```objc
- (void) enqueueNotification:(NSNotification *) notification postingStyle:(NSPostingStyle) postingStyle;
```

#### Discussion

This is a convenience method for calling [`enqueue(_:postingStyle:coalesceMask:forModes:)`](./enqueue%28_,postingstyle,coalescemask,formodes%29.md) with coalescing criteria that will coalesce only notifications that match both the notification’s name and object and the runloop mode [`default`](../runloop/mode/default.md).

## Parameters

- `notification`: The notification to add to the queue.
- `postingStyle`: The posting style for the notification. The posting style indicates when the notification queue should post the notification to its notification center.

## See Also

### Managing Notifications
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](./enqueue%28_,postingstyle,coalescemask,formodes%29.md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [func dequeueNotifications(matching: Notification, coalesceMask: Int)](./dequeuenotifications%28matching,coalescemask%29.md)
  Removes all notifications from the queue that match a provided notification using provided matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/enqueue(_:postingstyle:))*