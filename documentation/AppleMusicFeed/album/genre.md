# Album.Genre

**Framework**: Apple Music Feed  
**Kind**: dictionary

A genre name and its structure.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Album.Genre
```

#### Discussion

Genres are hierarchical beginning with the genre `Music`.

#### Data Example

The feed export is in Parquet format. This data example is in JSON format for illustrative purposes.

```None
{
    "genres": {
        "name": "Rock",
        "path": [
            "Music",
            "Classical",
            "Rock"
        ]
    }
}
```

## See Also

- [object Album.ArtistRole](album/artistrole.md)
  Information about an artist’s role.
- [object Album.Artworks](album/artworks-data.dictionary.md)
  A mapping of locale to localized album cover art.
- [object Album.Name](album/name-data.dictionary.md)
  A mapping of locale to localized names for the album.
- [object Album.NamePronunciation](album/namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Album.Prices](album/prices-data.dictionary.md)
  A mapping of locale to pricing information.
- [object Album.RecordLabel](album/recordlabel.md)
  Information about a record label.
- [object Album.RelatedArtist](album/relatedartist.md)
  Information about a related artist.
- [object Album.RelatedSong](album/relatedsong.md)
  Information about a related song.
- [object Album.ReleaseDate](album/releasedate-data.dictionary.md)
  A mapping of locale to release date for the album.
- [object Album.TitleVersion](album/titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Album.TitleVersionPronunciation](album/titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/genre)*