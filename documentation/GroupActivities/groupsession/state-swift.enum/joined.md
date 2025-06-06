# GroupSession.State.joined

**Framework**: Group Activities  
**Kind**: case

An active state that indicates the session allows data synchronization between devices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case joined
```

## Mentions

- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)

#### Discussion

Call the [`join()`](groupsession/join().md) method to begin the transition to this state. When the transition completes, use the session object to synchronize your app’s data with the other participants’ devices.

## See Also

- [GroupSession.State.waiting](groupsession/state-swift.enum/waiting.md)
  An idle state that indicates the session is waiting for the app to join the activity.
- [GroupSession.State.invalidated(reason:)](groupsession/state-swift.enum/invalidated(reason:).md)
  A state that indicates the session is no longer valid and can’t be used for shared activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/state-swift.enum/joined)*