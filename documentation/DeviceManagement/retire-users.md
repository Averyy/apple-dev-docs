# Retire Users

**Framework**: Device Management  
**Kind**: httpRequest

Retire users by client user IDs.

**Availability**:
- VPP License Management 2.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
{
    "users": [
        {
            "clientUserId": "client-100"
        },
        {
            "clientUserId": "client-101"
        }
    ]
}
```

**Response**:

```json
{
    "eventId": "dafdad60-4ef6-49b0-8150-64323f56d88d",
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

`POST https://vpp.itunes.apple.com/mdm/v2/users/retire`

## Request Body

missing

## See Also

- [Get Users](get-users-4mwln.md)
  Get information about a set of users.
- [Create Users](create-users.md)
  Create users to assign apps, books, and subscriptions to.
- [Update Users](update-users.md)
  Update details for existing users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retire-users)*