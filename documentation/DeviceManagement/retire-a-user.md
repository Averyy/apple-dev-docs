# Retire a User

**Framework**: Device Management  
**Kind**: httpRequest

Retire a user account.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This service disassociates a VPP user from its iTunes account and releases the revocable licenses associated with the VPP user. The revoked licenses can then be assigned to other users in the organization.

Currently, ebook licenses are irrevocable.

A retired VPP user can be reregistered, in the same organization, using the [`Register a User`](register-a-user.md) endpoint.

##### Example Request and Response

**Request**:

```None
{
  "userId": 1,
  "sToken": "h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="
}
```

**Response**:

```json
{
  "clientContext": "{\"guid\":\"b92\",\"hostname\":\"test.test.org\",\"ac2\":1}",
  "expirationMillis": 1898103480266,
  "location": {
    "locationId": 22222222222,
    "locationName": "LocationName"
  },
  "status": 0,
  "uId": "100978",
  "user": {
    "clientUserIdStr": "200006",
    "email": "user1@test.com",
    "licenses": [
      {
        "licenseId": 2,
        "adamId": 408709785,
        "productTypeId": 10,
        "pricingParam": "STDQ",
        "productTypeName": "Publication",
        "isIrrevocable": true
      }
    ],
    "status": "Retired",
    "userId": 1
  }
}
```

## Topics

### Request and Response
- [object RetireVppUserRequest](retirevppuserrequest.md)
  The request to retire a user.
- [object RetireVppUserResponse](retirevppuserresponse.md)
  The response from retiring a user.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/retireVPPUserSrv`

## Request Body

missing

## See Also

- [Get a User](get-a-user.md)
  Get information about a particular user.
- [Get Users](get-users-5boi1.md)
  Get information about a set of users.
- [Register a User](register-a-user.md)
  Register a user with the volume-purchase program.
- [Edit a User](edit-a-user.md)
  Modify details about a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retire-a-user)*