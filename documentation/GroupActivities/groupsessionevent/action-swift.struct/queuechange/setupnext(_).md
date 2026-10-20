# setUpNext(_:)

**Framework**: Group Activities  
**Kind**: method  
**Role**: Type Method

Returns a queue change for a new up-next item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static func setUpNext(_ item: GroupSessionEvent.Action.QueueChange.Item) -> GroupSessionEvent.Action.QueueChange
```

#### Return Value

A type that contains information about the change.

#### Discussion

Before showing a notice to the user, call this method to generate a type for the changed up-next item. Pass this type to the [`updatedQueue(_:)`](../updatedqueue%28_%29.md) method to create the postable action.

## Parameters

- `item`: The next item in the queue.

## See Also

### Specifying the type of change
- [static func added(GroupSessionEvent.Action.QueueChange.Item) -> GroupSessionEvent.Action.QueueChange](./added%28_%29.md)
  Returns a queue change for an added item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/queuechange/setupnext(_:))*