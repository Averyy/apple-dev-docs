# Artist.RelevanceScore

**Framework**: Apple Music Feed  
**Kind**: dictionary

A score representing artist relevance, used to rank artists when surfacing content.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Artist.RelevanceScore
```

#### Overview

A higher score indicates higher relevance. For example, an artist with a score of 90 is ranked as more relevant than an artist with a score of 50.

## Topics

### Related objects
- [object Artist.RelevanceScore.StorefrontOverrides](artist/relevancescore-data.dictionary/storefrontoverrides-data.dictionary.md)
  A mapping of storefront country code to relevance score.

## Properties

- `defaultScore` (integer): The default relevance score.
- `storefrontOverrides` (Artist.RelevanceScore.StorefrontOverrides): A mapping of storefront country codes to relevance scores.

## See Also

- [object Artist.Name](artist/name-data.dictionary.md)
  A mapping of locale to localized names for the artist.
- [object Artist.NamePronunciation](artist/namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/artist/relevancescore-data.dictionary)*