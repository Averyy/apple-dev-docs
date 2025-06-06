# Song.Prices

**Framework**: Apple Music Feed  
**Kind**: dictionary

A mapping of locale to pricing information.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Song.Prices
```

#### Data Example

The feed export is in Parquet format. This data example is in JSON format for illustrative purposes.

```None
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
- [object Song.Prices.Price](song/prices-data.dictionary/price.md)
  Information about a pricing offer.

## See Also

- [object Song.ArtistRole](song/artistrole.md)
  Information about an artist’s role.
- [object Song.Genre](song/genre.md)
  A genre name and its structure.
- [object Song.Name](song/name-data.dictionary.md)
  A mapping of locale to localized names for the song.
- [object Song.NamePronunciation](song/namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Song.RelatedAlbum](song/relatedalbum.md)
  Information about a related album.
- [object Song.RelatedArtist](song/relatedartist.md)
  Information about a related artist.
- [object Song.ReleaseDate](song/releasedate-data.dictionary.md)
  A mapping of locale to release date for the song.
- [object Song.TitleVersion](song/titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Song.TitleVersionPronunciation](song/titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/prices-data.dictionary)*