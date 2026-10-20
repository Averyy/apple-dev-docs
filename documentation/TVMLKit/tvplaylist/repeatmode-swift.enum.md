# TVPlaylist.RepeatMode

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

The modes that indicate how or whether media items can be replayed.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum RepeatMode
```

```c
enum TVPlaylistRepeatMode : NSInteger;
```

## Topics

### Replay Modes
- [TVPlaylist.RepeatMode.all](./repeatmode-swift.enum/all.md)
  Replay all of the media items in the playlist.
- [TVPlaylist.RepeatMode.one](./repeatmode-swift.enum/one.md)
  Replay the currently playing media item.
- [TVPlaylist.RepeatMode.none](./repeatmode-swift.enum/none.md)
  Replay none of the media items in the playlist.
### Initializers
- [init?(rawValue: Int)](./repeatmode-swift.enum/init%28rawvalue%29.md)

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
- [var endAction: TVPlaylist.EndAction](./endaction-swift.property.md)
  An action that causes media playback to end.
- [TVPlaylist.EndAction](./endaction-swift.enum.md)
  The actions that cause media playback to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist/repeatmode-swift.enum)*