# Artists.Attributes

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The attributes for an artist resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Artists.Attributes
```

## Properties

- `artwork` (Artwork): The artwork for the artist image.
- `editorialNotes` (EditorialNotes): The notes about the artist that appear in the Apple Music catalog.
- `genreNames` ([string]) *(required)*: The names of the genres associated with this artist.
- `inFavorites` (boolean): Whether the catalog resource ID is in the person’s favorites.
- `name` (string) *(required)*: The localized name of the artist.
- `url` (string) *(required)*: The URL for sharing the artist in Apple Music.

## See Also

### Related Objects
- [object Artists.Relationships](./relationships-data.dictionary.md)
  The relationships for an artist resource.
- [object Artists.Views](./views-data.dictionary.md)
  The views for associations between artists and other resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists/attributes-data.dictionary)*