# HMPresenceEventUserType

**Framework**: HomeKit  
**Kind**: enum

The group of users that triggers a presence event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum HMPresenceEventUserType
```

## Topics

### Selecting users
- [HMPresenceEventUserType.currentUser](hmpresenceeventusertype/currentuser.md)
  The current user triggers the presence event.
- [HMPresenceEventUserType.homeUsers](hmpresenceeventusertype/homeusers.md)
  All users associated with a home trigger a presence event.
- [HMPresenceEventUserType.customUsers](hmpresenceeventusertype/customusers.md)
  A custom set of users is used to trigger a presence event.
### Initializers
- [init?(rawValue: UInt)](hmpresenceeventusertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HMPresenceEvent](hmpresenceevent.md)
  An event that triggers based on the presence of users in the home.
- [class HMMutablePresenceEvent](hmmutablepresenceevent.md)
  A mutable event that triggers based on the presence of users in the home.
- [enum HMPresenceEventType](hmpresenceeventtype.md)
  The user presence type that triggers a presence event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmpresenceeventusertype)*