# Get Users

**Framework**: Device Management  
**Kind**: httpRequest

Get information about a set of users.

**Availability**:
- VPP License Management 2.0+

## Mentions

- [Getting started with the management API](getting-started-with-the-management-api.md)
- [Upgrading to the new management API](upgrading-to-the-new-management-api.md)
- [Using paginated endpoints](using-paginated-endpoints.md)
- [Managing users](managing-users.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
?activeOnly=true
```

**Response**:

```json
{
    "currentPageIndex": 0,
    "size": 3,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "users": [
        {
            "clientUserId": "client-101",
            "email": "client-101@apple.com",
            "inviteCode": "46bc93ea3acd41e0a4919c02db0d7d3a",
            "status": "Registered"
        },
        {
            "clientUserId": "client-102",
            "email": "client-102@apple.com",
            "inviteCode": "d2ab1319ff6448f89bb1b0e010cf68e0",
            "status": "Registered"
        },
        {
            "clientUserId": "client-103",
            "email": "client-1031@apple.com",
            "status": "Retired"
        }
    ],
    "versionId": "021f10a0-7035-11eb-9f67-bd1df52e1e13"
}
```

## Topics

### Response
- [object GetUsersResponse](getusersresponse.md)
  The paginated response that contains the requested users.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/users`

## Parameters

- `activeOnly` (boolean): The filter for only the active users.
- `clientUserId` (string): The filter for the unique identifier of a user in your organization.
- `pageIndex` (int32): The requested page index.
- `retiredOnly` (boolean): The filters for only the retired users.
- `sinceVersionId` (string): The filter for modified assignments since the specified version identifier.

## See Also

- [Create Users](create-users.md)
  Create users to assign apps, books, and subscriptions to.
- [Update Users](update-users.md)
  Update details for existing users.
- [Retire Users](retire-users.md)
  Retire users by client user IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-users-4mwln)*