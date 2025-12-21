# MusicCatalogSearchResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a catalog search request.

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
struct MusicCatalogSearchResponse
```

## Topics

### Instance Properties
- [let albums: MusicItemCollection<Album>](musiccatalogsearchresponse/albums.md)
  A collection of albums.
- [let artists: MusicItemCollection<Artist>](musiccatalogsearchresponse/artists.md)
  A collection of artists.
- [let curators: MusicItemCollection<Curator>](musiccatalogsearchresponse/curators.md)
  A collection of curators.
- [let musicVideos: MusicItemCollection<MusicVideo>](musiccatalogsearchresponse/musicvideos.md)
  A collection of music videos.
- [let playlists: MusicItemCollection<Playlist>](musiccatalogsearchresponse/playlists.md)
  A collection of playlists.
- [let radioShows: MusicItemCollection<RadioShow>](musiccatalogsearchresponse/radioshows.md)
  A collection of radio shows.
- [let recordLabels: MusicItemCollection<RecordLabel>](musiccatalogsearchresponse/recordlabels.md)
  A collection of record labels.
- [let songs: MusicItemCollection<Song>](musiccatalogsearchresponse/songs.md)
  A collection of songs.
- [let stations: MusicItemCollection<Station>](musiccatalogsearchresponse/stations.md)
  A collection of stations.
- [let topResults: MusicItemCollection<MusicCatalogSearchResponse.TopResult>](musiccatalogsearchresponse/topresults.md)
  A collection of top results.
### Enumerations
- [MusicCatalogSearchResponse.TopResult](musiccatalogsearchresponse/topresult.md)
  An item that represents one of the top results in a catalog search response.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct MusicCatalogSearchRequest](musiccatalogsearchrequest.md)
  A request that your app uses to fetch items from the Apple Music catalog using a search term.
- [protocol MusicCatalogSearchable](musiccatalogsearchable.md)
  A protocol for music items that your app can fetch by using a catalog search request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse)*