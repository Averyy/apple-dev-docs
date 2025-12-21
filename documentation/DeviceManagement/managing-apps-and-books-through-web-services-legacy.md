# Managing Apps and Books Through Web Services

**Framework**: Device Management

Associate volume purchases with users or devices using endpoints for Mobile Device Management (MDM), provided by the Volume Purchase Program (VPP).

#### Overview

Volume Purchase Program (VPP) allows an organization to manage and assign apps to users. If a user no longer needs an app, you can reclaim the app license and assign it to a different user. VPP can also assign a license to a device’s serial number, so an Apple Account is not required to download the app.

##### Authentication

All endpoints (except for [`Service Configuration`](service-configuration.md)) require an `sToken` parameter to authenticate.

Content managers can download a location-based `sToken` from the settings page in [`Upgrading to Apple School Manager (ASM) and Apple Business Manager (ABM)`](upgrading-to-apple-school-manager-asm-and-apple-business-manager-abm.md), and upload it into their MDM. This grants the MDM access to the licenses available at that location.

![Download a location-based token from the settings page and upload it to your MDM](https://docs-assets.developer.apple.com/published/64f7ab887e7d38afa4d27e12423d914d/media-3230503%402x.png)

The MDM server should store the location-based token along with its other private, protected properties and pass this token in the `sToken` field of all VPP API requests.

The `sToken` itself is a JSON object in Base64 encoding. When decoded, the resulting JSON object contains three fields: `token`, `expDate`, and `orgName`. For example, the following is an `sToken` value:

```swift
eyJ0b2tlbiI6InQxWG9VenBMRXRwZGxhK25zeENkd3JjdDBSandkaWNOaGRreW5STW05VVAyc2hSYTBMUnVGcVpQM0pLQmJUTWxDSE42ajNta1R6WVlQbVVkVXJXV2x3PT0iLCJleHBEYXRlIjoiMjAxNC0wOC0xNVQxODoxMzo1Mi0wNzAwIiwib3JnTmFtZSI6Ik9SRy4yMDA5MDcxNjAwIn0=
```

After Base64 decoding, this is the JSON:

```swift
{
  "token": "t1XoUzpLEtpdla+nsxCdwrct0RjwdicNhdkynRMm9UP2shRa0LRuFqZP3JKBbTMlCHN6j3mkTzYYPmUdUrWWlw==",
  "expDate": "2014-08-15T18:13:52-0700",
  "orgName": "ORG2009071600"
}
```

The `expDate` field contains the expiration date of the token in ISO 8601 format. The `orgName` field contains the name of the organization for which the token is issued.

If the provided token is within the expiration warning period (currently 15 days before the expiration date), then the response contains an additional field, `tokenExpDate`. The value of this field is the expiration date in ISO 8601 format. For example:

```swift
"tokenExpDate":"2013-07-26T18􏰁12􏰁09-0700" 
```

If this field is present in the response, it should serve as a reminder that it is time to get a new sToken in order to avoid any service disruption.

##### Read Only Access

You can tailor different sets of privileges for individual content managers using Managed Apple Accounts. This allows a fine range of control over what these users can do. For example, a content manager that only has the “Read Only” privileges can use the [`Get a User`](get-a-user.md), [`Get Users`](get-users-5boi1.md), and [`Get Assets`](get-assets-44p83.md) endpoints, but can’t use the [`Retire a User`](retire-a-user.md) or [`Manage Licenses`](manage-licenses.md) endpoints. You can also assign content managers “Can Purchase” and/or “Can Manage” privileges, so that an individual content manager can manage licenses but not buy them.

> **Note**:  Purchasing users and managing users automatically have read privileges.

##### Responses

As a convention, fields with null values are not included in responses. For example, the user object has an optional `email` field. The following example doesn’t have the `email` field in the user object, so the `email` field value is null.

```swift
"user":{
  "userId": 1,
  "clientUserIdStr": "810C9B91-DF83-41DA-80A1-408AD7F081A8",
  "itsIdHash": "C2Wwd8LcIaE2v6f2/mvu82Gs/Lc=",
  "status": "Associated",
  "licenses": [
    {
      "licenseId": 2,
      "adamId": 408709785,
      "productTypeId": 7,
      "pricingParam": "STDQ",
      "productTypeName": "Software",
      "isIrrevocable": false
    },
    {
      "licenseId": 4,
      "adamId": 497799835,
      "productTypeId": 7,
      "pricingParam": "STDQ",
      "productTypeName": "Software",
      "isIrrevocable": false
    }
  ]
}
```

If the user doesn’t have any licenses, the `licenses` field will not be included in the response. The license object in this context is a subfield of the user object. To avoid a cyclic reference, the user object is not included in the license object. But if the license is the top object returned, it includes a user object with `userId` and `clientUserIdStr` fields and, if the user is already associated with an iTunes account, an `itsIdHash` field.

##### Initial Import of Assigned Licenses

You don’t need to sync every license for a specific VPP account. You only need to track the asset counts and assignments. There is also no need to record the Apple license IDs; in fact, this isn’t recommended because it creates an unnecessary dependence on an internal data model, which can change. The recommended procedure to import licenses is to import license counts and then import the current assignments for each asset. Accomplish this in the following way:

1. Send a request to [`Get Assets`](get-assets-44p83.md) with `includeLicenseCounts=true`. This returns the current license count by `adamID` in the requested location.
2. For each `adamId` in the [`GetVppAssetResponse`](getvppassetresponse.md) from step 1, send a request to [`Get Assignments`](get-assignments-158kc.md). Record the `adamIdStr`, `pricingParam` and `clientUserIdStr` or `serialNumber` for each assignment in the [`VppAssignmentsResponse`](vppassignmentsresponse.md). Also record the `currentPageIndex` and `totalPages`.
3. Send another request to [`Get Assignments`](get-assignments-158kc.md) that includes the `nextPageIndex` value from step 2 as `pageIndex`, and record the values as described in step 2.
4. Repeat step 3 until `currentPageIndex` is equal to `totalPages` in the [`VppAssignmentsResponse`](vppassignmentsresponse.md).

See [`Retrieving a Large Record Set`](retrieving-a-large-record-set.md) for more information about using the `batchToken` and `sinceModifiedToken`.

##### Retry After Header

The VPP service may return a `503 Service Unavailable` status to clients whose requests result in an unusually high load on the VPP service, or when the VPP service is experiencing loads beyond its current request response capacity. A `Retry-After` header may be included in this response, indicating how long the client must wait before making additional requests. Clients who make requests before this time may be rejected for even longer periods of time, or (in extreme cases) may have their VPP account suspended.

Avoid triggering the `Retry-After` header by setting the `assignedOnly` parameter `true` in calls to [`Get Licenses`](get-licenses.md).

The `Retry-After` response-header field may also be used with any 3xx (Redirection) response to indicate the minimum time the user-agent is asked to wait before issuing the redirected request (see RFC 2616: HTTP/1.1, Section 14.37). The value of this field can be either an HTTP-date or an integer number of seconds (in decimal) after the time of the response.

```swift
Retry-After = "Retry-After" ":" ( HTTP-date | delta-seconds ) 
```

Two examples of usage are:

```swift
Retry-After: Fri, 31 Dec 1999 23:59:59 GMT
```

```swift
Retry-After: 120
```

In the latter example, the delay is 2 minutes.

## Topics

### Large Record Sets
- [Retrieving a Large Record Set](retrieving-a-large-record-set.md)
  Efficiently work with large record sets.
### Managed Apple Accounts
- [Associating an Apple Account with a Volume Purchase Program (VPP) User](associating-an-apple-id-with-a-volume-purchase-program-vpp-user.md)
  Manage Apple Accounts within your organization effectively.
### VPP Account Protection
- [Protecting Your VPP Account](protecting-your-vpp-account.md)
  Ensure a Volume Purchase Program (VPP) account is not managed or reset by another product.

## See Also

- [Upgrading to Apple School Manager (ASM) and Apple Business Manager (ABM)](upgrading-to-apple-school-manager-asm-and-apple-business-manager-abm.md)
  Manage devices and content across an organization user base with a single destination.
- [Interpreting Error Codes](interpreting-error-codes.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-apps-and-books-through-web-services-legacy)*