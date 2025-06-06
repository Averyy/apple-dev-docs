# insert(_:after:)

**Framework**: Media Player  
**Kind**: method

Inserts a modified queue after the designated media item.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func insert(_ queueDescriptor: MPMusicPlayerQueueDescriptor, after afterItem: MPMediaItem?)
```

## Parameters

- `queueDescriptor`: A queue descriptor the system uses to insert media items in the playback queue.
- `afterItem`: The media item before the insertion point for the modified queue.

## See Also

- [func remove(MPMediaItem)](mpmusicplayercontrollermutablequeue/remove(_:).md)
  Removes a media item from the music player’s queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollermutablequeue/insert(_:after:))*