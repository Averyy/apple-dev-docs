# end()

**Framework**: Group Activities  
**Kind**: method

Ends the activity for the entire group and stops the transfer of synchronized data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func end()
```

## Mentions

- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)

#### Discussion

Call this method to end the activity for all participants. When you call this method, the session transitions to the [`GroupSession.State.invalidated(reason:)`](groupsession/state-swift.enum/invalidated(reason:).md) state and stops the delivery of session-related updates. After ending the session, you can’t join it again.

Don’t call this method on a session already in the [`GroupSession.State.invalidated(reason:)`](groupsession/state-swift.enum/invalidated(reason:).md) state.

## See Also

- [func join()](groupsession/join.md)
  Starts the shared activity on the current device.
- [func leave()](groupsession/leave.md)
  Leaves the current activity and stops receiving synchronized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/end())*