# container(_:)

**Framework**: Group Activities  
**Kind**: method

Creates an item that contains the name of a container.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static func container(_ name: String) -> GroupSessionEvent.Action.QueueChange.Item
```

#### Discussion

When a participant changes an entire queue, call this method to create an item with the queue name. When you show the change notice, SharePlay displays the container name to the participant.

## Parameters

- `name`: The name of the container.

## See Also

- [static func song(String) -> GroupSessionEvent.Action.QueueChange.Item](groupsessionevent/action-swift.struct/queuechange/item/song(_:).md)
  Creates an item that contains the name of a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/queuechange/item/container(_:))*