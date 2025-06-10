# HMPresenceEventType

**Framework**: HomeKit  
**Kind**: enum

The user presence type that triggers a presence event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum HMPresenceEventType
```

## Topics

### Specifying presence type
- [HMPresenceEventType.everyEntry](hmpresenceeventtype/everyentry.md)
  Triggers the event every time a user enters the home.
- [HMPresenceEventType.everyExit](hmpresenceeventtype/everyexit.md)
  Triggers the event every time a user leaves the home.
- [HMPresenceEventType.firstEntry](hmpresenceeventtype/firstentry.md)
  Triggers an event for the first user entering the home.
- [HMPresenceEventType.lastExit](hmpresenceeventtype/lastexit.md)
  Triggers an event when the last user leaves the home.
### Using presence as a predicate
- [static var atHome: HMPresenceEventType](hmpresenceeventtype/athome.md)
  Triggers the event when at least one user is in the home.
- [static var notAtHome: HMPresenceEventType](hmpresenceeventtype/notathome.md)
  Triggers the event when there are no users in the home.
### Initializers
- [init?(rawValue: UInt)](hmpresenceeventtype/init(rawvalue:).md)

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
- [enum HMPresenceEventUserType](hmpresenceeventusertype.md)
  The group of users that triggers a presence event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmpresenceeventtype)*