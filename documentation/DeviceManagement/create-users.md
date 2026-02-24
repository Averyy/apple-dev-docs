# Create Users

**Framework**: Device Management  
**Kind**: httpRequest

Create users to assign apps and books to.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

##### Example Request and Response

**Request**:

```None
{
    "users": [
        {
            "clientUserId": "client-100",
            "email": "client-100@next.com",
            "managedAppleId": "maid-100@next.com"
        },
        {
            "clientUserId": "client-101",
            "email": "client-101@next.com",
            "managedAppleId": "maid-101@next.com"
        },
        {
            "clientUserId": "client-102",
            "email": "client-102@next.com"
        }
    ]
}
```

**Response**:

```json
{
    "eventId": "af70eb9b-0ab6-405d-87d8-3b9ed0c4f370",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

## Topics

### Request and Response
- [object ManageUsersRequest](manageusersrequest.md)
  The request for user management.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/users/create`

## Request Body

missing

## See Also

- [Get Users](get-users-4mwln.md)
  Get information about a set of users.
- [Update Users](update-users.md)
  Update details for existing users.
- [Retire Users](retire-users.md)
  Retire users by client user IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/create-users)*