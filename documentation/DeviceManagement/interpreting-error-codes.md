# Interpreting Error Codes

**Framework**: Device Management

Investigate service request errors and troubleshoot solutions.

#### Overview

When a service request results in error, there are normally two fields containing the error information in the response: an `errorNumber` field and an `errorMessage` field. There could be additional fields depending on the error.

The `errorMessage` field contains human-readable text explaining the error. The `errorNumber` field is intended for software to interpret. Any `errorMessage` value uniquely maps to an `errorNumber` value, but not the other way around.

##### Error Codes and Descriptions

| ErrorNumber | ErrorMessage |
| --- | --- |
| 9600 | Missing required argument. |
| 9601 | Login required. |
| 9602 | Invalid argument. |
| 9603 | Internal error. See [`Error Code 9603`](interpreting-error-codes#Error-Code-9603.md) for more information. |
| 9604 | Result not found. |
| 9605 | Account storefront incorrect. |
| 9606 | Error constructing token. |
| 9607 | License is irrevocable. |
| 9608 | Empty response from SharedData service. |
| 9609 | Registered user not found. |
| 9610 | License not found. |
| 9611 | Admin user not found. |
| 9612 | Failed to create claim job. |
| 9613 | Failed to create unclaim job. |
| 9614 | Invalid date format. |
| 9615 | OrgCountry not found. |
| 9616 | License already assigned. See [`Error Code 9616`](interpreting-error-codes#Error-Code-9616.md) for more information. |
| 9618 | The user has already been retired. |
| 9619 | License not associated. |
| 9620 | The user has already been deleted. |
| 9621 | The token has expired. Generate a new token in Apple School Manager. |
| 9622 | Invalid authentication token. |
| 9623 | Invalid Apple push notification token. |
| 9624 | License was refunded and is no longer valid. |
| 9625 | The sToken has been revoked. |
| 9626 | License already assigned to a different user. The MDM server should retry the assignment with a different license. |
| 9628 | Ineligible device assignment: MDM tried to assign an item to a serial number but device assignment is not allowed for that item. |
| 9630 | Too many recent already-assigned errors: If MDM gets the same 9616 error from assignments for the same organization, user identifier, and item identifier (license ID, adam ID, or pricing parameter) and does so within too short a time (generally several minutes), it  return this error code. |
| 9631 | Too many recent already-assigned errors: If MDM gets the same 9616 error from assignments for the same organization, user identifier, and item identifier (license ID, adam ID, or pricing parameter) and does so within too short a time (generally several minutes), it  return this error code. |
| 9632 | Too many recent manage-license calls with identical request: If MDM gets precisely the same request to `manageVPPLicensesByAdamIdSrv` too many times within too short a time (generally several minutes), it  return this error code. |
| 9633 | Data for a batch token passed could not be recovered. |
| 9634 | Returned when a caller tries to use a formerly deprecated featured that has been removed. |
| 9635 | The Apple Account passed for iTunes Store association cannot be found or is not applicable to organization of the user (see [`Managed Apple Accounts`](associating-an-apple-id-with-a-volume-purchase-program-vpp-user#Managed-Apple-Accounts.md)). |
| 9636 | Registered user not found. |
| 9637 | `sToken` is not allowed to perform the operation requested. |
| 9638 | The content manager account that generated `sToken` has no Managed ID organization ID and cannot manipulate the content manager requested. |
| 9641 | The Apple Account already associated to registered user. |
| 9642 | The Apple Account passed cannot be used at this time because it’s a VPP manager and the iTunes Store account not yet created and such creation requires user to agree to Terms. |
| 9643 | The license is currently locked for a pending transfer. Please try again later. |
| 9644 | Volume Purchase Program is currently in maintenance mode. Please try again later. |
| 9645 | This location is managed by Apple’s cloud MDM. Only read operations are allowed for this location. |
| 9646 | There are too many requests for the current Organization and the request has been rejected, either due to high server volume or an MDM issue. Use an incremental/exponential backoff strategy to retry the request until successful. |

Additional error codes may be added in the future.

###### Error Code 9616

Error number 9616 is returned when an attempt is made to assign a license to a user or device that already has a license for the specified app or book, in which case there’s no need to retry the assignment.

Additional information is returned to MDM when a `9616` error occurs. Sometimes, itʼs because the specific user in the request is already assigned to the item in question. When that happens, the `9616` error is accompanied by a `licenseAlreadyAssigned` entry with details about the user and the license. For example,

```swift
{
  "licenseAlreadyAssigned": {
    "pricingParam": "STDQ",
    "itsIdHash": "XuHVGvasXcfEVUUn4EP2wjHEUK00s=",
    "userId": 9918783273,
    "productTypeId": 8,
    "isIrrevocable": false,
    "adamIdStr": "778658393",
    "userIdStr": "9918783273",
    "licenseIdStr": "99147599840",
    "productTypeName": "Application",
    "clientUserIdStr": "xxutt8-e079-4b05-b403-a0792890",
    "licenseId": 9147599840,
    "adamId": 778658393,
    "status": "Associated"
  },
"regUsersAlreadyAssigned": [
    {
      "itsIdHash": "XuHVGvasXcfEVUUn4EP2wjHEUK00s=",
      "clientUserIdStr": "xxutt8-e079-4b05-b403-a0792890",
      "userId": 9918783273,
      "email": "user@example.apple.com",
      "status": "Associated"
    }
  ],

  "errorMessage": "License already assigned",
  "errorNumber": 9616,
  "status": -1
}
```

Alternatively, a `9616` error may have a `regUsersAlreadyAssigned` entry in the response, with information about the one or more other users who already have the item in question. In these cases, the VPP user specified by the user ID or the `clientUserIdStr` does not have the item, but some other users in the organization associated with the same iTunes Store account have the item. If that happens, the server returns `9616` and information about those other users:

```swift
{
  "errorMessage": "License already assigned",
  "regUsersAlreadyAssigned": [
    {
      "itsIdHash": "XXX2CVvZar9YZnpqJxV0SHOUCU=",
      "clientUserIdStr": "jjjCXhHHee0e3c-x999-43a9-Xe04-1dcax80ac01x",
      "userId": 9991992450,
      "email": "user@example.apple.com",
      "status": "Associated"
    }
  ],
  "errorNumber": 9616,
  "status": -1
}
```

###### Error Code 9603

Receiving a `9603` `Internal Error` response typically indicates the VPP server couldnʼt provide timely processing. Nothing is necessarily wrong with the request. When the MDM server receives this response, it should send the current request again. If it continues to receive `9603` errors after more than five attempts, it may mean that the VPP service is unexpectedly down and further retries should be scheduled for minutes later, instead of seconds.

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services-legacy.md)
  Associate volume purchases with users or devices using endpoints for Mobile Device Management (MDM), provided by the Volume Purchase Program (VPP).
- [Upgrading to Apple School Manager (ASM) and Apple Business Manager (ABM)](upgrading-to-apple-school-manager-asm-and-apple-business-manager-abm.md)
  Manage devices and content across an organization user base with a single destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/interpreting-error-codes)*