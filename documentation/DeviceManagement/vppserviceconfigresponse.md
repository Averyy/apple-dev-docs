# VppServiceConfigResponse

**Framework**: Device Management  
**Kind**: dictionary

The response with the service configuration.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VppServiceConfigResponse
```

## Properties

- `associateLicenseSrvUrl` (string): The URL for the `Associate License` endpoint. Note the `Associate License` endpoint has been deprecated. Use [`Manage Licenses`](manage-licenses.md) instead.
- `clientConfigSrvUrl` (string): The URL for the [`Client Configuration`](client-configuration.md) endpoint.
- `contentMetadataLookupUrl` (string): The URL that returns metadata about a product in the iTunes Store. See [`Getting App and Book Information (Legacy)`](getting-app-and-book-information-legacy.md), for more information.
- `disassociateLicenseSrvUrl` (string): The URL for the `Disassociate License` endpoint. Note the `Disassociate License`  endpoint has been deprecated. Use [`Manage Licenses`](manage-licenses.md) instead.
- `editUserSrvUrl` (string): The URL for the [`Edit a User`](edit-a-user.md) endpoint.
- `errorCodes` (VppErrorCode): List of possible error numbers and their human-readable explanations.
- `errorMessage` (string): The human-readable explanation of the error.
- `errorNumber` (int32): The numeric code of the error.
- `getLicensesSrvUrl` (string): The URL for the [`Get Licenses`](get-licenses.md) endpoint.
- `getUserSrvUrl` (string): The URL for the [`Get a User`](get-a-user.md) endpoint.
- `getUsersSrvUrl` (string): The URL for the [`Get Users`](get-users-5boi1.md) endpoint.
- `getVPPAssetsSrvUrl` (string): The URL for the [`Get Assets`](get-assets-44p83.md) endpoint.
- `invitationEmailUrl` (string): The URL template for inviting users to an organization.
- `manageVPPLicensesByAdamIdSrvUrl` (string): The URL for the [`Manage Licenses`](manage-licenses.md) endpoint.
- `maxBatchAssociateLicenseCount` (int32): The maximum number of entries allowed in the arrays for associating licenses with [`Manage Licenses`](manage-licenses.md). The MDM server should check this value every 5 minutes, because it could change without notice.
- `maxBatchDisassociateLicenseCount` (int32): The maximum number of entries allowed in the arrays for disassociating licenses from [`Manage Licenses`](manage-licenses.md). The MDM server should check this value every 5 minutes, because it could change without notice.
- `registerUserSrvUrl` (string): The URL for the [`Register a User`](register-a-user.md) endpoint.
- `retireUserSrvUrl` (string): The URL for the [`Retire a User`](retire-a-user.md) endpoint.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. `-1` = Failure.
- `vppWebsiteUrl` (string): The URL for the VPP website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppserviceconfigresponse)*