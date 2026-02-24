# Edit a User

**Framework**: Device Management  
**Kind**: httpRequest

Modify details about a user.

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
  "userId": 100014,
  "email": "test_reg_user15_edited@test.com",
  "sToken": "h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="
}
```

**Response**:

```json
{
  "clientContext": "{\"guid\":\"b92\",\"hostname\":\"test.test.org\",\"ac2\":1}",
  "expirationMillis": 1898103480266,
  "location": {
    "locationId": 2000000003431864,
    "locationName": "cloudMDM Location"
  },
  "status": 0,
  "uId": "100978",
  "user": {
    "clientUserIdStr": "200015",
    "email": "test_reg_user15_edited@test.com",
    "inviteCode": "9e8d1ecc57924d9da13b42b4f772a066",
    "inviteUrl": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?cc=us&inviteCode=9e8d1ecc57924d9da13b42b4f772a066&mt=8",
    "itsIdHash": "C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
    "status": "Registered",
    "userId": 100014
  }
}
```

## Topics

### Request and Response
- [object EditVppUserRequest](editvppuserrequest.md)
  The request to edit a user.
- [object EditVppUserResponse](editvppuserresponse.md)
  The response from editing a user.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/editVPPUserSrv`

## Request Body

missing

## See Also

- [Get a User](get-a-user.md)
  Get information about a particular user.
- [Get Users](get-users-5boi1.md)
  Get information about a set of users.
- [Register a User](register-a-user.md)
  Register a user with the volume-purchase program.
- [Retire a User](retire-a-user.md)
  Retire a user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/edit-a-user)*