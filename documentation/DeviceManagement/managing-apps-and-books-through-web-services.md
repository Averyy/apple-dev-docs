# Managing Apps and Books Through Web Services

**Framework**: Device Management

Associate app and book purchases with users or devices.

#### Overview

Organizations use Apple School Manager and Apple Business Manager to purchase their apps and books, then assign them to users and devices through the use of an MDM client. If a user no longer needs an app, you can reclaim it and assign it to a different user. Similarly, you can assign an app to a device’s serial number so an Apple Account isn’t necessary to download an app. Books aren’t device-assignable so you can’t reassign them among users.

##### Authenticate

All server endpoints except [`Service Config`](service-config.md) require a content token (`cToken`) header to authenticate an organization. A valid `cToken` allows an MDM client to manage assets for the specified location of an organization. Only one MDM client should manage a single location at any time. Multiple MDM clients managing the same location result in unpredictable asset allocation.

Content managers can download a location-based `cToken` from the Apps and Books section under the Settings tab in Apple School Manager or Apple Business Manager, and upload it into their MDM client.

![The Apps and Books settings section in Apple School Manager and Apple Business Manager for downloading content tokens.](https://docs-assets.developer.apple.com/published/041893ffc57ed18a43ef0cac764049d1/media-3737907.png)

The MDM client stores the location-based content token along with its other private, protected properties, and passes this token in the `Authorization` header of API requests.

The `cToken` is a JSON string in `Base64` encoding. When the server decodes it, the resulting JSON string contains three fields: `token`, `expDate`, and `orgName`.

| Field | Description |
| --- | --- |
| `token` | A unique identifier for the organization’s location under management. |
| `expDate` | The expiration date of the token in ISO-8601 format. |
| `orgName` | The name of the organization for the issued token. |

The following is an example `cToken` value:

```javascript

ewogICAgInRva2VuIjogIlZGZHdRbVZWTVZSUldGSktVbGRTTlZkc1pHcGpNR3hIVTI1Q2FrMXRhRzlhUjJ3eldqRkdkVk50ZUd0VFJrWjZVMVZhVDJGSFRuUlNiVGxOVVRCS1ExcEdhRTlOUjBaWVRrUXdQUT09IiwKICAgICJleHBEYXRlIjogIjIwMzAtMTEtMDhUMjI6MzM6MjIrMDAwMCIsCiAgICAib3JnTmFtZSI6ICJPUkcxMjM0NSIKfQ==

```

This is the JSON result after `Base64` decoding:

```javascript
{
    "token": "VFdwQmVVMVRRWFJKUldSNVdsZGpjMGxHU25Cak1taG9aR2wzWjFGdVNteGtTRkZ6U1VaT2FHTnRSbTlNUTBKQ1pGaE9NR0ZYTkQwPQ==",
    "expDate": "2030-11-08T22:33:22+0000",
    "orgName": "ORG12345"
}
```

If the provided `token` is within the expiration warning period (currently, 15 days before the expiration date), the response contains an additional field, `tokenExpirationDate`. The value of this field is the expiration date in ISO-8601 format, such as the following:

```javascript
{
    ...
    "tokenExpirationDate": "2030-11-08T22:33:22+0000"
}
```

##### Handle Permissions

Organization administrators can tailor different sets of privileges for an individual content manager’s `cToken` using Managed Apple Accounts, which allows a fine level of control over what those users can do. For example, a content manager with read-only privileges can use the [`Get Assets`](get-assets-4ski1.md), [`Get Assignments`](get-assignments-9wv1e.md), and [`Get Users`](get-users-4mwln.md) endpoints, but can’t use the [`User Management`](app-and-book-management#User-Management.md) or [`Asset Management`](app-and-book-management#Asset-Management.md) endpoints. You can also assign content managers the Can Purchase and the Can Manage privileges, so that an individual content manager can manage assets, but not buy them.

##### Identify the Current Mdm Client

To protect against another MDM client managing the same location, be sure to set [`MdmInfo`](mdminfo.md) in [`Client Config`](client-config-4szk1.md). Then inspect `MdmInfo` each time a response returns to ensure that no other MDM client overwrites it.

`MdmInfo` resembles the following:

```javascript
{
    "mdmInfo": {
        "id": "522d5c43-44ca-4f7e-ba7a-53570cf60765", //Unique identifier.
        "name": "Apple Configurator 2", //MDM client name.
        "metadata": "2.13.3" //Freeform metadata field.
    },
    ...
}
```

##### Import Users

The recommended procedure to import a location’s users into an MDM client is to import all currently active users in the requested location as follows:

1. Send a request to [`Get Users`](get-users-4mwln.md) with `includeRetired=0`.
2. Record the user data for each element of `users` in the [`GetUsersResponse`](getusersresponse.md).
3. Send another request to [`Get Users`](get-users-4mwln.md) that includes the `nextPageIndex` value from step 1 as `pageIndex,` and record the values as step 2 describes.
4. Repeat steps 2 and 3 until `currentPageIndex` is equal to `totalPages` in the [`GetUsersResponse`](getusersresponse.md).

For more information about managing users after importing them, see [`User Management`](app-and-book-management#User-Management.md).

##### Import Assigned Assets

The recommended procedure to import a location’s assets into an MDM client is to import asset counts and then import the current assignments for each asset as follows:

1. Send a request to [`Get Assets`](get-assets-4ski1.md) for count by `adamId` in the requested location.
2. For each `adamId` in the [`GetAssetsResponse`](getassetsresponse.md) from step 1, send a request to [`Get Assignments`](get-assignments-9wv1e.md).
3. Record the `adamId`, `pricingParam`, and `clientUserId` or `serialNumber` for each assignment in the [`GetAssignmentsResponse`](getassignmentsresponse.md). Also, record the `currentPageIndex` and `totalPages`.
4. Send another request to [`Get Assignments`](get-assignments-9wv1e.md) that includes the `nextPageIndex` value from step 3 as `pageIndex`, and record the values as step 3 describes.
5. Repeat step 4 until `currentPageIndex` is equal to `totalPages` in the [`GetAssignmentsResponse`](getassignmentsresponse.md).

See [`Get Assets`](get-assets-4ski1.md) for more information about using the `sinceVersionId`. For more information about managing assets after importing them, [`Asset Management`](app-and-book-management#Asset-Management.md).

## See Also

- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
  Manage devices and content across your organization using the new API version.
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.
- [Managing Assets](managing-assets.md)
  Retrieve key information to effectively manage assets across an organization’s users and devices.
- [Managing Users](managing-users.md)
  Retrieve key information to effectively manage users across an organization.
- [Using Paginated Endpoints](using-paginated-endpoints.md)
  Manage paginated endpoints to efficiently work with large record sets.
- [Subscribing to Notifications](subscribing-to-notifications.md)
  Listen to notifications to keep track of the latest events for an organization.
- [Handling Error Responses](handling-error-responses.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-apps-and-books-through-web-services)*