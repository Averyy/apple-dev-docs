# skipToPreviousItem()

**Framework**: Media Player  
**Kind**: method

Starts playback of the previous media item in the playback queue, or if the music player isn’t playing, designates the previous media item as the next to play.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func skipToPreviousItem()
```

#### Discussion

Calling this method when already at the first item in the playback queue ends playback.

## See Also

- [var nowPlayingItem: MPMediaItem?](mpmusicplayercontroller/nowplayingitem.md)
  The currently-playing media item, or the media item in a queue that you designated to begin playback with.
- [func skipToNextItem()](mpmusicplayercontroller/skiptonextitem.md)
  Starts playback of the next media item in the playback queue, or if the music player isn’t playing, designates the next media item as the next item to play.
- [func skipToBeginning()](mpmusicplayercontroller/skiptobeginning.md)
  Restarts playback at the beginning of the currently playing media item.
- [func append(MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/append(_:).md)
  Inserts the media items defined by the queue descriptor after the last media item in the current queue.
- [func prepend(MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/prepend(_:).md)
  Inserts the media items defined by the queue descriptor into the current queue immediately after the currently playing media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/skiptopreviousitem())*