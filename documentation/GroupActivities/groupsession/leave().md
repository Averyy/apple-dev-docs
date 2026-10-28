# leave()

**Framework**: Group Activities  
**Kind**: method  
**Role**: Instance Method

Leaves the current activity and stops receiving synchronized data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func leave()
```

## Mentions

- [Joining and managing a shared activity](../joining-and-managing-a-shared-activity.md)

## Discussion

When you call this method, the session transitions to the [`GroupSession.State.invalidated(reason:)`](./state-swift.enum/invalidated%28reason%29.md) state and stops the delivery of session-related updates. Call this method when the user dismisses your app’s activity-related UI.

Don’t call this method on a session already in the [`GroupSession.State.invalidated(reason:)`](./state-swift.enum/invalidated%28reason%29.md) state.

## See Also

### Joining and leaving the session
- [func join()](./join%28%29.md)
  Starts the shared activity on the current device.
- [func end()](./end%28%29.md)
  Ends the activity for the entire group and stops the transfer of synchronized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/leave())*