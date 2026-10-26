# playbackSpeed

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The playback speed for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * playbackSpeed;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * playbackSpeed;
```

## See Also

### Accessing Playback Settings
- [playShuffled](./playshuffled-93hn1.md)
  A Boolean value that indicates whether the media plays in a shuffled order.
- [resumePlayback](./resumeplayback-9zfyp.md)
  The resume playback setting at the time the user plays the media item.
- [var playbackRepeatMode: INPlaybackRepeatMode](./playbackrepeatmode.md)
  The repeat mode setting at the time the user plays the media item.
- [enum INPlaybackRepeatMode](../inplaybackrepeatmode.md)
  The possible repeat modes at the time the user plays the media item.
- [var playbackQueueLocation: INPlaybackQueueLocation](./playbackqueuelocation.md)
  The queue location for a media item during playback.
- [enum INPlaybackQueueLocation](../inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  An object that contains the search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent/playbackspeed-6ngbq)*