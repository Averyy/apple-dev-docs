# INPlaybackQueueLocation

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the playback queue location for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INPlaybackQueueLocation
```

```c
enum INPlaybackQueueLocation : NSInteger;
```

## Topics

### Constants
- [INPlaybackQueueLocation.unknown](./inplaybackqueuelocation/unknown.md)
  A response that indicates the system doesn’t know where to place the media item.
- [INPlaybackQueueLocation.now](./inplaybackqueuelocation/now.md)
  A response that tells the system to play the item immediately, interrupting any currently playing media.
- [INPlaybackQueueLocation.next](./inplaybackqueuelocation/next.md)
  A response that tells the system to play the media item after the currently playing media item finishes.
- [INPlaybackQueueLocation.later](./inplaybackqueuelocation/later.md)
  A response that tells the system to add the media item to the end of the playback queue.
### Initializers
- [init?(rawValue: Int)](./inplaybackqueuelocation/init%28rawvalue%29.md)

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
- [enum INPlaybackRepeatMode](./inplaybackrepeatmode.md)
  The possible repeat modes at the time the user plays the media item.
- [var playbackSpeed: Double?](./inplaymediaintent/playbackspeed-17r2t.md)
  The playback speed for a media item.
- [var playbackQueueLocation: INPlaybackQueueLocation](./inplaymediaintent/playbackqueuelocation.md)
  The queue location for a media item during playback.
- [var mediaSearch: INMediaSearch?](./inplaymediaintent/mediasearch.md)
  An object that contains the search parameters.
- [playShuffled](./inplaymediaintent/playshuffled-93hn1.md)
  A Boolean value that indicates whether the media plays in a shuffled order.
- [resumePlayback](./inplaymediaintent/resumeplayback-9zfyp.md)
  The resume playback setting at the time the user plays the media item.
- [playbackSpeed](./inplaymediaintent/playbackspeed-6ngbq.md)
  The playback speed for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackqueuelocation)*