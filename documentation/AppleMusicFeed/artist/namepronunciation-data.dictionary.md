# Artist.NamePronunciation

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to translations for the specific pronunciation-name translation type.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Artist.NamePronunciation
```

## Properties

- `locale` (string): A locale in the IETF language tag format. An empty value indicates fallback to `default`.
- `name` (string): A localized pronunciation of the artist name.

## See Also

### Related objects
- [object Artist.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the artist.
- [object Artist.RelevanceScore](./relevancescore-data.dictionary.md)
  A score representing artist relevance, used to rank artists when surfacing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/artist/namepronunciation-data.dictionary)*