# Artist.Name

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to localized names for the artist.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Artist.Name
```

## Properties

- `locale` (string): A locale in the IETF language tag format. An empty value indicates fallback to `default`.
- `name` (string): A localized uncensored name for the artist.

## See Also

### Related objects
- [object Artist.NamePronunciation](./namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Artist.RelevanceScore](./relevancescore-data.dictionary.md)
  A score representing artist relevance, used to rank artists when surfacing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/artist/name-data.dictionary)*