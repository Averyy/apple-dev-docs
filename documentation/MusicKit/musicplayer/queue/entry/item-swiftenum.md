# MusicPlayer.Queue.Entry.Item

**Framework**: MusicKit  
**Kind**: enum

An item that corresponds to an entry in the playback queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Item
```

## Topics

### Operators
- [static func == (MusicPlayer.Queue.Entry.Item, MusicPlayer.Queue.Entry.Item) -> Bool](musicplayer/queue/entry/item-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MusicPlayer.Queue.Entry.Item.musicVideo(_:)](musicplayer/queue/entry/item-swift.enum/musicvideo(_:).md)
  An item that corresponds to a music video.
- [MusicPlayer.Queue.Entry.Item.song(_:)](musicplayer/queue/entry/item-swift.enum/song(_:).md)
  An item that corresponds to a song.
### Instance Properties
- [var hashValue: Int](musicplayer/queue/entry/item-swift.enum/hashvalue.md)
  The hash value.
- [var id: MusicItemID](musicplayer/queue/entry/item-swift.enum/id-swift.property.md)
  The unique identifier for the music player item.
- [var playParameters: PlayParameters?](musicplayer/queue/entry/item-swift.enum/playparameters.md)
  The parameters to use to play the item.
### Instance Methods
- [func hash(into: inout Hasher)](musicplayer/queue/entry/item-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicPlayer.Queue.Entry.Item.ID](musicplayer/queue/entry/item-swift.enum/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musicplayer/queue/entry/item-swift.enum/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musicplayer/queue/entry/item-swift.enum/customstringconvertible-implementations.md)
- [Decodable Implementations](musicplayer/queue/entry/item-swift.enum/decodable-implementations.md)
- [Encodable Implementations](musicplayer/queue/entry/item-swift.enum/encodable-implementations.md)
- [Equatable Implementations](musicplayer/queue/entry/item-swift.enum/equatable-implementations.md)
- [MusicItem Implementations](musicplayer/queue/entry/item-swift.enum/musicitem-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MusicItem](musicitem.md)
- [MusicPropertyContainer](musicpropertycontainer.md)
- [PlayableMusicItem](playablemusicitem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/entry/item-swift.enum)*