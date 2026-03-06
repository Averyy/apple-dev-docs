# StationGenres.Relationships.StationGenresStationsRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship from the station genre to associated stations.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object StationGenres.Relationships.StationGenresStationsRelationship
```

## Properties

- `href` (string): A relative location for the relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([Stations]) *(required)*: Stations associated with the station genre.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/stationgenres/relationships-data.dictionary/stationgenresstationsrelationship)*