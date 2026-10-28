# Read a location

**Framework**: Roster API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Returns a specific location in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Discussion

Access to the `locations` resource requires authorization to either the `edu.users.read` or `edu.classes.read` scope.

### Example

**Request**:

```
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

### Path Parameters

- `locationId` (string) *(required)*: The identifier from the class. Use the `id` field from the [`Location`](./location.md) object.

## Responses

- `200` OK (`Location`, `application/json`): The request was successful.
- `401` Unauthorized: The access token was invalid.
- `403` Forbidden: You don’t have permission to access the requested location.
- `404` Not Found: The server didn’t find a location with the given `locationId` in the organization.
- `429`: The client made too many requests. The response includes an `X-Retry-After` header that indicates the number of seconds to wait before making another request.
- `500` Internal Server Error: The server encountered an internal error.

## See Also

### Information about locations
- [object Location](./location.md)
  A location in an Apple School Manager organization.
- [List locations](./returns-a-list-of-locations-for-an-apple-school-manager-organization.md)
  Returns a list of locations in an Apple School Manager organization.
- [object Locations](./locations.md)
  A list of locations, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-specific-location-in-an-apple-school-manager-organization)*