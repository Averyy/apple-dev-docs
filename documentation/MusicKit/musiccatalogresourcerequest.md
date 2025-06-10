# MusicCatalogResourceRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch items from the Apple Music catalog using a filter.

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
struct MusicCatalogResourceRequest<MusicItemType> where MusicItemType : MusicItem, MusicItemType : Decodable
```

## Topics

### Initializers
- [init()](musiccatalogresourcerequest/init.md)
  Creates a request to fetch top-level items in the Apple Music catalog.
- [init<Value>(matching: KeyPath<MusicItemType.FilterType, Value>, equalTo: Value)](musiccatalogresourcerequest/init(matching:equalto:).md)
  Creates a request to fetch items using a filter that matches a specific value.
- [init<Value>(matching: KeyPath<MusicItemType.FilterType, Value>, memberOf: [Value])](musiccatalogresourcerequest/init(matching:memberof:).md)
  Creates a request to fetch items using a filter that matches any value from an array of possible values.
### Instance Properties
- [var limit: Int?](musiccatalogresourcerequest/limit.md)
  A limit for the number of items to return in the catalog resource response.
- [var properties: [PartialMusicAsyncProperty<MusicItemType>]](musiccatalogresourcerequest/properties.md)
  A list of properties which the resource request will fetch for each music item in the response.
### Instance Methods
- [func response() async throws -> MusicCatalogResourceResponse<MusicItemType>](musiccatalogresourcerequest/response.md)
  Fetches items from the Apple Music catalog that match a specific filter.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MusicCatalogResourceResponse](musiccatalogresourceresponse.md)
  An object that contains results for a catalog resource request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest)*