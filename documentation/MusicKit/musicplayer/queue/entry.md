# MusicPlayer.Queue.Entry

**Framework**: MusicKit  
**Kind**: struct

An entry for the playback queue of the music player.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Entry
```

## Topics

### Operators
- [static func == (MusicPlayer.Queue.Entry, MusicPlayer.Queue.Entry) -> Bool](musicplayer/queue/entry/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(any PlayableMusicItem, startTime: TimeInterval?, endTime: TimeInterval?)](musicplayer/queue/entry/init(_:starttime:endtime:).md)
  Creates an entry of the playback queue with a playable music item, and optional start and end times.
### Instance Properties
- [var artwork: Artwork?](musicplayer/queue/entry/artwork.md)
  The artwork of this entry of the playback queue.
- [var description: String](musicplayer/queue/entry/description.md)
  A textual representation of this instance.
- [var endTime: TimeInterval?](musicplayer/queue/entry/endtime.md)
  An optional end time for this entry of the playback queue.
- [var hashValue: Int](musicplayer/queue/entry/hashvalue.md)
  The hash value.
- [let id: String](musicplayer/queue/entry/id-swift.property.md)
  The unique identifier of this entry of the playback queue.
- [var isTransient: Bool](musicplayer/queue/entry/istransient.md)
  A Boolean value that indicates whether this entry of the playback queue has a transient music item.
- [var item: MusicPlayer.Queue.Entry.Item?](musicplayer/queue/entry/item-swift.property.md)
  A music item that corresponds to this entry of the playback queue, such as a song or a music video.
- [var startTime: TimeInterval?](musicplayer/queue/entry/starttime.md)
  An optional start time for this entry of the playback queue.
- [var subtitle: String?](musicplayer/queue/entry/subtitle.md)
  The subtitle of this entry of the playback queue.
- [var title: String](musicplayer/queue/entry/title.md)
  The title of this entry of the playback queue.
- [var transientItem: (any PlayableMusicItem)?](musicplayer/queue/entry/transientitem.md)
  A music item that corresponds to a recently inserted entry in the playback queue that has underlying items the music player still needs to resolve.
### Instance Methods
- [func hash(into: inout Hasher)](musicplayer/queue/entry/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [MusicPlayer.Queue.Entry.ID](musicplayer/queue/entry/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Enumerations
- [MusicPlayer.Queue.Entry.Item](musicplayer/queue/entry/item-swift.enum.md)
  An item that corresponds to an entry in the playback queue.
### Default Implementations
- [Equatable Implementations](musicplayer/queue/entry/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/entry)*