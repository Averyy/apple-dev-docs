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
### Comparing states
- [static func != (Self, Self) -> Bool](groupsession/state-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (GroupSession<ActivityType>.State, GroupSession<ActivityType>.State) -> Bool](groupsession/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](groupsession/state-swift.enum/equatable-implementations.md)

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
- [var description: String](groupsession/description.md)
  A textual representation of this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/state-swift.enum)*