# playbackQueueLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The queue location for a media item during playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var playbackQueueLocation: INPlaybackQueueLocation { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INPlaybackQueueLocation playbackQueueLocation;
```

*macOS*

```objc
@property (atomic, assign, readonly) INPlaybackQueueLocation playbackQueueLocation;
```

## See Also

### Accessing Playback Settings
- [var playShuffled: Bool?](./playshuffled-2btex.md)
  A Boolean value that indicates whether the media plays in a shuffled order.
- [var resumePlayback: Bool?](./resumeplayback-1xw6r.md)
  The resume playback setting at the time the user plays the media item.
- [var playbackRepeatMode: INPlaybackRepeatMode](./playbackrepeatmode.md)
  The repeat mode setting at the time the user plays the media item.
- [enum INPlaybackRepeatMode](../inplaybackrepeatmode.md)
  The possible repeat modes at the time the user plays the media item.
- [var playbackSpeed: Double?](./playbackspeed-17r2t.md)
  The playback speed for a media item.
- [enum INPlaybackQueueLocation](../inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  An object that contains the search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent/playbackqueuelocation)*