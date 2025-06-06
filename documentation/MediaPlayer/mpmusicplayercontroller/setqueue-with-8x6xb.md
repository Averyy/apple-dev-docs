# setQueue(with:)

**Framework**: Media Player  
**Kind**: method

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

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](mpmediaplayback/preparetoplay().md).

## Parameters

- `storeIDs`: An array of store identifiers associated with the media items to add to the queue.

## See Also

- [func setQueue(with: MPMediaQuery)](mpmusicplayercontroller/setqueue(with:)-5rii3.md)
  Sets a music player’s playback queue based on a media query.
- [func setQueue(with: MPMediaItemCollection)](mpmusicplayercontroller/setqueue(with:)-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/setqueue(with:)-1izmj.md)
  Set the music player’s playback queue using media items that fit the queue descriptor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-8x6xb)*