# MusicPlayer.Queue.EntryInsertionPosition

**Framework**: MusicKit  
**Kind**: enum

An enumeration for the various supported positions for inserting playable music items or entries in the playback queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum EntryInsertionPosition
```

## Topics

### Operators
- [static func == (MusicPlayer.Queue.EntryInsertionPosition, MusicPlayer.Queue.EntryInsertionPosition) -> Bool](musicplayer/queue/entryinsertionposition/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MusicPlayer.Queue.EntryInsertionPosition.afterCurrentEntry](musicplayer/queue/entryinsertionposition/aftercurrententry.md)
  A position that allows prepending entries in the playback queue, similar to the Play Next feature in the Music app.
- [MusicPlayer.Queue.EntryInsertionPosition.tail](musicplayer/queue/entryinsertionposition/tail.md)
  A position that allows appending entries in the playback queue, similar to the Play Later feature in the Music app.
### Instance Properties
- [var hashValue: Int](musicplayer/queue/entryinsertionposition/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](musicplayer/queue/entryinsertionposition/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](musicplayer/queue/entryinsertionposition/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/entryinsertionposition)*