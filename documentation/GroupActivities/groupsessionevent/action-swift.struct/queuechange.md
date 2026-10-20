# GroupSessionEvent.Action.QueueChange

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

A type that describes a modification to the playback queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct QueueChange
```

#### Overview

Use this type to inform the participant about changes to the playback queue associated with the current activity. Your app manages the queue, along with any additions or changes. You use this type to communicate those changes back to the participant using the system UI.

When a change occurs, configure this type with information about the change, and wrap it in a [`GroupSessionEvent.Action`](../action-swift.struct.md) type. Pass the action to the [`showNotice(_:)`](../../groupsession/shownotice%28_%29.md) method to display the change to the participant.

## Topics

### Specifying the type of change
- [static func added(GroupSessionEvent.Action.QueueChange.Item) -> GroupSessionEvent.Action.QueueChange](./queuechange/added%28_%29.md)
  Returns a queue change for an added item.
- [static func setUpNext(GroupSessionEvent.Action.QueueChange.Item) -> GroupSessionEvent.Action.QueueChange](./queuechange/setupnext%28_%29.md)
  Returns a queue change for a new up-next item.
### Getting the changed item
- [GroupSessionEvent.Action.QueueChange.Item](./queuechange/item.md)
  Detailed information about an item involved in a queue change.

## See Also

### Getting change-related actions
- [static func updatedQueue(GroupSessionEvent.Action.QueueChange) -> GroupSessionEvent.Action](./updatedqueue%28_%29.md)
  Returns an action that represents a change to the playback queue.
- [static let updatedQueue: GroupSessionEvent.Action](./updatedqueue.md)
  An action that represents a nonspecific change to the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/queuechange)*