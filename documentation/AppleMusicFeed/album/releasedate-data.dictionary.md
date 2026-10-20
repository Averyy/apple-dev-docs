# Album.ReleaseDate

**Framework**: Apple Music Feed  
**Kind**: dictionary

A mapping of locale to release date for the album.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Album.ReleaseDate
```

## Properties

- `locale` (string): A locale in the IETF language tag format. An empty value indicates fallback to `default`.
- `releaseDate` (string): The date of content release in YYYY-MM-DD format. For Apple Music, the locale is always `default`, so the release date is the same regardless of the time zone.

## See Also

- [object Album.ArtistRole](album/artistrole.md)
  Information about an artist’s role.
- [object Album.Artworks](album/artworks-data.dictionary.md)
  A mapping of locale to localized album cover art.
- [object Album.Genre](album/genre.md)
  A genre name and its structure.
- [object Album.Name](album/name-data.dictionary.md)
  A mapping of locale to localized names for the album.
- [object Album.NamePronunciation](album/namepronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific pronunciation-name translation type.
- [object Album.Prices](album/prices-data.dictionary.md)
  A mapping of locale to pricing information.
- [object Album.RecordLabel](album/recordlabel.md)
  Information about a record label.
- [object Album.RelatedArtist](album/relatedartist.md)
  Information about a related artist.
- [object Album.RelatedSong](album/relatedsong.md)
  Information about a related song.
- [object Album.TitleVersion](album/titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Album.TitleVersionPronunciation](album/titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/releasedate-data.dictionary)*