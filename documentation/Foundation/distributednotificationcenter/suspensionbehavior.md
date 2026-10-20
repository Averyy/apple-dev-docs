# DistributedNotificationCenter.SuspensionBehavior

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants specify the types of notification delivery suspension behaviors.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SuspensionBehavior
```

```c
enum NSNotificationSuspensionBehavior : NSUInteger;
```

## Topics

### Constants
- [DistributedNotificationCenter.SuspensionBehavior.drop](./suspensionbehavior/drop.md)
  The server doesn’t queue any notifications with this name and object until the notification center resumes notification delivery.
- [DistributedNotificationCenter.SuspensionBehavior.coalesce](./suspensionbehavior/coalesce.md)
  The server only queues the last notification of the specified name and object; earlier notifications are dropped. In cover methods for which suspension behavior is not an explicit argument, `NSNotificationSuspensionBehaviorCoalesce` is the default.
- [DistributedNotificationCenter.SuspensionBehavior.hold](./suspensionbehavior/hold.md)
  The server holds all matching notifications until the queue has been filled (queue size determined by the server), at which point the server may flush queued notifications.
- [DistributedNotificationCenter.SuspensionBehavior.deliverImmediately](./suspensionbehavior/deliverimmediately.md)
### Initializers
- [init?(rawValue: UInt)](./suspensionbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [DistributedNotificationCenter.Options](./options.md)
  These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](./postnotificationname%28_,object,userinfo,options%29.md) method.
- [DistributedNotificationCenter.CenterType](./centertype.md)
  This constant specifies the notification center type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspensionbehavior)*