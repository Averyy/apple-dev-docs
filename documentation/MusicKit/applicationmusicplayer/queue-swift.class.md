# ApplicationMusicPlayer.Queue

**Framework**: MusicKit  
**Kind**: class  
**Role**: Class

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
- [ApplicationMusicPlayer.Queue.Entries](./queue-swift.class/entries-swift.struct.md)
### Initializers
- [init<S>(S, startingAt: S.Element?)](./queue-swift.class/init%28_,startingat%29.md)
  Creates a playback queue with playback queue entries.
- [init(album: Album, startingAt: Track)](./queue-swift.class/init%28album,startingat%29.md)
  Creates a playback queue with an album and a specific track for the player to start playback.
- [init(arrayLiteral: any PlayableMusicItem...)](./queue-swift.class/init%28arrayliteral%29.md)
- [init<S, PlayableMusicItemType>(for: S, startingAt: S.Element?)](./queue-swift.class/init%28for,startingat%29.md)
  Creates a playback queue with playable music items.
- [init(playlist: Playlist, startingAt: Playlist.Entry)](./queue-swift.class/init%28playlist,startingat%29.md)
  Creates a playback queue with a playlist and a specific playlist entry for the player to start playback.
### Instance Properties
- [var entries: ApplicationMusicPlayer.Queue.Entries](./queue-swift.class/entries-swift.property.md)

## Relationships

### Inherits From
- [MusicPlayer.Queue](../musicplayer/queue.md)
### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Observable](../../Observation/observable.md)
- [ObservableObject](../../Combine/observableobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class)*