# ApplicationMusicPlayer.Queue

**Framework**: MusicKit  
**Kind**: class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class Queue
```

## Topics

### Structures
- [ApplicationMusicPlayer.Queue.Entries](applicationmusicplayer/queue-swift.class/entries-swift.struct.md)
### Initializers
- [init<S>(S, startingAt: S.Element?)](applicationmusicplayer/queue-swift.class/init(_:startingat:).md)
  Creates a playback queue with playback queue entries.
- [init(album: Album, startingAt: Track)](applicationmusicplayer/queue-swift.class/init(album:startingat:).md)
  Creates a playback queue with an album and a specific track for the player to start playback.
- [init(arrayLiteral: any PlayableMusicItem...)](applicationmusicplayer/queue-swift.class/init(arrayliteral:).md)
- [init<S, PlayableMusicItemType>(for: S, startingAt: S.Element?)](applicationmusicplayer/queue-swift.class/init(for:startingat:).md)
  Creates a playback queue with playable music items.
- [init(playlist: Playlist, startingAt: Playlist.Entry)](applicationmusicplayer/queue-swift.class/init(playlist:startingat:).md)
  Creates a playback queue with a playlist and a specific playlist entry for the player to start playback.
### Instance Properties
- [var entries: ApplicationMusicPlayer.Queue.Entries](applicationmusicplayer/queue-swift.class/entries-swift.property.md)

## Relationships

### Inherits From
- [MusicPlayer.Queue](musicplayer/queue.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class)*