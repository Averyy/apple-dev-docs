# Curators.Relationships.CuratorsPlaylistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the curator to its playlists.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Curators.Relationships.CuratorsPlaylistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Playlists]) *(required)*: The playlists for the curator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/curators/relationships-data.dictionary/curatorsplaylistsrelationship)*