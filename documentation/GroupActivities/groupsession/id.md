# id

**Framework**: Group Activities  
**Kind**: property

The unique identifier of the current session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final let id: UUID
```

#### Discussion

The system assigns a globally unique identifier to each session. This identifier is valid only for the lifetime of the session object.

## See Also

- [var state: GroupSession<ActivityType>.State](groupsession/state-swift.property.md)
  The current state of the session.
- [GroupSession.State](groupsession/state-swift.enum.md)
  The possible states of a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/id)*