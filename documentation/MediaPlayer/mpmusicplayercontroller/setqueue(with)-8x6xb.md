# setQueue(with:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Sets a music player’s playback queue using with media items identified by the store identifiers.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setQueue(with storeIDs: [String])
```

```objc
- (void) setQueueWithStoreIDs:(NSArray<NSString *> *) storeIDs;
```

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](../mpmediaplayback/preparetoplay%28%29.md).

## Parameters

- `storeIDs`: An array of store identifiers associated with the media items to add to the queue.

## See Also

### Setting up a playback queue
- [func setQueue(with: MPMediaQuery)](./setqueue%28with%29-5rii3.md)
  Sets a music player’s playback queue based on a media query.
- [func setQueue(with: MPMediaItemCollection)](./setqueue%28with%29-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: MPMusicPlayerQueueDescriptor)](./setqueue%28with%29-1izmj.md)
  Set the music player’s playback queue using media items that fit the queue descriptor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-8x6xb)*