# List locations

**Framework**: Roster API  
**Kind**: httpRequest

Returns a list of locations in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

#### Discussion

Access to the `locations` resource requires authorization to either the `edu.users.read` or `edu.classes.read` scope.

##### Example

**Request**:

```None
curl "https://api-school.apple.com/rosterapi/v1/locations?limit=1" -H "Authorization: Bearer ${TOKEN}"
```

**Response**:

```json
{
  "locations":[{"id":"1234","name":"Example Location","domain":"example.com","timeZone":"PST","dateCreated":"2020-07-06T20:32:00Z","dateLastModified":"2023-04-20T09:49:33.938397143Z"}],
  "nextPageToken":"XbdJJGHGTqnueAVPfw2XOA",
  "moreToFollow":true
}
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/locations`

## Parameters

- `limit` (string): The maximum number of locations to return. The default is 100.
- `pageToken` (string): A token for paging through a large number of results. If the number of locations in the organization is greater than the `limit` parameter, pass the token returned in [`Locations`](locations.md).

## See Also

- [Read a location](returns-a-specific-location-in-an-apple-school-manager-organization.md)
  Returns a specific location in an Apple School Manager organization.
- [object Location](location.md)
  A location in an Apple School Manager organization.
- [object Locations](locations.md)
  A list of locations, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-locations-for-an-apple-school-manager-organization)*