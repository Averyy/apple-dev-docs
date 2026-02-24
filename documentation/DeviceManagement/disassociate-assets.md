# Disassociate Assets

**Framework**: Device Management  
**Kind**: httpRequest

Disassociate assets from client user IDs and serial numbers.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
{
    "assets": [
        {
            "adamId": "408709785",
            "pricingParam": "STDQ"
        },
        {
            "adamId": "377298193",
            "pricingParam": "STDQ"
        }
    ],
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
- [object ManageAssetsRequest](manageassetsrequest.md)
  The request for asset management.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/assets/disassociate`

## Request Body

missing

## See Also

- [Get Assets](get-assets-4ski1.md)
  Get the set of assets that your organization manages.
- [Associate Assets](associate-assets.md)
  Associate assets with client user IDs and serial numbers.
- [Revoke Assets](revoke-assets.md)
  Revoke assets from client user IDs and serial numbers.
- [Get Assignments](get-assignments-9wv1e.md)
  Get the set of current assignments for users or devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disassociate-assets)*