# setQueue(with:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Sets a music player’s playback queue based on a media query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setQueue(with query: MPMediaQuery)
```

```objc
- (void) setQueueWithQuery:(MPMediaQuery *) query;
```

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](../mpmediaplayback/preparetoplay%28%29.md).

## Parameters

- `query`: A media query that specifies the collection of media items that you want as the playback queue. See [`MPMediaQuery`](../mpmediaquery.md) for a description of query types and how to create them.

## See Also

### Setting up a playback queue
- [func setQueue(with: MPMediaItemCollection)](./setqueue%28with%29-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: [String])](./setqueue%28with%29-8x6xb.md)
  Sets a music player’s playback queue using with media items identified by the store identifiers.
- [func setQueue(with: MPMusicPlayerQueueDescriptor)](./setqueue%28with%29-1izmj.md)
  Set the music player’s playback queue using media items that fit the queue descriptor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-5rii3)*