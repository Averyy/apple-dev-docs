# GroupSessionEvent.Action.QueueChange.Item

**Framework**: Group Activities  
**Kind**: struct

Detailed information about an item involved in a queue change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Item
```

#### Overview

Before you notify a participant about a queue-related change, create an item that contains the name of the song or container that changed. Use this item to configure a [`GroupSessionEvent.Action.QueueChange`](groupsessionevent/action-swift.struct/queuechange.md) structure with additional details about the change.

## Topics

### Creating the item
- [static func song(String) -> GroupSessionEvent.Action.QueueChange.Item](groupsessionevent/action-swift.struct/queuechange/item/song(_:).md)
  Creates an item that contains the name of a song.
- [static func container(String) -> GroupSessionEvent.Action.QueueChange.Item](groupsessionevent/action-swift.struct/queuechange/item/container(_:).md)
  Creates an item that contains the name of a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/queuechange/item)*