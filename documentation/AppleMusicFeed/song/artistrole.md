# Song.ArtistRole

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

Information about an artist’s role.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Song.ArtistRole
```

## Properties

- `artistId` (string): The identifier for the artist in Apple Music.
- `artistName` (string): The name of the artist.
- `roleName` (string): The artist’s role. Possible values include `compose-author`, `contributor`, `translator`, `performer`, `arranger`, `composer`, `adapter`, and `author`.

## See Also

### Related objects
- [object Song.Genre](./genre.md)
  A genre name and its structure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/artistrole)*