# Song.NamePronunciation

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to translations for the specific pronunciation-name translation type.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Song.NamePronunciation
```

## Properties

- `locale` (string): A locale in the IETF language tag format. An empty value indicates fallback to `default`.
- `name` (string): A localized pronunciation of the song name.

## See Also

### Related objects
- [object Song.ArtistRole](./artistrole.md)
  Information about an artist’s role.
- [object Song.Genre](./genre.md)
  A genre name and its structure.
- [object Song.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the song.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/namepronunciation-data.dictionary)*