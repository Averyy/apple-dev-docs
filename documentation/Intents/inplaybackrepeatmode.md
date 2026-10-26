# INPlaybackRepeatMode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

The possible repeat modes at the time the user plays the media item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum INPlaybackRepeatMode
```

```c
enum INPlaybackRepeatMode : NSInteger;
```

## Topics

### Repeat Modes
- [INPlaybackRepeatMode.unknown](./inplaybackrepeatmode/unknown.md)
  Unknown repeat mode.
- [INPlaybackRepeatMode.none](./inplaybackrepeatmode/none.md)
  A mode that doesn’t repeat media items.
- [INPlaybackRepeatMode.all](./inplaybackrepeatmode/all.md)
  A mode that repeats all media items within a media container.
- [INPlaybackRepeatMode.one](./inplaybackrepeatmode/one.md)
  A mode that repeats the current media item within a media container.
### Initializers
- [init?(rawValue: Int)](./inplaybackrepeatmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Playback Settings
- [var playShuffled: Bool?](./inplaymediaintent/playshuffled-2btex.md)
  A Boolean value that indicates whether the media plays in a shuffled order.
- [var resumePlayback: Bool?](./inplaymediaintent/resumeplayback-1xw6r.md)
  The resume playback setting at the time the user plays the media item.
- [var playbackRepeatMode: INPlaybackRepeatMode](./inplaymediaintent/playbackrepeatmode.md)
  The repeat mode setting at the time the user plays the media item.
- [var playbackSpeed: Double?](./inplaymediaintent/playbackspeed-17r2t.md)
  The playback speed for a media item.
- [var playbackQueueLocation: INPlaybackQueueLocation](./inplaymediaintent/playbackqueuelocation.md)
  The queue location for a media item during playback.
- [enum INPlaybackQueueLocation](./inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.
- [var mediaSearch: INMediaSearch?](./inplaymediaintent/mediasearch.md)
  An object that contains the search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackrepeatmode)*