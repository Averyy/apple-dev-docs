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

## Topics

### Request and Response
- [object GetVppLicensesRequest](getvpplicensesrequest.md)
  The request for licenses.
- [object GetVppLicensesResponse](getvpplicensesresponse.md)
  The response with the licenses.

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