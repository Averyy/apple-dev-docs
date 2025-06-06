# DistributedNotificationCenter.Options

**Framework**: Foundation  
**Kind**: struct

These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md) method.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct Options
```

## Topics

### Constants
- [static var deliverImmediately: DistributedNotificationCenter.Options](distributednotificationcenter/options/deliverimmediately.md)
- [static var postToAllSessions: DistributedNotificationCenter.Options](distributednotificationcenter/options/posttoallsessions.md)
### Constants
- [let NSNotificationDeliverImmediately: DistributedNotificationCenter.Options](nsnotificationdeliverimmediately.md)
  When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.
- [let NSNotificationPostToAllSessions: DistributedNotificationCenter.Options](nsnotificationposttoallsessions.md)
  When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
### Initializers
- [init(rawValue: UInt)](distributednotificationcenter/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [DistributedNotificationCenter.CenterType](distributednotificationcenter/centertype.md)
  This constant specifies the notification center type.
- [DistributedNotificationCenter.SuspensionBehavior](distributednotificationcenter/suspensionbehavior.md)
  These constants specify the types of notification delivery suspension behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/options)*