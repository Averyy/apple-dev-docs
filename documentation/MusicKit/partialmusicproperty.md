# PartialMusicProperty

**Framework**: MusicKit  
**Kind**: class

A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.

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
class PartialMusicProperty<Root>
```

## Topics

### Type Properties
- [static let albums: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/albums-2huns.md)
  An identifier for the relationship property that returns the associated albums for the artist.
- [static let albums: MusicRelationshipProperty<Song, Album>](partialmusicproperty/albums-5kqf6.md)
  An identifier for the relationship property that returns the associated albums for the song.
- [static let albums: MusicRelationshipProperty<MusicVideo, Album>](partialmusicproperty/albums-6v0rp.md)
  An identifier of the relationship property that returns the associated albums for the music video.
- [static let appearsOn: MusicRelationshipProperty<Album, Playlist>](partialmusicproperty/appearson.md)
  An identifier for the association property that returns a collection of playlists that include tracks from the album.
- [static let appearsOnAlbums: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/appearsonalbums.md)
  An identifier for the association property that returns a collection of albums from other artists that this artist appears on.
- [static var artistURL: MusicExtendedAttributeProperty<MusicVideo, URL>](partialmusicproperty/artisturl-7j56f.md)
  An identifier for the extended attribute property that returns the artist’s URL.
- [static var artistURL: MusicExtendedAttributeProperty<Song, URL>](partialmusicproperty/artisturl-81r7i.md)
  An identifier for the extended attribute property that returns the artist’s URL.
- [static var artistURL: MusicExtendedAttributeProperty<Album, URL>](partialmusicproperty/artisturl-msvj.md)
  An identifier for the extended attribute property that returns the artist’s URL.
- [static let artists: MusicRelationshipProperty<Album, Artist>](partialmusicproperty/artists-1bm4c.md)
  An identifier for the relationship property that returns the associated artists for the album.
- [static let artists: MusicRelationshipProperty<Song, Artist>](partialmusicproperty/artists-3x8cx.md)
  An identifier for the relationship property that returns the associated artists for the song.
- [static let artists: MusicRelationshipProperty<MusicVideo, Artist>](partialmusicproperty/artists-6myll.md)
  An identifier of the relationship property that returns the associated artists for the music video.
- [static let audioVariants: MusicExtendedAttributeProperty<Song, [AudioVariant]>](partialmusicproperty/audiovariants-60v28.md)
  An identifier for the extended attribute property that returns the audio variants for the song.
- [static let audioVariants: MusicExtendedAttributeProperty<Album, [AudioVariant]>](partialmusicproperty/audiovariants-8zkt2.md)
  An identifier for the extended attribute property that returns the audio variants for the album.
- [static let compilationAlbums: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/compilationalbums.md)
  An identifier for the association property that returns a collection of compilation albums that include tracks by the artist.
- [static let composers: MusicRelationshipProperty<Song, Artist>](partialmusicproperty/composers.md)
  An identifier for the relationship property that returns the song’s composers.
- [static let curator: MusicRelationshipProperty<Playlist, Curator>](partialmusicproperty/curator.md)
  An identifier for the extended attribute property that returns the playlist’s associated curator.
- [static let entries: MusicRelationshipProperty<Playlist, Playlist.Entry>](partialmusicproperty/entries.md)
  An identifier for the relationship property that returns the entries in the playlist.
- [static let featuredAlbums: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/featuredalbums.md)
  An identifier for the association property that returns a collection of featured albums for the artist.
- [static let featuredArtists: MusicRelationshipProperty<Playlist, Artist>](partialmusicproperty/featuredartists.md)
  An identifier for the association property that returns a collection of featured artists for this playlist.
- [static let featuredPlaylists: MusicRelationshipProperty<Artist, Playlist>](partialmusicproperty/featuredplaylists.md)
  An identifier for the association property that returns a collection of the artist’s playlists.
- [static let fullAlbums: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/fullalbums.md)
  An identifier for the association property that returns a collection of the artist’s full-release albums.
- [static let genres: MusicRelationshipProperty<MusicVideo, Genre>](partialmusicproperty/genres-2y2ss.md)
  An identifier of the relationship property that returns the associated genres for the music video.
- [static let genres: MusicRelationshipProperty<Artist, Genre>](partialmusicproperty/genres-3jsli.md)
  An identifier for the relationship property that returns the associated genres for the artist.
- [static let genres: MusicRelationshipProperty<Song, Genre>](partialmusicproperty/genres-5w9nm.md)
  An identifier for the relationship property that returns the associated genres for the song.
- [static let genres: MusicRelationshipProperty<Album, Genre>](partialmusicproperty/genres-7el74.md)
  An identifier for the relationship property that returns the genres for the album.
- [static let latestRelease: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/latestrelease.md)
  An identifier for the association property that returns the artist’s most recent album.
- [static var latestReleases: MusicRelationshipProperty<RecordLabel, Album>](partialmusicproperty/latestreleases.md)
  An identifier for the association property that returns a collection of the most recent releases for the record label.
- [static let liveAlbums: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/livealbums.md)
  An identifier for the association property that returns a collection of the artist’s live albums.
- [static let moreByArtist: MusicRelationshipProperty<MusicVideo, MusicVideo>](partialmusicproperty/morebyartist.md)
  An identifier of the association property that returns a collection of additional music videos by the artist.
- [static let moreByCurator: MusicRelationshipProperty<Playlist, Playlist>](partialmusicproperty/morebycurator.md)
  An identifier for the association property that returns a collection of additional playlists by the same curator.
- [static let moreInGenre: MusicRelationshipProperty<MusicVideo, MusicVideo>](partialmusicproperty/moreingenre.md)
  A identifier of the association property that returns a collection of music videos in the same genre as this music video.
- [static let musicVideos: MusicRelationshipProperty<Artist, MusicVideo>](partialmusicproperty/musicvideos-6hip3.md)
  An identifier for the relationship property that returns the associated music videos for the artist.
- [static let musicVideos: MusicRelationshipProperty<Song, MusicVideo>](partialmusicproperty/musicvideos-89mym.md)
  An identifier for the relationship property that returns the song’s associated music videos.
- [static let otherVersions: MusicRelationshipProperty<Album, Album>](partialmusicproperty/otherversions.md)
  An identifier for the association property that returns a collection of other versions of the album.
- [static let playlists: MusicRelationshipProperty<Artist, Playlist>](partialmusicproperty/playlists-1j0l9.md)
  An identifier for the relationship property that returns the associated playlists for the artist.
- [static let playlists: MusicRelationshipProperty<Curator, Playlist>](partialmusicproperty/playlists-9quj1.md)
  An identifier for the relationship property that returns the associated playlists for the curator.
- [static let playlists: MusicRelationshipProperty<RadioShow, Playlist>](partialmusicproperty/playlists-wgt7.md)
  An identifier for the relationship property that returns the associated playlists for the radio show.
- [static let radioShow: MusicRelationshipProperty<Playlist, RadioShow>](partialmusicproperty/radioshow.md)
  An identifier for the extended attribute property that returns the playlist’s associated radio show.
- [static let recordLabels: MusicRelationshipProperty<Album, RecordLabel>](partialmusicproperty/recordlabels.md)
  An identifier for the relationship property that returns the record labels for the album.
- [static let relatedAlbums: MusicRelationshipProperty<Album, Album>](partialmusicproperty/relatedalbums.md)
  An identifier for the association property that returns a collection of related albums.
- [static let relatedVideos: MusicRelationshipProperty<Album, MusicVideo>](partialmusicproperty/relatedvideos.md)
  An identifier for the association property that returns a collection of related music videos for the album.
- [static let similarArtists: MusicRelationshipProperty<Artist, Artist>](partialmusicproperty/similarartists.md)
  An identifier for the association property that returns a collection of artists similar to this artist.
- [static let singles: MusicRelationshipProperty<Artist, Album>](partialmusicproperty/singles.md)
  An identifier of the association property that returns a collection of the artist’s albums in the  category.
- [static let songs: MusicRelationshipProperty<MusicVideo, Song>](partialmusicproperty/songs.md)
  An identifier of the relationship property that returns the associated songs for the music video.
- [static let station: MusicRelationshipProperty<Song, Station>](partialmusicproperty/station-8u1rf.md)
  An identifier for the relationship property that returns the associated station for the song.
- [static let station: MusicRelationshipProperty<Artist, Station>](partialmusicproperty/station-8zftf.md)
  An identifier for the relationship property that returns the associated station for the artist.
- [static let topMusicVideos: MusicRelationshipProperty<Artist, MusicVideo>](partialmusicproperty/topmusicvideos.md)
  An identifier for the association property that returns a collection of the artist’s top music videos.
- [static var topReleases: MusicRelationshipProperty<RecordLabel, Album>](partialmusicproperty/topreleases.md)
  An identifier for the association property that returns a collection of top releases for the record label.
- [static let topSongs: MusicRelationshipProperty<Artist, Song>](partialmusicproperty/topsongs.md)
  An identifier for the association property that returns a collection of the artist’s top songs.
- [static let tracks: MusicRelationshipProperty<Playlist, Track>](partialmusicproperty/tracks-8mq2j.md)
  An identifier for the relationship property that returns the tracks in the playlist.
- [static let tracks: MusicRelationshipProperty<Album, Track>](partialmusicproperty/tracks-9mk2l.md)
  An identifier for the relationship property that returns the tracks on the album.

## Relationships

### Inherits From
- [AnyMusicProperty](anymusicproperty.md)
### Inherited By
- [MusicAttributeProperty](musicattributeproperty.md)
- [PartialMusicAsyncProperty](partialmusicasyncproperty.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MusicItem](musicitem.md)
  A protocol with basic requirements for music items.
- [struct MusicItemID](musicitemid.md)
  An object that represents a unique identifier for a music item.
- [struct MusicItemCollection](musicitemcollection.md)
  A collection of music items.
- [protocol MusicPropertyContainer](musicpropertycontainer.md)
  A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- [class MusicRelationshipProperty](musicrelationshipproperty.md)
  An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- [class MusicExtendedAttributeProperty](musicextendedattributeproperty.md)
  An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- [class MusicAttributeProperty](musicattributeproperty.md)
  An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- [class PartialMusicAsyncProperty](partialmusicasyncproperty.md)
  A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- [class AnyMusicProperty](anymusicproperty.md)
  A type-erased identifier for a music item property, from any root type to any resulting value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/partialmusicproperty)*