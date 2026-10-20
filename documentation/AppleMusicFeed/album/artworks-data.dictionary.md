# Album.Artworks

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to localized album cover art.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Album.Artworks
```

## Topics

### Related objects
- [object Album.Artworks.Artwork](./artworks-data.dictionary/artwork-data.dictionary.md)
  Information about a piece of artwork.

## Properties

- `artwork` (Album.Artworks.Artwork): The cover art for the album.
- `locale` (string): A locale in the IETF language tag format. An empty value indicates default artwork without an associated locale.

## See Also

### Related objects
- [object Album.ArtistRole](./artistrole.md)
  Information about an artist’s role.
- [object Album.Genre](./genre.md)
  A genre name and its structure.
- [object Album.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the album.
- [object Album.NamePronunciation](./namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Album.Prices](./prices-data.dictionary.md)
  A mapping of locale to pricing information.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/artworks-data.dictionary)*