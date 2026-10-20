# Read the organization

**Framework**: Roster API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Returns information about the Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Mentions

- [Integrating with Roster API and Sign in with Apple](./integrating-with-roster-api-and-sign-in-with-apple.md)

#### Discussion

Access to the `organization` resource requires authorization to either the `edu.users.read` or `edu.classes.read` scope.

##### Example

**Request**:

```
curl "https://api-school.apple.com/rosterapi/v1/organization" -H "Authorization: Bearer ${TOKEN}"
```

**Response**:

```json
{
  "id":"1234",
  "type":"EDUCATION",
  "name":"Example Organization",
  "domains":[{"name":"example.com","isVerified":false}],
  "dateCreated":"2022-10-11T01:53:02Z",
  "dateLastModified":"2022-10-11T01:53:02Z"
}
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/organization`

## Responses

- `200` OK (`Organization`, `application/json`): The request was successful.
- `401` Unauthorized: The access token was invalid.
- `403` Forbidden: You don’t have permission to access the organization information.
- `404` Not Found: The server didn’t find the organization information.
- `429`: The client made too many requests. The response includes an `X-Retry-After` header that indicates the number of seconds to wait before making another request.
- `500` Internal Server Error: The server encountered an internal error.

## See Also

### Information about the organization
- [object Organization](./organization.md)
  Information about an Apple School Manager organization.
- [object Domain](./domain.md)
  A DNS domain name associated with an Apple School Manager organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-organization-infrmation)*