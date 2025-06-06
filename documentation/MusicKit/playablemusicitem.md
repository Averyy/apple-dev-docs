# PlayableMusicItem

**Framework**: MusicKit  
**Kind**: protocol

A set of properties that a music player uses to initiate playback for a music item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol PlayableMusicItem : MusicItem
```

## Topics

### Instance Properties
- [var playParameters: PlayParameters?](playablemusicitem/playparameters.md)
  The parameters to use to play the music item.

## Relationships

### Inherits From
- [MusicItem](musicitem.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [Album](album.md)
- [MusicPlayer.Queue.Entry.Item](musicplayer/queue/entry/item-swift.enum.md)
- [Playlist](playlist.md)
- [Playlist.Entry](playlist/entry.md)
- [Playlist.Entry.Item](playlist/entry/item-swift.enum.md)
- [RecentlyPlayedMusicItem](recentlyplayedmusicitem.md)
- [Song](song.md)
- [Station](station.md)
- [Track](track.md)

## See Also

- [class ApplicationMusicPlayer](applicationmusicplayer.md)
  An object your app uses to play music in a way that doesn’t affect the Music app’s state.
- [class SystemMusicPlayer](systemmusicplayer.md)
  An object your app uses to play music by controlling the Music app’s state.
- [class MusicPlayer](musicplayer.md)
  An object your app uses to play music.
- [struct PlayParameters](playparameters.md)
  An opaque object that represents parameters to initiate playback of a playable music item using a music player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playablemusicitem)*