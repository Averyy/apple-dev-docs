# Activities.Relationships

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The relationships for an activity resource.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Activities.Relationships
```

## Topics

### Related Objects
- [object Activities.Relationships.ActivitiesPlaylistsRelationship](./relationships-data.dictionary/activitiesplaylistsrelationship.md)
  A relationship between the activity and its playlists.

## Properties

- `playlists` (Activities.Relationships.ActivitiesPlaylistsRelationship): The playlists associated with this activity. By default, `playlists` includes identifiers only.

  Fetch limits: 10 default, 10 maximum.

## See Also

### Related Objects
- [object Activities.Attributes](./attributes-data.dictionary.md)
  The attributes for an activities resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/activities/relationships-data.dictionary)*