# Getting started with the management API

**Framework**: Device Management

Configure your device management service to handle content and user assignments.

#### Overview

Content managers use Apple School Manager and Apple Business to purchase apps, books, and subscriptions for their organization. Your device management service then assigns these assets to users and devices. If a user no longer needs an app or subscription, your device management service can reclaim it and reassign it to a different user. You can also assign an app directly to a device’s serial number, so an Apple Account isn’t necessary to download the app. Books and subscriptions aren’t device-assignable, and books can’t be reassigned among users.

#### Authenticate

All server endpoints except [`Service Config`](service-config.md) require a content token (`sToken`) to authenticate an organization. A valid `sToken` allows a device management service to manage assets for the specified organizational unit of an organization. Only one device management service should manage a single organizational unit at any time. Multiple device management services managing the same organizational unit result in unpredictable asset allocation.

Content managers can download an `sToken` for an organizational unit from the Apps and Books section under the Settings tab in Apple School Manager or Apple Business, and upload it into their device management service.

![The Apps and Books settings section in Apple School Manager and Apple Business for downloading content tokens.](/images/com.apple.devicemanagement/getting-started-with-the-management-api.png)

The device management service stores the organizational unit’s content token along with its other private, protected properties, and passes this token in the `Authorization` header of API requests.

The `sToken` is a JSON string in Base64 encoding. When the server decodes it, the resulting JSON string contains three fields: `token`, `expDate`, and `orgName`.

| Field | Description |
| --- | --- |
| `token` | A unique identifier for the organizational unit under management. |
| `expDate` | The expiration date of the token in ISO-8601 format. |
| `orgName` | The name of the organization for the issued token. |

The following is an example `sToken` value:

```javascript

ewogICAgInRva2VuIjogIlZGZHdRbVZWTVZSUldGSktVbGRTTlZkc1pHcGpNR3hIVTI1Q2FrMXRhRzlhUjJ3eldqRkdkVk50ZUd0VFJrWjZVMVZhVDJGSFRuUlNiVGxOVVRCS1ExcEdhRTlOUjBaWVRrUXdQUT09IiwKICAgICJleHBEYXRlIjogIjIwMzAtMTEtMDhUMjI6MzM6MjIrMDAwMCIsCiAgICAib3JnTmFtZSI6ICJPUkcxMjM0NSIKfQ==

```

This is the JSON result after Base64 decoding:

```json
{
    "token": "VFdwQmVVMVRRWFJKUldSNVdsZGpjMGxHU25Cak1taG9aR2wzWjFGdVNteGtTRkZ6U1VaT2FHTnRSbTlNUTBKQ1pGaE9NR0ZYTkQwPQ==",
    "expDate": "2030-11-08T22:33:22+0000",
    "orgName": "ORG12345"
}
```

If the token expires within 15 days, the response contains an additional field, `tokenExpirationDate`. The value of this field is the expiration date in ISO-8601 format, such as the following:

```json
{
    ...
    "tokenExpirationDate": "2030-11-08T22:33:22+0000"
}
```

#### Handle Permissions

Organization administrators can tailor different sets of privileges for an individual content manager’s `sToken` using Managed Apple Accounts, which allows a fine level of control over what those users can do. For example, a content manager with read-only privileges can use the [`Get Assets`](get-assets-4ski1.md), [`Get Assignments`](get-assignments-9wv1e.md), and [`Get Users`](get-users-4mwln.md) endpoints, but can’t use the [`User management`](app-book-and-subscription-management#User-management.md) or [`Asset management`](app-book-and-subscription-management#Asset-management.md) endpoints. Administrators can also assign content managers the Can Purchase and the Can Manage privileges, so that an individual content manager can manage assets, but not buy them.

#### Identify the Current Device Management Service

To protect against another device management service managing the same organizational unit, be sure to set [`MdmInfo`](mdminfo.md) in [`Client Config`](client-config-4szk1.md). Then inspect `MdmInfo` each time a response returns to ensure that no other device management service overwrites it.

`MdmInfo` resembles the following:

```json
{
    "mdmInfo": {
        "id": "522d5c43-44ca-4f7e-ba7a-53570cf60765", //Unique identifier.
        "name": "Apple Configurator 2", //MDM client name.
        "metadata": "2.13.3" //Freeform metadata field.
    },
    ...
}
```

#### Import Users

After authenticating, perform an initial import of the organizational unit’s active users. Send a request to [`Get Users`](get-users-4mwln.md) with `includeRetired=0`, then record the user data for each element of `users` in the [`GetUsersResponse`](getusersresponse.md). If the response includes a `nextPageIndex`, send another request with that value as the `pageIndex` query parameter and record the new page of users. Continue paging until `currentPageIndex` equals `totalPages`.

For more information about managing users after importing them, see [`User management`](app-book-and-subscription-management#User-management.md).

##### Sync Users After Import

Keep the imported user list up to date by passing the `versionId` from each response as the `sinceVersionId` query parameter in subsequent requests. Subsequent responses contain only users modified since that version. For more information about versioned queries and page-index pagination, see [`Using paginated endpoints`](using-paginated-endpoints.md).

#### Import Assigned Assets

Import asset counts first, then import the current assignments for each asset. Send a request to [`Get Assets`](get-assets-4ski1.md) to retrieve counts by `adamId` for the managed organizational unit. For each `adamId` in the [`GetAssetsResponse`](getassetsresponse.md), send a request to [`Get Assignments`](get-assignments-9wv1e.md) and record the `adamId`, `pricingParam`, and `clientUserId` or `serialNumber` for each assignment in the [`GetAssignmentsResponse`](getassignmentsresponse.md), along with the `currentPageIndex` and `totalPages`. Page through the results by passing the `nextPageIndex` value as the `pageIndex` query parameter in subsequent requests until `currentPageIndex` equals `totalPages`.

For more information about managing assets after importing them, see [`Asset management`](app-book-and-subscription-management#Asset-management.md).

##### Sync Assets and Assignments After Import

Keep assignment data current by passing the `versionId` from each Get Assignments response as the `sinceVersionId` query parameter in later requests to retrieve only the assignments modified since that version. [`Get Assets`](get-assets-4ski1.md) returns a `versionId` in its response but doesn’t accept `sinceVersionId` as a filter. To reconcile asset counts, refetch the full asset list and compare the stored `versionId` to detect when the underlying data changed. For more information about versioned queries and page-index pagination, see [`Using paginated endpoints`](using-paginated-endpoints.md).

#### Import Subscriptions

To import an organizational unit’s subscriptions, send a request to [`Get Subscriptions`](get-subscriptions.md). Filter by `parentAdamId` or `adamId`, or omit both to retrieve all subscriptions. The response includes seat counts broken down by renewal state — each subscription reports how many seats are `renewing` (auto-renewing at the end of the billing period) and how many are `expiring` (not renewing).

This endpoint uses cursor-based pagination instead of page-index pagination. Pass the `nextCursor` value from each response as the `cursor` query parameter in the next request, and continue until `nextCursor` is absent.

To import per-user subscription assignments, send a request to [`Get Subscription Assignments`](get-subscription-assignments.md). Each assignment includes a `renewing` Boolean value that reflects the renewal state of the seat assigned to that user. This endpoint also uses cursor-based pagination.

For more information about managing subscriptions, see [`Managing subscriptions`](managing-subscriptions.md).

#### Reconcile Subscriptions After Import

The subscription endpoints don’t support `sinceVersionId`, so reconcile subscription data by refetching the full dataset on a schedule that matches your freshness requirements. Subscribe to `SUBSCRIPTION_COUNT` and `SUBSCRIPTION_MANAGEMENT` notifications for real-time updates between scheduled syncs. For more information about cursor-based pagination, see [`Using paginated endpoints`](using-paginated-endpoints.md).

## See Also

- [Apps and books metadata for organizations](apps-and-books-metadata-for-organizations.md)
  Get metadata for apps and books your organization owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getting-started-with-the-management-api)*