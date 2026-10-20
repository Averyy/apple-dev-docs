# DistributedNotificationCenter.SuspensionBehavior.coalesce

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case coalesce
```

```c
NSNotificationSuspensionBehaviorCoalesce
```

## See Also

### Constants
- [DistributedNotificationCenter.SuspensionBehavior.drop](./drop.md)
  The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.
- [DistributedNotificationCenter.SuspensionBehavior.hold](./hold.md)
  The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [DistributedNotificationCenter.SuspensionBehavior.deliverImmediately](./deliverimmediately.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior/coalesce)*