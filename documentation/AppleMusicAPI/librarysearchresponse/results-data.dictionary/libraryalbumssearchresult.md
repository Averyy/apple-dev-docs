# LibrarySearchResponse.Results.LibraryAlbumsSearchResult

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The library albums results for a term search for specific resource types.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object LibrarySearchResponse.Results.LibraryAlbumsSearchResult
```

## Properties

- `data` ([LibraryAlbums]) *(required)*: The library album resources matching the search term, ordered by best match.
- `href` (string): A relative location for the resource.
- `next` (string): A relative cursor to fetch the next paginated collection of resources if more exist.

## See Also

### Related Objects
- [object LibrarySearchResponse.Results.LibraryArtistsSearchResult](./libraryartistssearchresult.md)
  The library artists results for a term search for specific resource types.
- [object LibrarySearchResponse.Results.LibraryMusicVideosSearchResult](./librarymusicvideossearchresult.md)
  The library music videos results for a term search for specific resource types.
- [object LibrarySearchResponse.Results.LibraryPlaylistsSearchResult](./libraryplaylistssearchresult.md)
  The library playlists results for a term search for specific resource types.
- [object LibrarySearchResponse.Results.LibrarySongsSearchResult](./librarysongssearchresult.md)
  The library songs results for a term search for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/librarysearchresponse/results-data.dictionary/libraryalbumssearchresult)*