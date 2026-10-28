# initWithMediaItems:mediaContainer:playShuffled:playbackRepeatMode:resumePlayback:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes an intent that describes media content such as a song, podcast episode, or movie.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 12.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 6.0

## Declaration

```objc
- (instancetype) initWithMediaItems:(NSArray<INMediaItem *> *) mediaItems mediaContainer:(INMediaItem *) mediaContainer playShuffled:(NSNumber *) playShuffled playbackRepeatMode:(INPlaybackRepeatMode) playbackRepeatMode resumePlayback:(NSNumber *) resumePlayback;
```

## Discussion

The [`INPlayMediaIntent`](../inplaymediaintent.md) object should include information about the media that accurately represents the content. For example, if the user plays a song from a particular album, include both pieces of information in the intent. Provide the song in `mediaItems` and the album in `mediaContainer`. If your app supports options for shuffle play, repeat modes, and resuming playback, include the current settings for those options when creating the intent.

## Parameters

- `mediaItems`: The media content, such as a song or episode of TV show, that the user is playing. When donating the intent, the system uses only the first item in the array, ignoring the other media items in the array.
- `mediaContainer`: The container of the media item. For example, when the user plays a song from the playlist, the playlist is the container. A television show with multiple episodes is another example. However, some media items, like movies, may have no container.
- `playShuffled`: A Boolean value that indicates whether the media plays in a shuffled order.
- `playbackRepeatMode`: The repeat mode setting at the time the user plays the media item.
- `resumePlayback`: The resume playback setting at the time the user plays the media item. Set to [`true`](../../Swift/true.md) when the user hasn’t finished listening to or watching the media item.

## See Also

### Creating a Play Media Intent
- [- initWithMediaItems:mediaContainer:playShuffled:playbackRepeatMode:resumePlayback:playbackQueueLocation:playbackSpeed:mediaSearch:](./initwithmediaitems_mediacontainer_playshuffled_playbackrepeatmode_resumeplayback_playbackqueuelocation_playbackspeed_mediasearch_.md)
  Initialize an intent that describes media content such as a song, podcast episode, or movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent/initwithmediaitems:mediacontainer:playshuffled:playbackrepeatmode:resumeplayback:)*