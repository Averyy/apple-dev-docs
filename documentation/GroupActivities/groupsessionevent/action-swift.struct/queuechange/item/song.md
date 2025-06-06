# song(_:)

**Framework**: Group Activities  
**Kind**: method

Creates an item that contains the name of a song.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static func song(_ name: String) -> GroupSessionEvent.Action.QueueChange.Item
```

#### Discussion

When a participant adds a song or changes the next song in the queue, call this method to create an item with the song name. When you show the change notice, SharePlay displays the song name to the participant.

## Parameters

- `name`: The name of the song.

## See Also

- [static func container(String) -> GroupSessionEvent.Action.QueueChange.Item](groupsessionevent/action-swift.struct/queuechange/item/container(_:).md)
  Creates an item that contains the name of a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/queuechange/item/song(_:))*