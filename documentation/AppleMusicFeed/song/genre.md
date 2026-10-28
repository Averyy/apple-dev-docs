# Song.Genre

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A genre name and its structure.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Song.Genre
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
- [object Song.ArtistRole](./artistrole.md)
  Information about an artist’s role.
- [object Song.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the song.
- [object Song.NamePronunciation](./namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Song.Prices](./prices-data.dictionary.md)
  A mapping of locale to pricing information.
- [object Song.RelatedAlbum](./relatedalbum.md)
- [object Song.RelatedArtist](./relatedartist.md)
  Information about a related artist.
- [object Song.ReleaseDate](./releasedate-data.dictionary.md)
  A mapping of locale to release date for the song.
- [object Song.RelevanceScore](./relevancescore-data.dictionary.md)
  A score representing song relevance, used to rank songs when surfacing content.
- [object Song.TitleVersion](./titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Song.TitleVersionPronunciation](./titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/genre)*