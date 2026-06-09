# Content types and metadata

**Framework**: Now Playing

Describe the media your app is playing.

#### Overview

Use content types to tell the system what kind of media your app is playing. Each content type provides metadata fields appropriate for its media category, such as the song title and artist for music, or the show name and season for TV episodes.

Return a content type from your [`content`](mediasessionrepresentable/content.md) or [`content`](remotemediasessionrepresentable/content.md) property. The framework uses this information to populate the Lock Screen, Control Center, and connected accessories.

Each content type has a small set of initializer parameters for its core metadata, plus mutable properties for additional fields like `isExplicit`, `genre`, `collectionID`, and `serviceID`. Set those properties on the content value before returning it:

```swift
var content: (any MediaContentRepresentable)? {
    guard let track = currentTrack else { return nil }
    var content = MusicContent(
        id: track.id,
        songTitle: track.title,
        artistName: track.artist,
        albumName: track.album,
        type: .audio,
        duration: .finite(track.duration),
        artwork: Artwork(id: track.artworkID) { size in
            let (data, _) = try await URLSession.shared.data(from: track.artworkURL)
            return try ArtworkRepresentation(data: data)
        }
    )
    content.isExplicit = track.isExplicit
    content.genre = track.genre
    return content
}
```

## Topics

### Presenting content
- [protocol MediaContentRepresentable](mediacontentrepresentable.md)
  A protocol that describes media content being played.
- [struct MusicContent](musiccontent.md)
  Content representing a music track or song.
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
### Specifying type and duration
- [enum MediaType](mediatype.md)
  The type of media being played.
- [enum MediaDuration](mediaduration.md)
  The duration of media content.
### Displaying artwork
- [struct Artwork](artwork.md)
  Artwork for a media item that can be requested at a specified size.
- [struct ArtworkRepresentation](artworkrepresentation.md)
  An artwork image representation, such as music album cover art, associated with a media item.
- [struct AnimatedArtwork](animatedartwork.md)
  Animated artwork for the media item with video and preview support.

## See Also

- [struct MediaPlaybackSnapshot](mediaplaybacksnapshot.md)
  A snapshot of playback state and timing for a Now Playing session.
- [Playback commands](playback-commands.md)
  Declare the playback controls your app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/content-types-and-metadata)*