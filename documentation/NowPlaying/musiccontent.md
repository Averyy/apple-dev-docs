# MusicContent

**Framework**: Now Playing  
**Kind**: struct

Content representing a music track or song.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct MusicContent
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use this type for music playback, including songs, albums, and playlists.

The following example shows how to create music content with additional metadata:

```swift
var content: some MediaContentRepresentable {
    var content = MusicContent(
        id: track.id,
        songTitle: track.title,
        artistName: track.artist,
        albumName: track.album,
        type: .audio,
        duration: .finite(track.duration),
        artwork: Artwork(id: track.artworkID) { size in
            let data = await loadArtworkData(size: size)
            return try ArtworkRepresentation(data: data)
        }
    )
    content.composer = track.composer
    content.genre = track.genre
    content.isExplicit = track.isExplicit
    return content
}
```

## Topics

### Initializers
- [init(id: String, songTitle: String, artistName: String, albumName: String, type: MediaType, duration: MediaDuration?, artwork: Artwork?)](musiccontent/init(id:songtitle:artistname:albumname:type:duration:artwork:).md)
  Creates music content with the specified metadata.
- [init(id: String, songTitle: String, artistName: String, albumName: String, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)](musiccontent/init(id:songtitle:artistname:albumname:type:duration:artwork:animatedartwork:).md)
  Creates music content with static and animated artwork.
### Instance Properties
- [let albumName: String](musiccontent/albumname.md)
  The name of the album.
- [let animatedArtwork: AnimatedArtwork?](musiccontent/animatedartwork.md)
  Animated artwork for this content.
- [let artistName: String](musiccontent/artistname.md)
  The name of the artist or performer.
- [let artwork: Artwork?](musiccontent/artwork.md)
  Artwork for this content.
- [var composer: String?](musiccontent/composer.md)
  The name of the composer, if applicable.
- [let duration: MediaDuration?](musiccontent/duration.md)
  The duration of this content.
- [var isrc: String?](musiccontent/isrc.md)
  The International Standard Recording Code (ISRC) for this content.
- [let songTitle: String](musiccontent/songtitle.md)
  The title of the song.
- [let type: MediaType](musiccontent/type.md)
  The media type (audio or video).

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [MediaContentRepresentable](mediacontentrepresentable.md)

## See Also

- [protocol MediaContentRepresentable](mediacontentrepresentable.md)
  A protocol that describes media content being played.
- [struct PodcastContent](podcastcontent.md)
  Content representing a podcast episode.
- [struct MovieContent](moviecontent.md)
  Content representing a movie.
- [struct TVShowContent](tvshowcontent.md)
  Content representing a TV show episode.
- [struct BookContent](bookcontent.md)
  Content representing an audiobook or book being read aloud.
- [struct RadioContent](radiocontent.md)
  Content representing a radio station or live audio stream.
- [struct HomeMediaContent](homemediacontent.md)
  Content representing home media or ambient content.
- [struct GenericContent](genericcontent.md)
  Content representing generic or unspecified media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/musiccontent)*