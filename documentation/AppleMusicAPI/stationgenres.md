# StationGenres

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a station genre.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object StationGenres
```

## Topics

### Related Objects
- [object StationGenres.Attributes](stationgenres/attributes-data.dictionary.md)
  The attributes for the station genre resource.
- [object StationGenres.Relationships](stationgenres/relationships-data.dictionary.md)
  The relationships for a station genre resource.

## Properties

- `id` (string) *(required)*: The identifier for the station genre.
- `type` (string) *(required)*: This value must always be `station-genres`.
- `href` (string) *(required)*: The relative location for the station genre resource.
- `attributes` (StationGenres.Attributes): The attributes for the station genre.
- `relationships` (StationGenres.Relationships): The relationships for the station genre.

## See Also

- [object Stations](stations.md)
  A resource object that represents a station.
- [object StationsResponse](stationsresponse.md)
  The response to a stations request.
- [object StationGenresResponse](stationgenresresponse.md)
  The response to a specific station genres resource request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/stationgenres)*