# Get Users

**Framework**: Device Management  
**Kind**: httpRequest

Get information about a set of users.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Retrieving a Large Record Set](retrieving-a-large-record-set.md)
- [Handling Error Responses](handling-error-responses.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
{
  "batchToken": null,
  "sinceModifiedToken": null,
  "includeRetired": 1,
  "includeRetiredOnly": false,
  "ifModifiedSince": null,
  "overrideIndex": null,
  "sToken": "h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2 a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="
}
```

**Response**:

```json
{
  "clientContext": "{\"guid\":\"b92\",\"hostname\":\"test.test.org\",\"ac2\":1}",
  "batchCount": 4,
  "expirationMillis": 1898103480266,
  "location": {
    "locationId": 22222222222,
    "locationName": "LocationName"
  },
  "sinceModifiedToken": "H4sIAAAAAAAAAKtWMFCwVdBQMDQwMDEwV9C0VlAoyS9JzHFKLEnOSC12yy/NS3EGEiVAVYZAycw03/yUzLTM1JTgzLzkVN/MnJzMYpCcqamJiaGlkbGBiakZiiEw3QYg0cqCVCBTqRisF2qQEsjYvOSc0pTUoNSSzKLUFIhdtQAHYCyLnAAAAA==",
  "status": 0,
  "totalBatchCount": "0",
  "totalCount": 4,
  "uId": "100978",
  "users": [
    {
      "userId": 1,
      "email": "user1@test.com",
      "clientUserIdStr": "200006",
      "status": "Associated",
      "itsIdHash": "C2Wwd8LcIaE2v6f2/mvu82Gs/Lc="
    },
    {
      "userId": 2,
      "email": "user2@test.com",
      "clientUserIdStr": "200007",
      "status": "Associated",
      "itsIdHash": "*leSKk3IaE2vk2KLmv2k3/200D3="
    },
    {
      "userId": 3,
      "email": "user3@test.com",
      "clientUserIdStr": "user3@test.com",
      "status": "Registered",
      "inviteCode": "f551b37da07146628e8dcbe0111f0364",
      "inviteUrl": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?inviteCode=f551b37da07146628e8dcbe0111f0364&mt=8"
    },
    {
      "userId": 4,
      "email": "user4@test.com",
      "clientUserIdStr": "user4@test.com",
      "status": "Registered",
      "inviteUrl": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?inviteCode=859c5aa3485a48918a5f4f70c5629ec8&mt=8",
      "inviteCode": "859c5aa3485a48918a5f4f70c5629ec8"
    }
  ]
}
```

## Topics

### Request and Response
- [object GetVppUsersRequest](getvppusersrequest.md)
  The request for the users’ details service.
- [object GetVppUsersResponse](getvppusersresponse.md)
  The response from the users’ details service.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/getVPPUsersSrv`

## Request Body

missing

## See Also

- [Get a User](get-a-user.md)
  Get information about a particular user.
- [Register a User](register-a-user.md)
  Register a user with the volume-purchase program.
- [Edit a User](edit-a-user.md)
  Modify details about a user.
- [Retire a User](retire-a-user.md)
  Retire a user account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-users-5boi1)*