# TVPlaylist.RepeatMode

**Framework**: TVMLKit  
**Kind**: enum

The modes that indicate how or whether media items can be replayed.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
enum RepeatMode
```

## Topics

### Replay Modes
- [TVPlaylist.RepeatMode.all](tvplaylist/repeatmode-swift.enum/all.md)
  Replay all of the media items in the playlist.
- [TVPlaylist.RepeatMode.one](tvplaylist/repeatmode-swift.enum/one.md)
  Replay the currently playing media item.
- [TVPlaylist.RepeatMode.none](tvplaylist/repeatmode-swift.enum/none.md)
  Replay none of the media items in the playlist.
### Initializers
- [init?(rawValue: Int)](tvplaylist/repeatmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var mediaItems: [TVMediaItem]](tvplaylist/mediaitems.md)
  An array of media items contained in the playlist.
- [var userInfo: [String : Any]?](tvplaylist/userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a playlist.
- [var repeatMode: TVPlaylist.RepeatMode](tvplaylist/repeatmode-swift.property.md)
  A mode that determines how media items are replayed.
- [var endAction: TVPlaylist.EndAction](tvplaylist/endaction-swift.property.md)
  An action that causes media playback to end.
- [TVPlaylist.EndAction](tvplaylist/endaction-swift.enum.md)
  The actions that cause media playback to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist/repeatmode-swift.enum)*