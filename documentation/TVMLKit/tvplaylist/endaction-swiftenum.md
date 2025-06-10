# TVPlaylist.EndAction

**Framework**: TVMLKit  
**Kind**: enum

The actions that cause media playback to end.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
enum EndAction
```

## Topics

### End Playback Reasons
- [TVPlaylist.EndAction.stop](tvplaylist/endaction-swift.enum/stop.md)
  The player has stopped playback
- [TVPlaylist.EndAction.pause](tvplaylist/endaction-swift.enum/pause.md)
  The player has paused playback.
- [TVPlaylist.EndAction.waitForMoreItems](tvplaylist/endaction-swift.enum/waitformoreitems.md)
  The player is waiting for more media items.
### Initializers
- [init?(rawValue: Int)](tvplaylist/endaction-swift.enum/init(rawvalue:).md)

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
- [TVPlaylist.RepeatMode](tvplaylist/repeatmode-swift.enum.md)
  The modes that indicate how or whether media items can be replayed.
- [var endAction: TVPlaylist.EndAction](tvplaylist/endaction-swift.property.md)
  An action that causes media playback to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaylist/endaction-swift.enum)*