# AppleCurators.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The relationships for an Apple curator resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object AppleCurators.Relationships
```

## Topics

### Related Objects
- [object AppleCurators.Relationships.AppleCuratorsPlaylistsRelationship](./relationships-data.dictionary/applecuratorsplaylistsrelationship.md)
  A relationship from the Apple curator to its playlists.

## Properties

- `playlists` (AppleCurators.Relationships.AppleCuratorsPlaylistsRelationship): The playlists associated with this curator. By default, `playlists` includes identifiers only.

  Fetch limits: 10 default, 10 maximum.

## See Also

### Related Objects
- [object AppleCurators.Attributes](./attributes-data.dictionary.md)
  The attributes for an Apple curator resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/applecurators/relationships-data.dictionary)*