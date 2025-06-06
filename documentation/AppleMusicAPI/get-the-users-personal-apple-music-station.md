# Get the User's Personal Apple Music Station

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the current user’s personal Apple Music station.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

## See Also

- [object Stations](stations.md)
  A resource object that represents a station.
- [object StationsResponse](stationsresponse.md)
  The response to a stations request.
- [Get a Catalog Station](get-a-catalog-station.md)
  Fetch a station by using its identifier.
- [Get a Catalog Station's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-38wmf.md)
  Fetch a station’s relationship using its identifier.
- [Get Multiple Catalog Stations](get-multiple-catalog-stations.md)
  Fetch one or more stations by using their identifiers.
- [Get the Apple Music Live Radio Stations](get-the-apple-music-live-radio-stations.md)
  Fetch the Apple Music live radio stations for the storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-user's-personal-apple-music-station)*