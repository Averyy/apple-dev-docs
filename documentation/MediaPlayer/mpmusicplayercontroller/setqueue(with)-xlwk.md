# setQueue(with:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Sets a music player’s playback queue using a media item collection.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setQueue(with itemCollection: MPMediaItemCollection)
```

```objc
- (void) setQueueWithItemCollection:(MPMediaItemCollection *) itemCollection;
```

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](../mpmediaplayback/preparetoplay%28%29.md).

## Parameters

- `itemCollection`: A media item collection that you want as the playback queue. See [`MPMediaItemCollection`](../mpmediaitemcollection.md) for a description of media item collections and how to use them.

## See Also

### Setting up a playback queue
- [func setQueue(with: MPMediaQuery)](./setqueue%28with%29-5rii3.md)
  Sets a music player’s playback queue based on a media query.
- [func setQueue(with: [String])](./setqueue%28with%29-8x6xb.md)
  Sets a music player’s playback queue using with media items identified by the store identifiers.
- [func setQueue(with: MPMusicPlayerQueueDescriptor)](./setqueue%28with%29-1izmj.md)
  Set the music player’s playback queue using media items that fit the queue descriptor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-xlwk)*