# Get Organizational Units

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of organizational units in an organization.

**Availability**:
- Apple Business API 2.6+

##### Example

**Request**:

```
curl "https://api-business.apple.com/v1/organizationalUnits" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
    "data": [
      {
        "type": "organizationalUnits",
        "id": "OU789012",
        "attributes": {
          "name": "Engineering",
          "description": "Engineering organizational unit",
          "createdDateTime": "2023-03-15T10:00:00Z",
          "updatedDateTime": "2024-06-01T14:30:00Z"
        },
        "relationships": {
          "users": {
            "links": {
              "self": "https://api-business.apple.com/v1/organizationalUnits/OU789012/relationships/users"
            }
          }
        },
        "links": {
          "self": "https://api-business.apple.com/v1/organizationalUnits/OU789012"
        }
      }
    ],
    "links": {
      "self": "https://api-business.apple.com/v1/organizationalUnits",
      "next": "https://api-business.apple.com/v1/organizationalUnits?cursor=MDowOjE3NDYxMTM4OTI1OTA6MTc0NjExMzg5MjU5MDp0cnVlOmZhbHNlOjE3NDYxMTM4OTI1OTA"
    },
    "meta": {
      "paging": {
        "nextCursor": "MDowOjE3NDYxMTM4OTI1OTA6MTc0NjExMzg5MjU5MDp0cnVlOmZhbHNlOjE3NDYxMTM4OTI1OTA",
        "limit": 100
      }
    }
  }
```

## Topics

### Responses
- [object OrganizationalUnitsResponse](./organizationalunitsresponse.md)
  A response that contains a list of organizational unit resources.

## Endpoint

`GET https://api-business.apple.com/v1/organizationalUnits`

## Parameters

### Query Parameters

- `fields[organizationalUnits]` ([string]): The fields to return for included related types.

  **Allowed Values**: `name`, `description`, `createdDateTime`, `updatedDateTime`, `users`
- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`

## Responses

- `200` OK (`OrganizationalUnitsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Organizational Units
- [Get Organizational Unit Information](./get-organizationalunit-information.md)
  Get information about a specific organizational unit in an organization.
- [Get User IDs for an Organizational Unit](./get-all-user-ids-for-an-organizationalunit.md)
  Get a list of user IDs for an organizational unit in an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-organizational-units)*