# Get Assets

**Framework**: Device Management  
**Kind**: httpRequest

Get the set of assets that your organization manages.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Using Paginated Endpoints](using-paginated-endpoints.md)
- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
- [Managing Assets](managing-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
?pageIndex=0&pricingParam=STDQ&productType=App
```

**Response**:

```json
{
    "assets": [
        {
            "adamId": "408709785",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "377298193",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "361309726",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "361304891",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "361285480",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        }
    ],
    "currentPageIndex": 0,
    "size": 5,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "versionId": "70e8c740-514c-11eb-bb63-a90b882fcd52"
}
```

## Topics

### Response
- [object GetAssetsResponse](getassetsresponse.md)
  The paginated response that contains the requested assets.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/assets`

## Parameters

- `pageIndex` (int32): The requested page index.
- `productType` (string): The filter for the asset product type.
- `pricingParam` (string): The filter for the asset product quality.
- `revocable` (boolean): The filter for asset revocability.
- `deviceAssignable` (boolean): The filter for asset device assignability.
- `maxAvailableCount` (int32): The filter for the maximum inclusive assets available count.
- `minAvailableCount` (int32): The filter for the minimum inclusive assets available count.
- `maxAssignedCount` (int32): The filter for the maximum inclusive assets assigned count.
- `minAssignedCount` (int32): The filter for the minimum inclusive assets assigned count.
- `adamId` (string): The filter for the asset product unique identifier.

## See Also

- [Associate Assets](associate-assets.md)
  Associate assets with client user IDs and serial numbers.
- [Disassociate Assets](disassociate-assets.md)
  Disassociate assets from client user IDs and serial numbers.
- [Revoke Assets](revoke-assets.md)
  Revoke assets from client user IDs and serial numbers.
- [Get Assignments](get-assignments-9wv1e.md)
  Get the set of current assignments for users or devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-assets-4ski1)*