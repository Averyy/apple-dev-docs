# MusicPropertyContainer

**Framework**: MusicKit  
**Kind**: protocol

A protocol for music items that allow loading additional properties that you can fetch asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol MusicPropertyContainer
```

## Topics

### Instance Methods
- [func with([PartialMusicAsyncProperty<Self>]) async throws -> Self](musicpropertycontainer/with(_:).md)
  Loads a new instance of the music item that includes the specified properties.
- [func with([PartialMusicAsyncProperty<Self>], preferredSource: MusicPropertySource) async throws -> Self](musicpropertycontainer/with(_:preferredsource:)-8ec7p.md)
  Loads a new instance of the music item that includes the specified properties.
- [func with(PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self](musicpropertycontainer/with(_:preferredsource:)-9wqhc.md)
  Loads a new instance of the music item that includes the specified properties.

## Relationships

### Conforming Types
- [Album](album.md)
- [Artist](artist.md)
- [Curator](curator.md)
- [Genre](genre.md)
- [MusicPlayer.Queue.Entry.Item](musicplayer/queue/entry/item-swift.enum.md)
- [MusicVideo](musicvideo.md)
- [Playlist](playlist.md)
- [Playlist.Entry](playlist/entry.md)
- [Playlist.Entry.Item](playlist/entry/item-swift.enum.md)
- [RadioShow](radioshow.md)
- [RecordLabel](recordlabel.md)
- [Song](song.md)
- [Station](station.md)
- [Track](track.md)

## See Also

- [protocol MusicItem](musicitem.md)
  A protocol with basic requirements for music items.
- [struct MusicItemID](musicitemid.md)
  An object that represents a unique identifier for a music item.
- [struct MusicItemCollection](musicitemcollection.md)
  A collection of music items.
- [class MusicRelationshipProperty](musicrelationshipproperty.md)
  An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- [class MusicExtendedAttributeProperty](musicextendedattributeproperty.md)
  An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- [class MusicAttributeProperty](musicattributeproperty.md)
  An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- [class PartialMusicAsyncProperty](partialmusicasyncproperty.md)
  A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- [class PartialMusicProperty](partialmusicproperty.md)
  A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- [class AnyMusicProperty](anymusicproperty.md)
  A type-erased identifier for a music item property, from any root type to any resulting value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicpropertycontainer)*