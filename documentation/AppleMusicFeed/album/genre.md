# Album.Genre

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A genre name and its structure.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Album.Genre
```

## Discussion

Genres are hierarchical beginning with the genre `Music`.

## Data example

The feed export is in Parquet format. This data example is in JSON format for illustrative purposes.

```
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

## Properties

- `name` (string): The name of the genre.
- `path` ([string]): A list of genres in hierarchical order. For example, if `Classical` is a subgenre of `Music`, this value is `[‘Music’, ‘Classical’]`.

## See Also

### Related objects
- [object Album.ArtistRole](./artistrole.md)
  Information about an artist’s role.
- [object Album.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized album cover art.
- [object Album.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the album.
- [object Album.NamePronunciation](./namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Album.Prices](./prices-data.dictionary.md)
  A mapping of locale to pricing information.
- [object Album.RecordLabel](./recordlabel.md)
  Information about a record label.
- [object Album.RelatedArtist](./relatedartist.md)
  Information about a related artist.
- [object Album.RelatedSong](./relatedsong.md)
  Information about a related song.
- [object Album.ReleaseDate](./releasedate-data.dictionary.md)
  A mapping of locale to release date for the album.
- [object Album.TitleVersion](./titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Album.TitleVersionPronunciation](./titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/genre)*