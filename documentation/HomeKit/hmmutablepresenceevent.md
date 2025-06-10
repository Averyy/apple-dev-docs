# HMMutablePresenceEvent

**Framework**: HomeKit  
**Kind**: class

A mutable event that triggers based on the presence of users in the home.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMMutablePresenceEvent
```

## Topics

### Configuring a presence event
- [var presenceEventType: HMPresenceEventType](hmmutablepresenceevent/presenceeventtype.md)
  The event type that triggers the presence event.
- [var presenceUserType: HMPresenceEventUserType](hmmutablepresenceevent/presenceusertype.md)
  The user type whose presence triggers the event.

## Relationships

### Inherits From
- [HMPresenceEvent](hmpresenceevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HMPresenceEvent](hmpresenceevent.md)
  An event that triggers based on the presence of users in the home.
- [enum HMPresenceEventType](hmpresenceeventtype.md)
  The user presence type that triggers a presence event.
- [enum HMPresenceEventUserType](hmpresenceeventusertype.md)
  The group of users that triggers a presence event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablepresenceevent)*