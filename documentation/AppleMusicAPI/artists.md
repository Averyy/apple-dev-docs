# Artists

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents the artist of an album where an artist can be one or more people.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Artists
```

## Mentions

- [Handling Resource Representation and Relationships](handling-resource-representation-and-relationships.md)

## Topics

### Related Objects
- [object Artists.Attributes](artists/attributes-data.dictionary.md)
  The attributes for an artist resource.
- [object Artists.Relationships](artists/relationships-data.dictionary.md)
  The relationships for an artist resource.
- [object Artists.Views](artists/views-data.dictionary.md)
  The views for associations between artists and other resources.

## Properties

- `id` (string) *(required)*: The identifier for the artist.
- `type` (string) *(required)*: This value is always `artists`.
- `href` (string) *(required)*: The relative location for the artist resource.
- `attributes` (Artists.Attributes): The attributes for the artist.
- `relationships` (Artists.Relationships): The relationships for the artist.
- `views` (Artists.Views): The views for associations between artists and other resources.

## See Also

- [object ArtistsResponse](artistsresponse.md)
  The response to an artists request.
- [object LibraryArtists](libraryartists.md)
  A resource object that represents an artist present in a user’s library.
- [object LibraryArtistsResponse](libraryartistsresponse.md)
  The response to a library artists request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists)*