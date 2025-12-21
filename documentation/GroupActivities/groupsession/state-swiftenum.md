# GroupSession.State

**Framework**: Group Activities  
**Kind**: enum

The possible states of a session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

## Topics

### Session states
- [GroupSession.State.waiting](groupsession/state-swift.enum/waiting.md)
  An idle state that indicates the session is waiting for the app to join the activity.
- [GroupSession.State.joined](groupsession/state-swift.enum/joined.md)
  An active state that indicates the session allows data synchronization between devices.
- [GroupSession.State.invalidated(reason:)](groupsession/state-swift.enum/invalidated(reason:).md)
  A state that indicates the session is no longer valid and can’t be used for shared activities.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: GroupSession<ActivityType>.State](groupsession/state-swift.property.md)
  The current state of the session.
- [let id: UUID](groupsession/id.md)
  The unique identifier of the current session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/state-swift.enum)*