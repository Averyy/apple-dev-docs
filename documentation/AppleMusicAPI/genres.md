# Genres

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a music genre.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Genres
```

## Topics

### Related Objects
- [object Genres.Attributes](genres/attributes-data.dictionary.md)
  The attributes for a genre resource.

## Properties

- `id` (string) *(required)*: The identifier for the genre.
- `type` (string) *(required)*: This value must always be `genres`.
- `href` (string) *(required)*: The relative location for the genre resource.
- `attributes` (Genres.Attributes): The attributes for the genre.

## See Also

- [object GenresResponse](genresresponse.md)
  The response to a genres request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/genres)*