# Get User IDs for an Organizational Unit

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of user IDs for an organizational unit in an organization.

**Availability**:
- Apple Business API 2.6+

##### Example

**Request**:

```
curl "https://api-business.apple.com/v1/organizationalUnits/{id}/relationships/users" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
  {
    "data": [
      {
        "type": "users",
        "id": "1234567890"
      },
      {
        "type": "users",
        "id": "0987654321"
      }
    ],
    "links": {
      "self": "https://api-business.apple.com/v1/organizationalUnits/OU789012/relationships/users",
      "next": "https://api-business.apple.com/v1/organizationalUnits/OU789012/relationships/users?cursor=MDowOjE3NDYxMTg0NjkzOTc6MTc0NjExODQ2OTM5Nzp0cnVlOmZhbHNlOjE3NDYxMTg0NjkzOTc"
    },
    "meta": {
      "paging": {
        "nextCursor": "MDowOjE3NDYxMTg0NjkzOTc6MTc0NjExODQ2OTM5Nzp0cnVlOmZhbHNlOjE3NDYxMTg0NjkzOTc",
        "limit": 100
      }
    }
  }
```

## Topics

### Responses
- [object OrganizationalUnitUsersLinkagesResponse](./organizationalunituserslinkagesresponse.md)
  A response that contains a list of user IDs for an organizational unit.

## Endpoint

`GET https://api-business.apple.com/v1/organizationalUnits/{id}/relationships/users`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`

## Responses

- `200` OK (`OrganizationalUnitUsersLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Organizational Units
- [Get Organizational Units](./get-organizational-units.md)
  Get a list of organizational units in an organization.
- [Get Organizational Unit Information](./get-organizationalunit-information.md)
  Get information about a specific organizational unit in an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-all-user-ids-for-an-organizationalunit)*