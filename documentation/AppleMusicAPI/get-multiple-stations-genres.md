# Get Multiple Stations Genres

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more station genres by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object StationGenres](stationgenres.md)
  A resource object that represents a station genre.
- [object StationGenresResponse](stationgenresresponse.md)
  The response to a specific station genres resource request.
- [Get a Station Genre](get-a-station-genre.md)
  Fetch a station genre by using its identifier.
- [Get a Station Genre’s Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-i4r0.md)
  Fetch a station genre’s relationship by using its identifier.
- [Get All Station Genres](get-all-station-genres.md)
  Fetch all station genres for a given storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-stations-genres)*