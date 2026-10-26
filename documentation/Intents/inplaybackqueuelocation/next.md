# INPlaybackQueueLocation.next

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response that tells the system to play the media item after the currently playing media item finishes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case next
```

```c
INPlaybackQueueLocationNext
```

## See Also

### Constants
- [INPlaybackQueueLocation.unknown](./unknown.md)
  A response that indicates the system doesn’t know where to place the media item.
- [INPlaybackQueueLocation.now](./now.md)
  A response that tells the system to play the item immediately, interrupting any currently playing media.
- [INPlaybackQueueLocation.later](./later.md)
  A response that tells the system to add the media item to the end of the playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackqueuelocation/next)*