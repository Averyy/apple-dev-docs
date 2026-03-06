# Curators.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary

The relationships for a curator resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Curators.Relationships
```

## Topics

### Related Objects
- [object Curators.Relationships.CuratorsPlaylistsRelationship](curators/relationships-data.dictionary/curatorsplaylistsrelationship.md)
  A relationship from the curator to its playlists.

## Properties

- `playlists` (Curators.Relationships.CuratorsPlaylistsRelationship): The playlists associated with the curator. By default, `playlists` includes identifiers only. Fetch limits: 10 default, 10 maximum.

## See Also

- [object Curators.Attributes](curators/attributes-data.dictionary.md)
  The attributes for a curator resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/curators/relationships-data.dictionary)*