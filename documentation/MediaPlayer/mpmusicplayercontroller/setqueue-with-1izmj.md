# setQueue(with:)

**Framework**: Media Player  
**Kind**: method

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

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](mpmediaplayback/preparetoplay().md).

## Parameters

- `descriptor`: A queue descriptor the system uses to add media items to the playback queue.

## See Also

- [func setQueue(with: MPMediaQuery)](mpmusicplayercontroller/setqueue(with:)-5rii3.md)
  Sets a music player’s playback queue based on a media query.
- [func setQueue(with: MPMediaItemCollection)](mpmusicplayercontroller/setqueue(with:)-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: [String])](mpmusicplayercontroller/setqueue(with:)-8x6xb.md)
  Sets a music player’s playback queue using with media items identified by the store identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-1izmj)*