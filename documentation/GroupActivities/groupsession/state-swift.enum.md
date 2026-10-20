# GroupSession.State

**Framework**: Group Activities  
**Kind**: enum  
**Role**: Enumeration

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
- [GroupSession.State.waiting](./state-swift.enum/waiting.md)
  An idle state that indicates the session is waiting for the app to join the activity.
- [GroupSession.State.joined](./state-swift.enum/joined.md)
  An active state that indicates the session allows data synchronization between devices.
- [GroupSession.State.invalidated(reason:)](./state-swift.enum/invalidated%28reason%29.md)
  A state that indicates the session is no longer valid and can’t be used for shared activities.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the session details
- [var state: GroupSession<ActivityType>.State](./state-swift.property.md)
  The current state of the session.
- [let id: UUID](./id.md)
  The unique identifier of the current session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/state-swift.enum)*