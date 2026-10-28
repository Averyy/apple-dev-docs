# Song.Prices

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to pricing information.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Song.Prices
```

## Data example

The feed export is in Parquet format. This data example is in JSON format for illustrative purposes.

```
{
"prices": {
    "fr": [
        {
            "currencyCode": "EUR",
            "price": "1.29",
            "priceType": "buy"
            "quality": "standard-definition"
        },
        {
            "currencyCode": "EUR",
            "price": "2.29",
            "priceType": "buy"
            "quality": "high-definition"
        }
    ]
}
}
```

## Topics

### Related objects
- [object Song.Prices.Price](./prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([Song.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string)

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

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/prices-data.dictionary)*