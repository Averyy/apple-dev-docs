# HMMutablePresenceEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMMutablePresenceEvent : HMPresenceEvent
```

## Topics

### Configuring a presence event
- [var presenceEventType: HMPresenceEventType](./hmmutablepresenceevent/presenceeventtype.md)
  The event type that triggers the presence event.
- [var presenceUserType: HMPresenceEventUserType](./hmmutablepresenceevent/presenceusertype.md)
  The user type whose presence triggers the event.

## Relationships

### Inherits From
- [HMPresenceEvent](./hmpresenceevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### User presence
- [class HMPresenceEvent](./hmpresenceevent.md)
  An event that triggers based on the presence of users in the home.
- [enum HMPresenceEventType](./hmpresenceeventtype.md)
  The user presence type that triggers a presence event.
- [enum HMPresenceEventUserType](./hmpresenceeventusertype.md)
  The group of users that triggers a presence event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablepresenceevent)*