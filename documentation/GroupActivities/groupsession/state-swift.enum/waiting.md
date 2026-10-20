# GroupSession.State.waiting

**Framework**: Group Activities  
**Kind**: case  
**Role**: Case

An idle state that indicates the session is waiting for the app to join the activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case waiting
```

## Mentions

- [Joining and managing a shared activity](../../joining-and-managing-a-shared-activity.md)

## See Also

### Session states
- [GroupSession.State.joined](./joined.md)
  An active state that indicates the session allows data synchronization between devices.
- [GroupSession.State.invalidated(reason:)](./invalidated%28reason%29.md)
  A state that indicates the session is no longer valid and can’t be used for shared activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/state-swift.enum/waiting)*