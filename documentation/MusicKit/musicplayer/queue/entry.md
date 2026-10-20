# MusicPlayer.Queue.Entry

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

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

### Initializers
- [init(any PlayableMusicItem, startTime: TimeInterval?, endTime: TimeInterval?)](./entry/init%28_,starttime,endtime%29.md)
  Creates an entry of the playback queue with a playable music item, and optional start and end times.
### Instance Properties
- [var artwork: Artwork?](./entry/artwork.md)
  The artwork of this entry of the playback queue.
- [var endTime: TimeInterval?](./entry/endtime.md)
  An optional end time for this entry of the playback queue.
- [let id: String](./entry/id.md)
  The unique identifier of this entry of the playback queue.
- [var isTransient: Bool](./entry/istransient.md)
  A Boolean value that indicates whether this entry of the playback queue has a transient music item.
- [var item: MusicPlayer.Queue.Entry.Item?](./entry/item-swift.property.md)
  A music item that corresponds to this entry of the playback queue, such as a song or a music video.
- [var startTime: TimeInterval?](./entry/starttime.md)
  An optional start time for this entry of the playback queue.
- [var subtitle: String?](./entry/subtitle.md)
  The subtitle of this entry of the playback queue.
- [var title: String](./entry/title.md)
  The title of this entry of the playback queue.
- [var transientItem: (any PlayableMusicItem)?](./entry/transientitem.md)
  A music item that corresponds to a recently inserted entry in the playback queue that has underlying items the music player still needs to resolve.
### Enumerations
- [MusicPlayer.Queue.Entry.Item](./entry/item-swift.enum.md)
  An item that corresponds to an entry in the playback queue.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Identifiable](../../../Swift/identifiable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/queue/entry)*