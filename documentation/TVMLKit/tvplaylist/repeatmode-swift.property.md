# repeatMode

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A mode that determines how media items are replayed.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var repeatMode: TVPlaylist.RepeatMode { get }
```

```objc
@property (nonatomic, assign, readonly) TVPlaylistRepeatMode repeatMode;
```

## See Also

### Retrieving Playlist Information
- [var mediaItems: [TVMediaItem]](./mediaitems.md)
  An array of media items contained in the playlist.
- [var userInfo: [String : Any]?](./userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a playlist.
- [TVPlaylist.RepeatMode](./repeatmode-swift.enum.md)
  The modes that indicate how or whether media items can be replayed.
- [var endAction: TVPlaylist.EndAction](./endaction-swift.property.md)
  An action that causes media playback to end.
- [TVPlaylist.EndAction](./endaction-swift.enum.md)
  The actions that cause media playback to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist/repeatmode-swift.property)*