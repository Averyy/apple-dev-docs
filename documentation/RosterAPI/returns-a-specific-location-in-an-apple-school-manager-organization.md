# Read a location

**Framework**: Roster API  
**Kind**: httpRequest

Returns a specific location in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

#### Discussion

Access to the `locations` resource requires authorization to either the `edu.users.read` or `edu.classes.read` scope.

##### Example

**Request**:

```None
curl "https://api-school.apple.com/rosterapi/v1/locations/1234" \
        -H "Authorization: Bearer ${TOKEN}"

```

**Response**:

```json
{
  "id":"1234",
  "name":"Example Location",
  "domain":"example.com",
  "timeZone":"PST",
  "dateCreated":"2020-07-06T20:32:00Z",
  "dateLastModified":"2023-04-20T09:44:49.566949810Z"
}
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/locations/{locationId}`

## Parameters

- `locationId` (string) *(required)*: The identifier from the class. Use the `id` field from the [`Location`](location.md) object.

## See Also

- [object Location](location.md)
  A location in an Apple School Manager organization.
- [List locations](returns-a-list-of-locations-for-an-apple-school-manager-organization.md)
  Returns a list of locations in an Apple School Manager organization.
- [object Locations](locations.md)
  A list of locations, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-specific-location-in-an-apple-school-manager-organization)*