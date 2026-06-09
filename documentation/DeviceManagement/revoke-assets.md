# Revoke Assets

**Framework**: Device Management  
**Kind**: httpRequest

Revoke assets from client user IDs and serial numbers.

**Availability**:
- VPP License Management 2.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
{
    "clientUserIds": [
        "client-1",
        "client-2"
    ],
    "serialNumbers": [
        "serial-1",
        "serial-2"
    ]
}
```

**Response**:

```json
{
    "eventId": "ed3edfc3-e617-465e-b309-a17925266e14",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

## Topics

### Request and Response
- [object RevokeAssetsRequest](revokeassetsrequest.md)
  The request for asset revocation.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/assets/revoke`

## Request Body

missing

## See Also

- [Get Assets](get-assets-4ski1.md)
  Get the set of assets that your organization manages.
- [Associate Assets](associate-assets.md)
  Associate assets with client user IDs and serial numbers.
- [Disassociate Assets](disassociate-assets.md)
  Disassociate assets from client user IDs and serial numbers.
- [Get Assignments](get-assignments-9wv1e.md)
  Get the set of current assignments for users or devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/revoke-assets)*