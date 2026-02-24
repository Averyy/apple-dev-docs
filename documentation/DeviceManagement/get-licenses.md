# Get Licenses

**Framework**: Device Management  
**Kind**: httpRequest

Get the set of licenses managed by your organization.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Retrieving a Large Record Set](retrieving-a-large-record-set.md)
- [Upgrading to Apple School Manager (ASM) and Apple Business Manager (ABM)](upgrading-to-apple-school-manager-asm-and-apple-business-manager-abm.md)

#### Discussion

This call returns an exhaustive list of individual licenses managed by your organization. For performance reasons, it’s recommended that you use a combination of [`Get Assets`](get-assets-44p83.md)  and [`Get Assignments`](get-assignments-158kc.md) as described in the initial import process in [`Managing Apps and Books Through Web Services`](managing-apps-and-books-through-web-services-legacy.md) instead of this API.

Additionally, it’s not recommended to use the Apple license IDs returned in the [`GetVppLicensesResponse`](getvpplicensesresponse.md) in MDM implementations because it creates an unnecessary dependence on internal data models, which can change.

##### Example Request and Response

**Request**:

```None
{
  "batchToken": null,
  "sinceModifiedToken": null,
  "adamId": null,
  "sToken": "h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2 a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ=",
  "pricingParam": null,
  "serialNumber": null,
  "assignedOnly": true,
  "userAssignedOnly": false,
  "deviceAssignedOnly": false,
  "ifModifiedSince": null,
  "overrideIndex": null
}
```

**Response**:

```json
{
  "batchCount": 183,
  "batchToken": "H4sIAAAAAAAAAEWOUQvCIBSF/4rsXZlO3SJ6aRBEjR76BZteSyY6moNG9N/TIHq5nHO55zv3hWKIvdv3Ud1hPoTF6zaNiHZIbhGyXsMzaZq0C2FcphOsyRfnY0uGHCIxjOAJJazmnELTYKXkgLluGB5KzfDGGC6YUlQyUyTMv+9XxPJ2nSBzv8x8Zk0XtDUW9NV6BZ11zs6Xh73lb4TgvGRVWclabNH7A91iXJzFAAAA",
  "clientContext": "{\"guid\":\"b92\",\"hostname\":\"test.test.org\",\"ac2\":1}",
  "expirationMillis": 1898103480266,
  "ifModifiedSinceMillisOrig": "1554402303675",
  "licenses": [
    {
      "adamId": 408709785,
      "adamIdStr": "408709785",
      "clientUserIdStr": "9a17b450-9820-471e-b232-13a479ddede0",
      "isIrrevocable": false,
      "itsIdHash": "LsrJ6NhzbsOzQXShrpUTWGnD/X8=",
      "licenseId": 102547,
      "licenseIdStr": "102547",
      "pricingParam": "STDQ",
      "productTypeId": 8,
      "productTypeName": "Application",
      "status": "Associated",
      "userId": 10715446,
      "userIdStr": "10715446"
    },
    {
      "adamId": 435160039,
      "adamIdStr": "435160039",
      "clientUserIdStr": "9a17b450-9820-471e-b232-13a479ddede0",
      "isIrrevocable": true,
      "itsIdHash": "LsrJ6NhzbsOzQXShrpUTWGnD/X8=",
      "licenseId": 795047681,
      "licenseIdStr": "795047681",
      "pricingParam": "PLUS",
      "productTypeId": 10,
      "productTypeName": "Publication",
      "status": "Associated",
      "userId": 6561022,
      "userIdStr": "6561022"
    },
    {
      "adamId": 645859810,
      "adamIdStr": "645859810",
      "isIrrevocable": false,
      "licenseId": 967494668,
      "licenseIdStr": "967494668",
      "pricingParam": "STDQ",
      "productTypeId": 8,
      "productTypeName": "Application",
      "serialNumber": "C39N3035G68P",
      "status": "Associated"
    }
  ],
  "location": {
    "locationId": 22222222222,
    "locationName": "LocationName"
  },
  "status": 0,
  "totalBatchCount": "2",
  "totalCount": 416,
  "uId": "100978"
}
```

## Topics

### Request and Response
- [object GetVppLicensesRequest](getvpplicensesrequest.md)
  The request for licenses.
- [object GetVppLicensesResponse](getvpplicensesresponse.md)
  The response with the licenses.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/getVPPLicensesSrv`

## Request Body

missing

## See Also

- [Get Assets](get-assets-44p83.md)
  Get the set of assets managed by your organization.
- [Get Assignments](get-assignments-158kc.md)
  Get a list of assignments currently assigned to a user or device.
- [Manage Licenses](manage-licenses.md)
  Associate and disassociate licenses with users and devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-licenses)*