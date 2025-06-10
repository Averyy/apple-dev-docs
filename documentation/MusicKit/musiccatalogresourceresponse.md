# MusicCatalogResourceResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a catalog resource request.

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
struct MusicCatalogResourceResponse<MusicItemType> where MusicItemType : MusicItem
```

## Topics

### Instance Properties
- [let items: MusicItemCollection<MusicItemType>](musiccatalogresourceresponse/items.md)
  A collection of items matching the filter used in the originating [`MusicCatalogResourceRequest`](musiccatalogresourcerequest.md).
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiccatalogresourceresponse/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiccatalogresourceresponse/customstringconvertible-implementations.md)
- [Decodable Implementations](musiccatalogresourceresponse/decodable-implementations.md)
- [Encodable Implementations](musiccatalogresourceresponse/encodable-implementations.md)
- [Equatable Implementations](musiccatalogresourceresponse/equatable-implementations.md)
- [Hashable Implementations](musiccatalogresourceresponse/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MusicCatalogResourceRequest](musiccatalogresourcerequest.md)
  A request that your app uses to fetch items from the Apple Music catalog using a filter.
- [protocol AlbumFilter](albumfilter.md)
  Album properties your app uses as a filter for a catalog resource request.
- [protocol ArtistFilter](artistfilter.md)
  Artist properties your app uses as a filter for a catalog resource request.
- [protocol CuratorFilter](curatorfilter.md)
  Curator properties your app uses as a filter for a catalog resource request.
- [protocol GenreFilter](genrefilter.md)
  Genre properties your app uses as a filter for a catalog resource request.
- [protocol MusicVideoFilter](musicvideofilter.md)
  Music video properties your app uses as a filter for a catalog resource request.
- [protocol PlaylistFilter](playlistfilter.md)
  Playlist properties your app uses as a filter for a catalog resource request.
- [protocol RadioShowFilter](radioshowfilter.md)
  Radio Show properties your app uses as a filter for a catalog resource request.
- [protocol RecordLabelFilter](recordlabelfilter.md)
  The set of record label properties your app uses as a filter for a catalog resource request.
- [protocol SongFilter](songfilter.md)
  Song properties your app uses as a filter for a catalog resource request.
- [protocol StationFilter](stationfilter.md)
  The set of station properties your app uses as a filter for a catalog resource request.
- [protocol FilterableMusicItem](filterablemusicitem.md)
  A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogresourceresponse)*