# Get Organizational Unit Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific organizational unit in an organization.

**Availability**:
- Apple Business API 2.6+

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/organizationalUnits/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
      "data": {
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
      },
      "links": {
        "self": "https://api-business.apple.com/v1/organizationalUnits/OU789012"
      }
    }
```

## Topics

### Responses
- [object OrganizationalUnitResponse](./organizationalunitresponse.md)
  A response that contains a single organizational unit resource.

## Endpoint

`GET https://api-business.apple.com/v1/organizationalUnits/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[organizationalUnits]` ([string]): The fields to return for included related types.

  **Allowed Values**: `name`, `description`, `createdDateTime`, `updatedDateTime`, `users`

## Responses

- `200` OK (`OrganizationalUnitResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Organizational Units
- [Get Organizational Units](./get-organizational-units.md)
  Get a list of organizational units in an organization.
- [Get User IDs for an Organizational Unit](./get-all-user-ids-for-an-organizationalunit.md)
  Get a list of user IDs for an organizational unit in an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-organizationalunit-information)*