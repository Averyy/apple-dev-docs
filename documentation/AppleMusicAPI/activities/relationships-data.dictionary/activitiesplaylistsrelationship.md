# Activities.Relationships.ActivitiesPlaylistsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship between the activity and its playlists.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Activities.Relationships.ActivitiesPlaylistsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Playlists]) *(required)*: The playlists associated with this activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/activities/relationships-data.dictionary/activitiesplaylistsrelationship)*