# DistributedNotificationCenter.CenterType

**Framework**: Foundation  
**Kind**: struct

This constant specifies the notification center type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct CenterType
```

## Topics

### Type Properties
- [static let localNotificationCenterType: DistributedNotificationCenter.CenterType](distributednotificationcenter/centertype/localnotificationcentertype.md)
  Distributes notifications to all tasks on the sender’s computer.
### Initializers
- [init(String)](distributednotificationcenter/centertype/init(_:).md)
- [init(rawValue: String)](distributednotificationcenter/centertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DistributedNotificationCenter.Options](distributednotificationcenter/options.md)
  These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md) method.
- [DistributedNotificationCenter.SuspensionBehavior](distributednotificationcenter/suspensionbehavior.md)
  These constants specify the types of notification delivery suspension behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/centertype)*