# Search for places using mulitple identifiers

**Framework**: Apple Maps Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Obtain a set of Place objects for a given set of Place IDs.

**Availability**:
- Apple Maps Server API 1.2+

## Endpoint

`GET https://maps-api.apple.com/v1/place`

## Parameters

### Query Parameters

- `ids` (string) *(required)*: A comma separated list of Place IDs.
- `lang` (Lang): The language code for the response.

  **Default**: `en-US`

## Responses

- `200` OK (`PlacesResponse`, `application/json`): A list of [`PlacesResponse`](./placesresponse.md) results.
- `400` Bad Request (`ErrorResponse`, `application/json`): An [`ErrorResponse`](./errorresponse.md) object that contains an error message and an array of strings that contain additional details about the error.
- `401` Unauthorized (`ErrorResponse`, `application/json`): An [`ErrorResponse`](./errorresponse.md) object that contains an error message that indicates the Maps access token is missing or invalid, and an array of strings that contains additional details about the error.
- `500` Internal Server Error (`ErrorResponse`, `application/json`): An [`ErrorResponse`](./errorresponse.md) object that contains a server error message and an array of strings that describe additional details about the error.

## See Also

### Searching
- [type AddressCategory](./addresscategory.md)
  Search categories related to political geographical boundaries.
- [type SearchACResultType](./searchacresulttype.md)
  An enumerated string that indicates the result type for the search request.
- [type SearchResultType](./searchresulttype.md)
  An enumerated string that indicates the result type for the search autocomplete request.
- [object AlternateIdsResponse](./alternateidsresponse.md)
  A list of alternate Place IDs and associated errors.
- [object AlternateIdsResponse.AlternateIds](./alternateidsresponse/alternateids.md)
  Contains a list of alternate Place IDs for a given Place ID.
- [object PlacesResponse](./placesresponse.md)
  A list of Place IDs and errors.
- [object PlacesResponse.PlaceLookupError](./placesresponse/placelookuperror.md)
  An error associated with a lookup call.
- [Search for places that match specific criteria](./v1-search.md)
  Find places by name or by specific search criteria.
- [Search for places that meet specific criteria to autocomplete a place search](./v1-searchautocomplete.md)
  Find results that you can use to autocomplete searches.
- [Search for a place using an identifier](./v1-place-_id.md)
  Obtain a Place object for a given Place ID.
- [Obtain a list of alternate place identifiers](./v1-place-alternateids.md)
  Get a list of alternate Place IDs given one or more Place IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-place)*