# Song.RelevanceScore

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A score representing song relevance, used to rank songs when surfacing content.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Song.RelevanceScore
```

## Overview

A higher score indicates higher relevance. For example, a song with a score of 90 is ranked as more relevant than a song with a score of 50.

## Topics

### Related objects
- [object Song.RelevanceScore.StorefrontOverrides](./relevancescore-data.dictionary/storefrontoverrides-data.dictionary.md)
  A mapping of storefront country code to relevance score.

## Properties

- `defaultScore` (integer): The default relevance score.
- `storefrontOverrides` (Song.RelevanceScore.StorefrontOverrides): A mapping of storefront country codes to relevance scores.

## See Also

### Related objects
- [object Song.ArtistRole](./artistrole.md)
  Information about an artist’s role.
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
- [object Song.TitleVersion](./titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Song.TitleVersionPronunciation](./titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/relevancescore-data.dictionary)*