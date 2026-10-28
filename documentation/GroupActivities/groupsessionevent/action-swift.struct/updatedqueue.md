# updatedQueue

**Framework**: Group Activities  
**Kind**: property  
**Role**: Type Property

An action that represents a nonspecific change to the queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let updatedQueue: GroupSessionEvent.Action
```

## Discussion

Use this action when the other action types don’t accurately describe the change you made to the queue. If you can specify the change using a [`GroupSessionEvent.Action.QueueChange`](./queuechange.md) type, use the [`updatedQueue(_:)`](./updatedqueue%28_%29.md) method instead.

## See Also

### Getting change-related actions
- [static func updatedQueue(GroupSessionEvent.Action.QueueChange) -> GroupSessionEvent.Action](./updatedqueue%28_%29.md)
  Returns an action that represents a change to the playback queue.
- [GroupSessionEvent.Action.QueueChange](./queuechange.md)
  A type that describes a modification to the playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/updatedqueue)*