# DistributedNotificationCenter.SuspensionBehavior.deliverImmediately

**Framework**: Foundation  
**Kind**: case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case deliverImmediately
```

#### Discussion

The server delivers notifications matching this registration irrespective of whether [`suspended`](distributednotificationcenter/suspended.md) with an argument of [`true`](https://developer.apple.com/documentation/swift/true) has been called. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications. The effect is as if [`suspended`](distributednotificationcenter/suspended.md) with an argument of [`false`](https://developer.apple.com/documentation/swift/false) were first called if the application is suspended, followed by the notification in question being delivered, followed by a transition back to the previous suspended or unsuspended state.

## See Also

- [DistributedNotificationCenter.SuspensionBehavior.drop](distributednotificationcenter/suspensionbehavior/drop.md)
  The server does not queue any notifications with this name and object until [`suspended`](distributednotificationcenter/suspended.md) with an argument of [`false`](https://developer.apple.com/documentation/swift/false) is called.
- [DistributedNotificationCenter.SuspensionBehavior.coalesce](distributednotificationcenter/suspensionbehavior/coalesce.md)
  The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [DistributedNotificationCenter.SuspensionBehavior.hold](distributednotificationcenter/suspensionbehavior/hold.md)
  The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [DistributedNotificationCenter.SuspensionBehavior.drop](distributednotificationcenter/suspensionbehavior/drop.md)
  The server does not queue any notifications with this name and object until [`suspended`](distributednotificationcenter/suspended.md) with an argument of [`false`](https://developer.apple.com/documentation/swift/false) is called.
- [DistributedNotificationCenter.SuspensionBehavior.coalesce](distributednotificationcenter/suspensionbehavior/coalesce.md)
  The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [DistributedNotificationCenter.SuspensionBehavior.hold](distributednotificationcenter/suspensionbehavior/hold.md)
  The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior/deliverimmediately)*