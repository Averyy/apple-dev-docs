# Get a User

**Framework**: Device Management  
**Kind**: httpRequest

Get information about a particular user.

**Availability**:
- VPP License Management 1.0+

#### Discussion

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
    "inviteCode": "201d8c3d520e4b34bec3ed49f20b5b8a",
    "inviteUrl": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?cc=us&inviteCode=201d8c3d520e4b34bec3ed49f20b5b8a&mt=8",
    "itsIdHash": "C2Wwd8LcIaE2v6f2/mvu82Gs/Lc=",
    "licenses":[
         {
            "licenseId":2,
            "adamId":408709785,
            "productTypeId":7,
            "pricingParam":"STDQ",
            "productTypeName":"Software",
            "isIrrevocable":false
         },
         {
            "licenseId":4,
            "adamId":497799835,
            "productTypeId":7,
            "pricingParam":"STDQ",
            "productTypeName":"Software",
            "isIrrevocable":false
         }
      ],
    "status": "Registered",
    "userId": 1
  }
}
```

## Topics

### Request and Response
- [object GetVppUserRequest](getvppuserrequest.md)
  The request for the user details service.
- [object GetVppUserResponse](getvppuserresponse.md)
  The response from the user details service.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/getVPPUserSrv`

## Request Body

missing

## See Also

- [Get Users](get-users-5boi1.md)
  Get information about a set of users.
- [Register a User](register-a-user.md)
  Register a user with the volume-purchase program.
- [Edit a User](edit-a-user.md)
  Modify details about a user.
- [Retire a User](retire-a-user.md)
  Retire a user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-a-user)*