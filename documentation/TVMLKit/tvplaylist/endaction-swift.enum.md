# TVPlaylist.EndAction

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

The actions that cause media playback to end.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum EndAction
```

```c
enum TVPlaylistEndAction : NSInteger;
```

## Topics

### End Playback Reasons
- [TVPlaylist.EndAction.stop](./endaction-swift.enum/stop.md)
  The player has stopped playback
- [TVPlaylist.EndAction.pause](./endaction-swift.enum/pause.md)
  The player has paused playback.
- [TVPlaylist.EndAction.waitForMoreItems](./endaction-swift.enum/waitformoreitems.md)
  The player is waiting for more media items.
### Initializers
- [init?(rawValue: Int)](./endaction-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving Playlist Information
- [var mediaItems: [TVMediaItem]](./mediaitems.md)
  An array of media items contained in the playlist.
- [var userInfo: [String : Any]?](./userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a playlist.
- [var repeatMode: TVPlaylist.RepeatMode](./repeatmode-swift.property.md)
  A mode that determines how media items are replayed.
- [TVPlaylist.RepeatMode](./repeatmode-swift.enum.md)
  The modes that indicate how or whether media items can be replayed.
- [var endAction: TVPlaylist.EndAction](./endaction-swift.property.md)
  An action that causes media playback to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist/endaction-swift.enum)*