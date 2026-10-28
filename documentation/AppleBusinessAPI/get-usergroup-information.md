# Get User Group Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific user group in an organization.

**Availability**:
- Apple Business API 2.6+

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/userGroups/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
      "data": {
        "type": "userGroups",
        "id": "UG123456",
        "attributes": {
          "ouId": "OU789012",
          "name": "Engineering Team",
          "type": "STANDARD",
          "totalMemberCount": 25,
          "status": "ACTIVE",
          "createdDateTime": "2023-03-15T10:00:00Z",
          "updatedDateTime": "2024-06-01T14:30:00Z"
        },
        "relationships": {
          "users": {
            "links": {
              "self": "https://api-business.apple.com/v1/userGroups/UG123456/relationships/users"
            }
          }
        },
        "links": {
          "self": "https://api-business.apple.com/v1/userGroups/UG123456"
        }
      },
      "links": {
        "self": "https://api-business.apple.com/v1/userGroups/UG123456"
      }
    }
```

## Topics

### Responses
- [object UserGroupResponse](./usergroupresponse.md)
  A response that contains a single user group resource.

## Endpoint

`GET https://api-business.apple.com/v1/userGroups/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[userGroups]` ([string]): The fields to return for included related types.

  **Allowed Values**: `ouId`, `name`, `type`, `totalMemberCount`, `createdDateTime`, `updatedDateTime`, `status`, `users`

## Responses

- `200` OK (`UserGroupResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### UserGroups
- [Get User Groups](./get-user-groups.md)
  Get a list of user groups in an organization.
- [Get User IDs for a User Group](./get-all-user-ids-for-a-user-group.md)
  Get a list of user IDs for a user group in an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-usergroup-information)*