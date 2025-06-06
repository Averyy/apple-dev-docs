# MusicVideoFilter

**Framework**: MusicKit  
**Kind**: protocol

Music video properties your app uses as a filter for a catalog resource request.

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
protocol MusicVideoFilter
```

## Topics

### Instance Properties
- [var id: MusicItemID](musicvideofilter/id.md)
  The unique identifier for the music video.
- [var isrc: String?](musicvideofilter/isrc.md)
  The International Standard Recording Code (ISRC) for the music video.

## See Also

- [struct MusicCatalogResourceRequest](musiccatalogresourcerequest.md)
  A request that your app uses to fetch items from the Apple Music catalog using a filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicvideofilter)*