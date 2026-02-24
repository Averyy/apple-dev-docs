# Register a User

**Framework**: Device Management  
**Kind**: httpRequest

Register a user with the volume-purchase program.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Associating an Apple Account with a Volume Purchase Program (VPP) User](associating-an-apple-id-with-a-volume-purchase-program-vpp-user.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
{
  "email": "test_reg_user11@test.com",
  "clientUserIdStr": "200002",
  "sToken": "h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Ropo4KDn3MKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="
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
    "clientUserIdStr": "200002",
    "email": "test_reg_user11@test.com",
    "inviteCode": "9e8d1ecc57924d9da13b42b4f772a066",
    "inviteUrl": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?cc=us&inviteCode= 89e8d1ecc57924d9da13b42b4f772a066&mt=8",
    "status": "Registered",
    "userId": 100014
  }
}
```

## Topics

### Request and Response
- [object RegisterVppUserRequest](registervppuserrequest.md)
  The request for registering a user.
- [object RegisterVppUserResponse](registervppuserresponse.md)
  The response from registering a user.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/registerVPPUserSrv`

## Request Body

missing

## See Also

- [Get a User](get-a-user.md)
  Get information about a particular user.
- [Get Users](get-users-5boi1.md)
  Get information about a set of users.
- [Edit a User](edit-a-user.md)
  Modify details about a user.
- [Retire a User](retire-a-user.md)
  Retire a user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/register-a-user)*