# LibraryPlaylists.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for a library playlist resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylists.Relationships
```

## Topics

### Related Objects
- [object LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship](libraryplaylists/relationships-data.dictionary/libraryplaylistscatalogrelationship.md)
  A relationship from the playlist to its associated catalog content.
- [object LibraryPlaylists.Relationships.LibraryPlaylistsTracksRelationship](libraryplaylists/relationships-data.dictionary/libraryplayliststracksrelationship.md)
  A relationship from the playlist to its tracks.

## Properties

- `catalog` (LibraryPlaylists.Relationships.LibraryPlaylistsCatalogRelationship): The corresponding playlist in the Apple Music catalog the playlist is associated with. Fetch limits: None (associated with at most one catalog playlist).
- `tracks` (LibraryPlaylists.Relationships.LibraryPlaylistsTracksRelationship): The library songs and library music videos included in the playlist. By default, `tracks` not included. Only available when fetching a single library playlist resource by ID. Fetch limits: 100 default, 100 maximum.

## See Also

- [object LibraryPlaylists.Attributes](libraryplaylists/attributes-data.dictionary.md)
  The attributes for a library playlist resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylists/relationships-data.dictionary)*