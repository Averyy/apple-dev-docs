# mediaItems

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

An array of media items contained in the playlist.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var mediaItems: [TVMediaItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<TVMediaItem *> * mediaItems;
```

## See Also

### Retrieving Playlist Information
- [var userInfo: [String : Any]?](./userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a playlist.
- [var repeatMode: TVPlaylist.RepeatMode](./repeatmode-swift.property.md)
  A mode that determines how media items are replayed.
- [TVPlaylist.RepeatMode](./repeatmode-swift.enum.md)
  The modes that indicate how or whether media items can be replayed.
- [var endAction: TVPlaylist.EndAction](./endaction-swift.property.md)
  An action that causes media playback to end.
- [TVPlaylist.EndAction](./endaction-swift.enum.md)
  The actions that cause media playback to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist/mediaitems)*