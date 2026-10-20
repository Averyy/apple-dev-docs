# skipToBeginning()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Restarts playback at the beginning of the currently playing media item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func skipToBeginning()
```

```objc
- (void) skipToBeginning;
```

## See Also

### Controlling playback
- [func skipToNextItem()](./skiptonextitem%28%29.md)
  Starts playback of the next media item in the playback queue, or if the music player isn’t playing, designates the next media item as the next item to play.
- [func skipToPreviousItem()](./skiptopreviousitem%28%29.md)
  Starts playback of the previous media item in the playback queue, or if the music player isn’t playing, designates the previous media item as the next to play.
- [func append(MPMusicPlayerQueueDescriptor)](./append%28_%29.md)
  Inserts the media items defined by the queue descriptor after the last media item in the current queue.
- [func prepend(MPMusicPlayerQueueDescriptor)](./prepend%28_%29.md)
  Inserts the media items defined by the queue descriptor into the current queue immediately after the currently playing media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/skiptobeginning())*