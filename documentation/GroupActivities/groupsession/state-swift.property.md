# state

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

The current state of the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@Published
<GroupSession<ActivityType>.State> final var state: GroupSession<ActivityType>.State { get }
```

#### Discussion

Use this property to get the current state value, or configure a subscriber to detect changes to the value. To change the state of a session, call the [`join()`](./join%28%29.md) and [`leave()`](./leave%28%29.md) methods.

If a failure occurs or the session ends, the session object transitions to the [`GroupSession.State.invalidated(reason:)`](./state-swift.enum/invalidated%28reason%29.md)state. If the session ends because of an error, it provides information about that error.

## See Also

### Getting the session details
- [GroupSession.State](./state-swift.enum.md)
  The possible states of a session.
- [let id: UUID](./id.md)
  The unique identifier of the current session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/state-swift.property)*