# Song.Genre

**Framework**: Apple Music Feed  
**Kind**: dictionary

A genre name and its structure.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Song.Genre
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

- [object Song.ArtistRole](song/artistrole.md)
  Information about an artist’s role.
- [object Song.Name](song/name-data.dictionary.md)
  A mapping of locale to localized names for the song.
- [object Song.NamePronunciation](song/namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Song.Prices](song/prices-data.dictionary.md)
  A mapping of locale to pricing information.
- [object Song.RelatedAlbum](song/relatedalbum.md)
  Information about a related album.
- [object Song.RelatedArtist](song/relatedartist.md)
  Information about a related artist.
- [object Song.ReleaseDate](song/releasedate-data.dictionary.md)
  A mapping of locale to release date for the song.
- [object Song.TitleVersion](song/titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Song.TitleVersionPronunciation](song/titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/genre)*