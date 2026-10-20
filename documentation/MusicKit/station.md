# Station

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

A music item that represents a station.

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
struct Station
```

## Topics

### Instance Properties
- [var artwork: Artwork?](./station/artwork.md)
  The station artwork.
- [var contentRating: ContentRating?](./station/contentrating.md)
  The rating of the content that potentially plays while playing the station.
- [var duration: TimeInterval?](./station/duration.md)
  The duration of the stream.
- [var editorialNotes: EditorialNotes?](./station/editorialnotes.md)
  The notes about the station that appear in the Music app.
- [var episodeNumber: Int?](./station/episodenumber.md)
  The episode number of the station.
- [let id: MusicItemID](./station/id.md)
  The unique identifier for the station.
- [var isLive: Bool](./station/islive.md)
  A Boolean value that indicates whether the station is live.
- [var name: String](./station/name.md)
  The name of the station.
- [var playParameters: PlayParameters?](./station/playparameters.md)
  The parameters to use to play the station.
- [var stationProviderName: String?](./station/stationprovidername.md)
  The name of the entity that provides the station.
- [var url: URL?](./station/url.md)
  The URL for the station.
### Default Implementations
- [FilterableMusicItem Implementations](./station/filterablemusicitem-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [FilterableMusicItem](./filterablemusicitem.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [MusicCatalogSearchable](./musiccatalogsearchable.md)
- [MusicItem](./musicitem.md)
- [MusicPersonalRecommendationItem](./musicpersonalrecommendationitem.md)
- [MusicPropertyContainer](./musicpropertycontainer.md)
- [MusicRecentlyPlayedRequestable](./musicrecentlyplayedrequestable.md)
- [PlayableMusicItem](./playablemusicitem.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Music Items
- [struct Album](./album.md)
  A music item that represents an album.
- [struct Artist](./artist.md)
  A music item that represents an artist.
- [struct Curator](./curator.md)
  A music item that represents a curator.
- [struct Genre](./genre.md)
  A music item that represents a genre.
- [struct MusicVideo](./musicvideo.md)
  A music item that represents a music video.
- [struct Playlist](./playlist.md)
  A music item that represents a playlist.
- [struct RadioShow](./radioshow.md)
  A music item that represents a radio show.
- [struct RecordLabel](./recordlabel.md)
  A music item that represents a record label.
- [struct Song](./song.md)
  A music item that represents a song.
- [enum Track](./track.md)
  A music item that represents a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/station)*