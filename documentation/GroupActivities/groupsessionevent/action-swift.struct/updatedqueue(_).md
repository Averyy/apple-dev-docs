# updatedQueue(_:)

**Framework**: Group Activities  
**Kind**: method  
**Role**: Type Method

Returns an action that represents a change to the playback queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static func updatedQueue(_ change: GroupSessionEvent.Action.QueueChange) -> GroupSessionEvent.Action
```

#### Discussion

When you want to notify the user of changes to the playback queue, call this method to create an action type with the details of the change. Then call the [`showNotice(_:)`](../../groupsession/shownotice%28_%29.md) method to post that action. For example, use the following code to notify the user that someone added a song to the queue.

```swift
groupSession.showNotice(.updatedQueue(.added(.song("Here comes the sun"))))
```

## Parameters

- `change`: The change that ocurred to the queue.

## See Also

### Getting change-related actions
- [static let updatedQueue: GroupSessionEvent.Action](./updatedqueue.md)
  An action that represents a nonspecific change to the queue.
- [GroupSessionEvent.Action.QueueChange](./queuechange.md)
  A type that describes a modification to the playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/updatedqueue(_:))*