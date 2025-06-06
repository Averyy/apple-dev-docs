# TVPlaylist

**Framework**: TVMLKit  
**Kind**: class

A collection of media items associated with the Apple TV JavaScript player.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVPlaylist
```

#### Overview

A `TVPlaylist` object contains read-only information about a playlist associated with the JavaScript player. You can use this information with your own custom [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) objects exposed through a [`TVPlayer`](tvplayer.md) object. For example, you can retrieve album information from the JavaScript player and play the track through a `TVPlayer` object.

## Topics

### Retrieving Playlist Information
- [var mediaItems: [TVMediaItem]](tvplaylist/mediaitems.md)
  An array of media items contained in the playlist.
- [var userInfo: [String : Any]?](tvplaylist/userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a playlist.
- [var repeatMode: TVPlaylist.RepeatMode](tvplaylist/repeatmode-swift.property.md)
  A mode that determines how media items are replayed.
- [TVPlaylist.RepeatMode](tvplaylist/repeatmode-swift.enum.md)
  The modes that indicate how or whether media items can be replayed.
- [var endAction: TVPlaylist.EndAction](tvplaylist/endaction-swift.property.md)
  An action that causes media playback to end.
- [TVPlaylist.EndAction](tvplaylist/endaction-swift.enum.md)
  The actions that cause media playback to end.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVMediaItem](tvmediaitem.md)
  A single audio or video item associated with the Apple TV JavaScript player.
- [class TVPlayer](tvplayer.md)
  A customizable native media player used to control playback from the JavaScript player used in an Apple TV client-server app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist)*