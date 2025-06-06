# prepend(_:)

**Framework**: Media Player  
**Kind**: method

Inserts the media items defined by the queue descriptor into the current queue immediately after the currently playing media item.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func prepend(_ descriptor: MPMusicPlayerQueueDescriptor)
```

## Parameters

- `descriptor`: A queue descriptor the system uses to prepend media items to the playback queue.

## See Also

- [func skipToNextItem()](mpmusicplayercontroller/skiptonextitem.md)
  Starts playback of the next media item in the playback queue, or if the music player isn’t playing, designates the next media item as the next item to play.
- [func skipToBeginning()](mpmusicplayercontroller/skiptobeginning.md)
  Restarts playback at the beginning of the currently playing media item.
- [func skipToPreviousItem()](mpmusicplayercontroller/skiptopreviousitem.md)
  Starts playback of the previous media item in the playback queue, or if the music player isn’t playing, designates the previous media item as the next to play.
- [func append(MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/append(_:).md)
  Inserts the media items defined by the queue descriptor after the last media item in the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/prepend(_:))*