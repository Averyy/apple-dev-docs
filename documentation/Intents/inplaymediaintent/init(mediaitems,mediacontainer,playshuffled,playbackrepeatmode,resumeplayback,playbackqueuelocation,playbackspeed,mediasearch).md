# init(mediaItems:mediaContainer:playShuffled:playbackRepeatMode:resumePlayback:playbackQueueLocation:playbackSpeed:mediaSearch:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an intent that describes media content such as a song, podcast episode, or movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 14.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
convenience init(mediaItems: [INMediaItem]? = nil, mediaContainer: INMediaItem? = nil, playShuffled: Bool? = nil, playbackRepeatMode: INPlaybackRepeatMode = .unknown, resumePlayback: Bool? = nil, playbackQueueLocation: INPlaybackQueueLocation = .unknown, playbackSpeed: Double? = nil, mediaSearch: INMediaSearch? = nil)
```

#### Discussion

The [`INPlayMediaIntent`](../inplaymediaintent.md) object should include information about the media that accurately represents the content. For example, if the user plays a song from a particular album, include both pieces of information in the intent. Provide the song in `mediaItems` and the album in `mediaContainer`. If your app supports options for shuffle play, repeat modes, and resuming playback, include the current settings for those options when creating the intent.

## Parameters

- `mediaItems`: The media content, such as a song or episode of TV show, that the user is playing. When donating the intent, the system uses only the first item in the array, ignoring the other media items in the array.
- `mediaContainer`: The container of the media item. For example, when the user plays a song from the playlist, the playlist is the container. A television show with multiple episodes is another example. However, some media items, like movies, may have no container.
- `playShuffled`: A Boolean value that indicates whether the media plays in a shuffled order.
- `playbackRepeatMode`: The repeat mode setting at the time the user plays the media item.
- `resumePlayback`: The resume playback setting at the time the user plays the media item. Set to [`true`](../../Swift/true.md) when the user hasn’t finished listening to or watching the media item.
- `playbackQueueLocation`: The location in the queue to play the media item.
- `playbackSpeed`: The speed to play the media item.
- `mediaSearch`: The search parameters for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent/init(mediaitems:mediacontainer:playshuffled:playbackrepeatmode:resumeplayback:playbackqueuelocation:playbackspeed:mediasearch:))*