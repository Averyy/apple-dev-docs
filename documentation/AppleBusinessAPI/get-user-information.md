# Get User Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific user in an organization.

**Availability**:
- Apple Business API 2.6+

##### Example

**Request**:

```
curl "https://api-business.apple.com/v1/users/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
      "data": {
        "type": "users",
        "id": "1234567890",
        "attributes": {
          "firstName": "John",
          "lastName": "Doe",
          "middleName": "A",
          "status": "ACTIVE",
          "managedAppleAccount": "john.doe@appleid.example.com",
          "isExternalUser": false,
          "roleOuList": [
            {
              "roleName": "Administrator",
              "ouId": "OU123456"
            }
          ],
          "email": "john.doe@example.com",
          "employeeNumber": "EMP001",
          "costCenter": "CC100",
          "division": "Engineering",
          "department": "IT",
          "jobTitle": "Software Engineer",
          "startDateTime": "2023-01-15T08:00:00Z",
          "createdDateTime": "2023-01-10T10:30:00Z",
          "updatedDateTime": "2024-06-01T14:22:00Z",
          "phoneNumbers": [
            {
              "phoneNumber": "+1-555-123-4567",
              "type": "WORK"
            }
          ]
        },
        "links": {
          "self": "https://api-business.apple.com/v1/users/1234567890"
        }
      },
      "links": {
        "self": "https://api-business.apple.com/v1/users/1234567890"
      }
    }
```

## Topics

### Responses
- [object UserResponse](./userresponse.md)
  A response that contains a single user resource.

## Endpoint

`GET https://api-business.apple.com/v1/users/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[users]` ([string]): The fields to return for included related types.

  **Allowed Values**: `firstName`, `lastName`, `middleName`, `status`, `managedAppleAccount`, `isExternalUser`, `roleOuList`, `email`, `employeeNumber`, `costCenter`, `division`, `department`, `jobTitle`, `startDateTime`, `createdDateTime`, `updatedDateTime`, `phoneNumbers`

## Responses

- `200` OK (`UserResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Users
- [Get Users](./get-users.md)
  Get a list of users in an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-user-information)*