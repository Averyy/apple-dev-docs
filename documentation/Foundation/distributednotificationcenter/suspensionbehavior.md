# DistributedNotificationCenter.SuspensionBehavior

**Framework**: Foundation  
**Kind**: enum

These constants specify the types of notification delivery suspension behaviors.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SuspensionBehavior
```

## Topics

### Constants
- [DistributedNotificationCenter.SuspensionBehavior.drop](distributednotificationcenter/suspensionbehavior/drop.md)
  The server does not queue any notifications with this name and object until [`suspended`](distributednotificationcenter/suspended.md) with an argument of [`false`](https://developer.apple.com/documentation/swift/false) is called.
- [DistributedNotificationCenter.SuspensionBehavior.coalesce](distributednotificationcenter/suspensionbehavior/coalesce.md)
  The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [DistributedNotificationCenter.SuspensionBehavior.hold](distributednotificationcenter/suspensionbehavior/hold.md)
  The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [DistributedNotificationCenter.SuspensionBehavior.deliverImmediately](distributednotificationcenter/suspensionbehavior/deliverimmediately.md)
- [DistributedNotificationCenter.SuspensionBehavior.drop](distributednotificationcenter/suspensionbehavior/drop.md)
  The server does not queue any notifications with this name and object until [`suspended`](distributednotificationcenter/suspended.md) with an argument of [`false`](https://developer.apple.com/documentation/swift/false) is called.
- [DistributedNotificationCenter.SuspensionBehavior.coalesce](distributednotificationcenter/suspensionbehavior/coalesce.md)
  The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [DistributedNotificationCenter.SuspensionBehavior.hold](distributednotificationcenter/suspensionbehavior/hold.md)
  The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [DistributedNotificationCenter.SuspensionBehavior.deliverImmediately](distributednotificationcenter/suspensionbehavior/deliverimmediately.md)
### Initializers
- [init?(rawValue: UInt)](distributednotificationcenter/suspensionbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [DistributedNotificationCenter.Options](distributednotificationcenter/options.md)
  These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md) method.
- [DistributedNotificationCenter.CenterType](distributednotificationcenter/centertype.md)
  This constant specifies the notification center type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior)*