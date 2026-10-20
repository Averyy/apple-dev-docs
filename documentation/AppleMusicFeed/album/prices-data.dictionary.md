# Album.Prices

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to pricing information.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Album.Prices
```

#### Data example

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
- [object Album.Prices.Price](./prices-data.dictionary/price.md)
  Information about a pricing offer.

## Properties

- `prices` ([Album.Prices.Price]): A list of localized pricing information for the content.
- `storefront` (string)

## See Also

### Related objects
- [object Album.ArtistRole](./artistrole.md)
  Information about an artist’s role.
- [object Album.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized album cover art.
- [object Album.Genre](./genre.md)
  A genre name and its structure.
- [object Album.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the album.
- [object Album.NamePronunciation](./namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Album.RecordLabel](./recordlabel.md)
  Information about a record label.
- [object Album.RelatedArtist](./relatedartist.md)
  Information about a related artist.
- [object Album.RelatedSong](./relatedsong.md)
  Information about a related song.
- [object Album.ReleaseDate](./releasedate-data.dictionary.md)
  A mapping of locale to release date for the album.
- [object Album.TitleVersion](./titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Album.TitleVersionPronunciation](./titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/prices-data.dictionary)*