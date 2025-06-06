# Manage Licenses

**Framework**: Device Management  
**Kind**: httpRequest

Associate and disassociate licenses with users and devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This endpoint operates on a single asset (specified by the `{adamIdStr, pricingParam}` tuple) for multiple associations and disassociations in a single request.

Licenses are disassociated from all users specified by the `disassociateClientUserIdStrs` array, the devices specified by the `disassociateSerialNumbers` array, or the licenses specified by the `disassociateLicenseIdStrs` array (which must only specify licenses assigned to the specified asset). At most one of these `disassociate*` arrays may be specified per request.

Then licenses are associated either with the users specified by the `associateClientUserIdStrs` array or the devices specified by the `associateSerialNumbers` array. Device assignment doesn’t trigger notifcation.

At most, one `associate*` and one `disassociate*` array is allowed per request. Specifying more than one of either `associate*` or `disassociate*` arrays result in undefined behavior.

##### Example Request and Response with a Serial Number

##### Example Request and Response with a Client User Id String

## Topics

### Request and Response
- [object ManageVppLicensesByAdamIdRequest](managevpplicensesbyadamidrequest.md)
  The request to manage licenses.
- [object ManageVppLicensesByAdamIdResponse](managevpplicensesbyadamidresponse.md)
  The response from managing licenses.

## Request Body

missing

## See Also

- [Get Assets](get-assets-44p83.md)
  Get the set of assets managed by your organization.
- [Get Assignments](get-assignments-158kc.md)
  Get a list of assignments currently assigned to a user or device.
- [Get Licenses](get-licenses.md)
  Get the set of licenses managed by your organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manage-licenses)*