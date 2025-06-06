# MusicPlayer.Queue

**Framework**: MusicKit  
**Kind**: class

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
- [MusicPlayer.Queue.Entry](musicplayer/queue/entry.md)
  An entry for the playback queue of the music player.
### Initializers
- [init<S>(S, startingAt: S.Element?)](musicplayer/queue/init(_:startingat:).md)
  Creates a playback queue with playback queue entries.
- [init(album: Album, startingAt: Track)](musicplayer/queue/init(album:startingat:).md)
  Creates a playback queue with an album and a specific track for the player to start playback.
- [convenience init(arrayLiteral: any PlayableMusicItem...)](musicplayer/queue/init(arrayliteral:).md)
  Creates an instance initialized with the given elements.
- [init<S, PlayableMusicItemType>(for: S, startingAt: S.Element?)](musicplayer/queue/init(for:startingat:).md)
  Creates a playback queue with playable music items.
- [init(playlist: Playlist, startingAt: Playlist.Entry)](musicplayer/queue/init(playlist:startingat:).md)
  Creates a playback queue with a playlist and a specific playlist entry for the player to start playback.
### Instance Properties
- [var currentEntry: MusicPlayer.Queue.Entry?](musicplayer/queue/currententry.md)
  The currently active entry in the playback queue.
- [var objectWillChange: AnyPublisher<Void, Never>](musicplayer/queue/objectwillchange.md)
  A publisher that emits before the object has changed.
### Instance Methods
- [func insert<PlayableMusicItemType>(PlayableMusicItemType, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](musicplayer/queue/insert(_:position:)-186ue.md)
  Inserts a playable music item into the playback queue.
- [func insert<S, PlayableMusicItemType>(S, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](musicplayer/queue/insert(_:position:)-228pb.md)
  Inserts playable music items into the playback queue.
- [func insert(MusicPlayer.Queue.Entry, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](musicplayer/queue/insert(_:position:)-3lv7k.md)
  Inserts an entry into the playback queue.
- [func insert<S>(S, position: MusicPlayer.Queue.EntryInsertionPosition) async throws](musicplayer/queue/insert(_:position:)-58ohm.md)
  Inserts entries into the playback queue.
### Type Aliases
- [MusicPlayer.Queue.ArrayLiteralElement](musicplayer/queue/arrayliteralelement.md)
  The type of the elements of an array literal.
- [MusicPlayer.Queue.ObjectWillChangePublisher](musicplayer/queue/objectwillchangepublisher.md)
  The type of publisher that emits before the object has changed.
### Enumerations
- [MusicPlayer.Queue.EntryInsertionPosition](musicplayer/queue/entryinsertionposition.md)
  An enumeration for the various supported positions for inserting playable music items or entries in the playback queue.
### Default Implementations
- [Equatable Implementations](musicplayer/queue/equatable-implementations.md)
- [Hashable Implementations](musicplayer/queue/hashable-implementations.md)

## Relationships

### Inherited By
- [ApplicationMusicPlayer.Queue](applicationmusicplayer/queue-swift.class.md)
### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue)*