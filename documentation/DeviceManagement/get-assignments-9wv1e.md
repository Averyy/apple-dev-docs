# Get Assignments

**Framework**: Device Management  
**Kind**: httpRequest

Get the set of current assignments for users or devices.

**Availability**:
- VPP License Management 2.0+

## Mentions

- [Getting started with the management API](getting-started-with-the-management-api.md)
- [Upgrading to the new management API](upgrading-to-the-new-management-api.md)
- [Using paginated endpoints](using-paginated-endpoints.md)
- [Managing assets](managing-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
?adamId=408709785
```

**Response**:

```json
{
    "assignments": [
        {
            "adamId": "408709785",
            "clientUserId": "client-1",
            "pricingParam": "STDQ"
        },
        {
            "adamId": "408709785",
            "serialNumber": "serial-1",
            "pricingParam": "STDQ"
        }
    ],
    "size": 2,
    "currentPageIndex": 0,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "versionId": "009061cb-87d1-4ea8-ae4c-7849dc49224e"
}
```

## Topics

### Response
- [object GetAssignmentsResponse](getassignmentsresponse.md)
  The paginated response that contains requested assignments.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/assignments`

## Parameters

- `adamId` (string): The filter for the assignment product’s unique identifier.
- `clientUserId` (string): The filter for the unique identifier of assigned users in your organization.
- `excludeInactiveUsers` (boolean)
- `includeUserState` (boolean)
- `pageIndex` (int32): The requested page index.
- `pricingParam` (string)
- `serialNumber` (string): The filter for the unique identifier of assigned devices in your organization.
- `sinceVersionId` (string): The filter for modified assignments since the specified version identifier.

## See Also

- [Get Assets](get-assets-4ski1.md)
  Get the set of assets that your organization manages.
- [Associate Assets](associate-assets.md)
  Associate assets with client user IDs and serial numbers.
- [Disassociate Assets](disassociate-assets.md)
  Disassociate assets from client user IDs and serial numbers.
- [Revoke Assets](revoke-assets.md)
  Revoke assets from client user IDs and serial numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-assignments-9wv1e)*