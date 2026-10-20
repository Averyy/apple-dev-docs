# setQueue(with:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Set the music player’s playback queue using media items that fit the queue descriptor properties.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setQueue(with descriptor: MPMusicPlayerQueueDescriptor)
```

```objc
- (void) setQueueWithDescriptor:(MPMusicPlayerQueueDescriptor *) descriptor;
```

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](../mpmediaplayback/preparetoplay%28%29.md).

## Parameters

- `descriptor`: A queue descriptor the system uses to add media items to the playback queue.

## See Also

### Setting up a playback queue
- [func setQueue(with: MPMediaQuery)](./setqueue%28with%29-5rii3.md)
  Sets a music player’s playback queue based on a media query.
- [func setQueue(with: MPMediaItemCollection)](./setqueue%28with%29-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: [String])](./setqueue%28with%29-8x6xb.md)
  Sets a music player’s playback queue using with media items identified by the store identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-1izmj)*