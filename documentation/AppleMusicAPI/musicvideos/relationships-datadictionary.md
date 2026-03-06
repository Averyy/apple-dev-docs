# MusicVideos.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for a music video resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicVideos.Relationships
```

## Topics

### Related Objects
- [object MusicVideos.Relationships.MusicVideosAlbumsRelationship](musicvideos/relationships-data.dictionary/musicvideosalbumsrelationship.md)
  A relationship from the music video to its albums.
- [object MusicVideos.Relationships.MusicVideosArtistsRelationship](musicvideos/relationships-data.dictionary/musicvideosartistsrelationship.md)
  A relationship from the music video to its artists.
- [object MusicVideos.Relationships.MusicVideosGenresRelationship](musicvideos/relationships-data.dictionary/musicvideosgenresrelationship.md)
  A relationship from the music video to its genres.
- [object MusicVideos.Relationships.MusicVideosLibraryRelationship](musicvideos/relationships-data.dictionary/musicvideoslibraryrelationship.md)
  A relationship from the music video to its library.
- [object MusicVideos.Relationships.MusicVideosSongsRelationship](musicvideos/relationships-data.dictionary/musicvideossongsrelationship.md)
  A relationship from the music video to its songs.

## Properties

- `albums` (MusicVideos.Relationships.MusicVideosAlbumsRelationship): The albums associated with the music video. By default, `albums` includes identifiers only. Fetch limits: 10 default, 10 maximum.
- `artists` (MusicVideos.Relationships.MusicVideosArtistsRelationship): The artists associated with the music video. By default, `artists` includes identifiers only. Fetch limits: 10 default, 10 maximum.
- `genres` (MusicVideos.Relationships.MusicVideosGenresRelationship): The genres associated with the music video. By default, `genres` not included. Fetch limits: None.
- `library` (MusicVideos.Relationships.MusicVideosLibraryRelationship): The library of a music video if added to library. Fetch limits: None.
- `songs` (MusicVideos.Relationships.MusicVideosSongsRelationship): The songs associated with the music video. Fetch limits: 10 default, 10 maximum.

## See Also

- [object MusicVideos.Attributes](musicvideos/attributes-data.dictionary.md)
  The attributes for a music video resource.
- [object MusicVideos.Views](musicvideos/views-data.dictionary.md)
  The views for a music video resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicvideos/relationships-data.dictionary)*