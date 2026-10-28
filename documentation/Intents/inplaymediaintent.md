# INPlayMediaIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intent that contains information about media playable from your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INPlayMediaIntent
```

```objc
@interface INPlayMediaIntent : INIntent
```

## Mentions

- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)
- [Creating an Intents App Extension](../SiriKit/creating-an-intents-app-extension.md)

## Overview

Use [`INPlayMediaIntent`](./inplaymediaintent.md) to donate songs, movies, and other media the user plays in your app, or to recommend upcoming media, such as new TV shows or podcast episodes. The system uses these donations to offer the user relevant search results and suggestions.

[`INPlayMediaIntent`](./inplaymediaintent.md) supports playing audio in the background. See `Enabling Background Audio` for more information about supporting background audio in your app.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (audio only) |
| Always requires unlocked device | No |

## Topics

### Creating a Play Media Intent
- [convenience init(mediaItems: [INMediaItem]?, mediaContainer: INMediaItem?, playShuffled: Bool?, playbackRepeatMode: INPlaybackRepeatMode, resumePlayback: Bool?, playbackQueueLocation: INPlaybackQueueLocation, playbackSpeed: Double?, mediaSearch: INMediaSearch?)](./inplaymediaintent/init%28mediaitems,mediacontainer,playshuffled,playbackrepeatmode,resumeplayback,playbackqueuelocation,playbackspeed,mediasearch%29.md)
  Creates an intent that describes media content such as a song, podcast episode, or movie.
- [- initWithMediaItems:mediaContainer:playShuffled:playbackRepeatMode:resumePlayback:playbackQueueLocation:playbackSpeed:mediaSearch:](./inplaymediaintent/initwithmediaitems_mediacontainer_playshuffled_playbackrepeatmode_resumeplayback_playbackqueuelocation_playbackspeed_mediasearch_.md)
  Initialize an intent that describes media content such as a song, podcast episode, or movie.
- [- initWithMediaItems:mediaContainer:playShuffled:playbackRepeatMode:resumePlayback:](./inplaymediaintent/initwithmediaitems_mediacontainer_playshuffled_playbackrepeatmode_resumeplayback_.md)
  Initializes an intent that describes media content such as a song, podcast episode, or movie.
### Accessing Media Items
- [var mediaContainer: INMediaItem?](./inplaymediaintent/mediacontainer.md)
  The media item container.
- [var mediaItems: [INMediaItem]?](./inplaymediaintent/mediaitems.md)
  The media content.
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
- [enum INPlaybackQueueLocation](./inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.
- [var mediaSearch: INMediaSearch?](./inplaymediaintent/mediasearch.md)
  An object that contains the search parameters.
- [playShuffled](./inplaymediaintent/playshuffled-93hn1.md)
  A Boolean value that indicates whether the media plays in a shuffled order.
- [resumePlayback](./inplaymediaintent/resumeplayback-9zfyp.md)
  The resume playback setting at the time the user plays the media item.
- [playbackSpeed](./inplaymediaintent/playbackspeed-6ngbq.md)
  The playback speed for a media item.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Playable Media Intents
- [protocol INPlayMediaIntentHandling](./inplaymediaintenthandling.md)
  The interface an object implements to confirm and handle play media intents.
- [class INPlayMediaIntentResponse](./inplaymediaintentresponse.md)
  An intents handler’s response to a play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent)*