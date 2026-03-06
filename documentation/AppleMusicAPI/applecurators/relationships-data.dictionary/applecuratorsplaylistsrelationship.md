# AppleCurators.Relationships.AppleCuratorsPlaylistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the Apple curator to its playlists.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object AppleCurators.Relationships.AppleCuratorsPlaylistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Playlists]) *(required)*: The playlists for the curator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/applecurators/relationships-data.dictionary/applecuratorsplaylistsrelationship)*