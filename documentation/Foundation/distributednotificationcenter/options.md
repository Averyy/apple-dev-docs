# DistributedNotificationCenter.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](./postnotificationname%28_,object,userinfo,options%29.md) method.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct Options
```

```c
enum NSDistributedNotificationOptions : NSUInteger;
```

## Topics

### Constants
- [var NSNotificationDeliverImmediately: DistributedNotificationCenter.Options](../nsnotificationdeliverimmediately.md)
  When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.
- [static var deliverImmediately: DistributedNotificationCenter.Options](./options/deliverimmediately.md)
  When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state.
- [var NSNotificationPostToAllSessions: DistributedNotificationCenter.Options](../nsnotificationposttoallsessions.md)
  When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
- [static var postToAllSessions: DistributedNotificationCenter.Options](./options/posttoallsessions.md)
  When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [DistributedNotificationCenter.CenterType](./centertype.md)
  This constant specifies the notification center type.
- [DistributedNotificationCenter.SuspensionBehavior](./suspensionbehavior.md)
  These constants specify the types of notification delivery suspension behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/options)*