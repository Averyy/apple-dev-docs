# INMediaItemType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

The type of content the media item describes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum INMediaItemType
```

```c
enum INMediaItemType : NSInteger;
```

## Topics

### Stations
- [INMediaItemType.station](./inmediaitemtype/station.md)
  A media type that indicates a station.
- [INMediaItemType.radioStation](./inmediaitemtype/radiostation.md)
  A media type that indicates a radio station.
- [INMediaItemType.algorithmicRadioStation](./inmediaitemtype/algorithmicradiostation.md)
  A media type that indicates related content.
### Music
- [INMediaItemType.album](./inmediaitemtype/album.md)
  A media type that indicates an album.
- [INMediaItemType.artist](./inmediaitemtype/artist.md)
  A media type that indicates an artist.
- [INMediaItemType.musicStation](./inmediaitemtype/musicstation.md)
  A media type that indicates a music station.
- [INMediaItemType.musicVideo](./inmediaitemtype/musicvideo.md)
  A media type that indicates a music video.
- [INMediaItemType.playlist](./inmediaitemtype/playlist.md)
  A media type that indicates a playlist of music.
- [INMediaItemType.song](./inmediaitemtype/song.md)
  A media type that indicates a song.
- [INMediaItemType.music](./inmediaitemtype/music.md)
  A media type that indicates music.
### Movie and TV
- [INMediaItemType.movie](./inmediaitemtype/movie.md)
  A media type that indicates a movie.
- [INMediaItemType.tvShow](./inmediaitemtype/tvshow.md)
  A media type that indicates a TV show or series.
- [INMediaItemType.tvShowEpisode](./inmediaitemtype/tvshowepisode.md)
  A media type that indicates an episode of a TV show or series.
### Podcast
- [INMediaItemType.podcastEpisode](./inmediaitemtype/podcastepisode.md)
  A media type that indicates a podcast episode.
- [INMediaItemType.podcastPlaylist](./inmediaitemtype/podcastplaylist.md)
  A media type that indicates a playlist of podcast episodes.
- [INMediaItemType.podcastShow](./inmediaitemtype/podcastshow.md)
  A media type that indicates a podcast show.
- [INMediaItemType.podcastStation](./inmediaitemtype/podcaststation.md)
  A media type that indicates a podcast station.
### Audio Book
- [INMediaItemType.audioBook](./inmediaitemtype/audiobook.md)
  A media type that indicates an audio book.
### News
- [INMediaItemType.news](./inmediaitemtype/news.md)
  A media type that indicates news.
### General
- [INMediaItemType.unknown](./inmediaitemtype/unknown.md)
  A media type that indicates an unknown type.
- [INMediaItemType.genre](./inmediaitemtype/genre.md)
  A media type that indicates a genre.
### Initializers
- [init?(rawValue: Int)](./inmediaitemtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Describing the Media Item
- [var artwork: INImage?](./inmediaitem/artwork.md)
  Artwork for the media item.
- [var identifier: String?](./inmediaitem/identifier.md)
  The value your app uses to identify the media item.
- [var title: String?](./inmediaitem/title.md)
  The media item title.
- [var artist: String?](./inmediaitem/artist.md)
  The artist associated with the media item.
- [var type: INMediaItemType](./inmediaitem/type.md)
  The media item type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitemtype)*