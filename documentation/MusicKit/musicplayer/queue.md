# MusicPlayer.Queue

**Framework**: MusicKit  
**Kind**: class  
**Role**: Class

A representation of the playback queue for a music player.

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
- [MusicPlayer.Queue.Entry](./queue/entry.md)
  An entry for the playback queue of the music player.
### Initializers
- [init<S>(S, startingAt: S.Element?)](./queue/init%28_,startingat%29.md)
  Creates a playback queue with playback queue entries.
- [init(album: Album, startingAt: Track)](./queue/init%28album,startingat%29.md)
  Creates a playback queue with an album and a specific track for the player to start playback.
- [init<S, PlayableMusicItemType>(for: S, startingAt: S.Element?)](./queue/init%28for,startingat%29.md)
  Creates a playback queue with playable music items.
- [init(playlist: Playlist, startingAt: Playlist.Entry)](./queue/init%28playlist,startingat%29.md)
  Creates a playback queue with a playlist and a specific playlist entry for the player to start playback.
### Instance Properties
- [var affectsListeningHistory: Bool](./queue/affectslisteninghistory.md)
  A Boolean value that indicates whether this playing this queue will affect the user’s listening history. Defaults to `true`.
- [var currentEntry: MusicPlayer.Queue.Entry?](./queue/currententry.md)
  The currently active entry in the playback queue.
### Instance Methods
- [func insert<PlayableMusicItemType>(PlayableMusicItemType, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](./queue/insert%28_,position%29-186ue.md)
  Inserts a playable music item into the playback queue.
- [func insert<S, PlayableMusicItemType>(S, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](./queue/insert%28_,position%29-228pb.md)
  Inserts playable music items into the playback queue.
- [func insert(MusicPlayer.Queue.Entry, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](./queue/insert%28_,position%29-3lv7k.md)
  Inserts an entry into the playback queue.
- [func insert<S>(S, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](./queue/insert%28_,position%29-58ohm.md)
  Inserts entries into the playback queue.
### Enumerations
- [MusicPlayer.Queue.EntryInsertionPosition](./queue/entryinsertionposition.md)
  An enumeration for the various supported positions for inserting playable music items or entries in the playback queue.

## Relationships

### Inherited By
- [ApplicationMusicPlayer.Queue](../applicationmusicplayer/queue-swift.class.md)
### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Observable](../../Observation/observable.md)
- [ObservableObject](../../Combine/observableobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue)*