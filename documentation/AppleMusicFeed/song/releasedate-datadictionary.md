# Song.ReleaseDate

**Framework**: Apple Music Feed  
**Kind**: dictionary

A mapping of locale to release date for the song.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Song.ReleaseDate
```

## Properties

- `locale` (string): A locale in the IETF language tag format. An empty value indicates fallback to `default`.
- `releaseDate` (string): The date of content release in YYYY-MM-DD format. For Apple Music, the locale is always `default`, so the release date is the same regardless of the time zone.

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
  Information about a related album.
- [object Song.RelatedArtist](song/relatedartist.md)
  Information about a related artist.
- [object Song.TitleVersion](song/titleversion-data.dictionary.md)
  A mapping of locale to translations for the specific title-version translation type.
- [object Song.TitleVersionPronunciation](song/titleversionpronunciation-data.dictionary.md)
  A mapping of locale to translations for the specific title-version-pronunciation-name translation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/song/releasedate-data.dictionary)*