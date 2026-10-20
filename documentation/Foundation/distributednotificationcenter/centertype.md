# DistributedNotificationCenter.CenterType

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

This constant specifies the notification center type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct CenterType
```

```c
typedef NSString * NSDistributedNotificationCenterType;
```

## Topics

### Type Properties
- [static let localNotificationCenterType: DistributedNotificationCenter.CenterType](./centertype/localnotificationcentertype.md)
  Distributes notifications to all tasks on the sender’s computer.
### Initializers
- [init(String)](./centertype/init%28_%29.md)
- [init(rawValue: String)](./centertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [DistributedNotificationCenter.Options](./options.md)
  These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](./postnotificationname%28_,object,userinfo,options%29.md) method.
- [DistributedNotificationCenter.SuspensionBehavior](./suspensionbehavior.md)
  These constants specify the types of notification delivery suspension behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/centertype)*