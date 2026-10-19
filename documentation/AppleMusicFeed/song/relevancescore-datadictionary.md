# Song.RelevanceScore

**Framework**: Apple Music Feed  
**Kind**: dictionary

A score representing song relevance, used to rank songs when surfacing content.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Song.RelevanceScore
```

#### Overview

A higher score indicates higher relevance. For example, a song with a score of 90 is ranked as more relevant than a song with a score of 50.

## Topics

### Related objects
- [object Song.RelevanceScore.StorefrontOverrides](song/relevancescore-data.dictionary/storefrontoverrides-data.dictionary.md)
  A mapping of storefront country code to relevance score.

## Properties

- `defaultScore` (integer): The default relevance score.
- `storefrontOverrides` (Song.RelevanceScore.StorefrontOverrides): A mapping of storefront country codes to relevance scores.

## See Also

- [object Song.ArtistRole](song/artistrole.md)
  Information about an artist’s role.
- [object Song.Genre](song/genre.md)
  A genre name and its structure.
- [object Song.Name](song/name-data.dictionary.md)
  A mapping of locale to localized names for the song.
- [object Song.NamePronunciation](song/namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Song.Prices](song/prices-data.dictionary.md)
  A mapping of locale to pricing information.
- [object Song.RelatedAlbum](song/relatedalbum.md)
- [object Song.RelatedArtist](song/relatedartist.md)
  Information about a related artist.
- [object Song.ReleaseDate](song/releasedate-data.dictionary.md)
  A mapping of locale to release date for the song.
- [object Song.TitleVersion](song/titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Song.TitleVersionPronunciation](song/titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/relevancescore-data.dictionary)*