# setQueue(with:)

**Framework**: Media Player  
**Kind**: method

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

#### Discussion

To begin playback after establishing a playback queue, call [`prepareToPlay()`](mpmediaplayback/preparetoplay().md).

## Parameters

- `query`: A media query that specifies the collection of media items that you want as the playback queue. See   for a description of query types and how to create them.

## See Also

- [func setQueue(with: MPMediaItemCollection)](mpmusicplayercontroller/setqueue(with:)-xlwk.md)
  Sets a music player’s playback queue using a media item collection.
- [func setQueue(with: [String])](mpmusicplayercontroller/setqueue(with:)-8x6xb.md)
  Sets a music player’s playback queue using with media items identified by the store identifiers.
- [func setQueue(with: MPMusicPlayerQueueDescriptor)](mpmusicplayercontroller/setqueue(with:)-1izmj.md)
  Set the music player’s playback queue using media items that fit the queue descriptor properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/setqueue(with:)-5rii3)*