# Read the organization

**Framework**: Roster API  
**Kind**: httpRequest

Returns information about the Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Mentions

- [Integrating with Roster API and Sign in with Apple](integrating-with-roster-api-and-sign-in-with-apple.md)

#### Discussion

Access to the `organization` resource requires authorization to either the `edu.users.read` or `edu.classes.read` scope.

##### Example

**Request**:

```None
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

## See Also

- [object Organization](organization.md)
  Information about an Apple School Manager organization.
- [object Domain](domain.md)
  A DNS domain name associated with an Apple School Manager organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-organization-infrmation)*