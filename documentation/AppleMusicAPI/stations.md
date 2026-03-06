# Stations

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents a station.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Stations
```

## Topics

### Related Objects
- [object Stations.Attributes](stations/attributes-data.dictionary.md)
  The attributes for a station resource.
- [object Stations.Relationships](stations/relationships-data.dictionary.md)
  The name of the relationship you want to fetch for this resource.

## Properties

- `id` (string) *(required)*: The identifier for the station.
- `type` (string) *(required)*: This value must always be `stations`.
- `href` (string) *(required)*: The relative location for the station resource.
- `attributes` (Stations.Attributes): The attributes for the station.
- `relationships` (Stations.Relationships): The relationships for the station.

## See Also

- [object StationsResponse](stationsresponse.md)
  The response to a stations request.
- [object StationGenres](stationgenres.md)
  A resource object that represents a station genre.
- [object StationGenresResponse](stationgenresresponse.md)
  The response to a specific station genres resource request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/stations)*