# Update Users

**Framework**: Device Management  
**Kind**: httpRequest

Update details for existing users.

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
            "email": "client-100@apple.com"
        },
        {
            "clientUserId": "client-101",
            "email": "client-101@apple.com"
        },
        {
            "clientUserId": "client-102",
            "email": "client-102@apple.com",
            "managedAppleId": "maid-102@apple.com"
        }
    ]
}
```

**Response**:

```json
{
    "eventId": "dcd54e0c-5898-4837-8cea-b220f9570835",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000"
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

`POST https://vpp.itunes.apple.com/mdm/v2/users/update`

## Request Body

missing

## See Also

- [Get Users](get-users-4mwln.md)
  Get information about a set of users.
- [Create Users](create-users.md)
  Create users to assign apps and books to.
- [Retire Users](retire-users.md)
  Retire users by client user IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/update-users)*