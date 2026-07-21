# Upgrading to the new management API

**Framework**: Device Management

Migrate from API version 1 to version 2 for improved performance.

#### Overview

New features and improved asynchronous processing in App, Book, and Subscription Management API 2 enable device management services to manage apps, books, and subscriptions in a faster and more scalable way than ever before. To take advantage of these new features, you need to change the way in which you manage apps, books, and subscriptions.

For more information, see [`Getting started with the management API`](getting-started-with-the-management-api.md). For an overview of what’s new in version 2, watch the WWDC21 presentation [`Improve MDM assignment of Apps and Books`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10137).

#### Review Endpoint Changes

The following table shows the differences between the API 1 and API 2 endpoints. For more information about specific API protocols and usage, see [`App, Book, and Subscription Management`](app-book-and-subscription-management.md).

| Version 1 | HTTP method | Version 2 | HTTP method |
| --- | --- | --- | --- |
| `editVPPUserSrv` | `POST` | `users/update` | `POST` |
| `getAssignments` | `POST` | `assignments` | `GET` |
| `getVPPAssetsSrv` | `POST` | `assets` | `GET` |
| `getVPPLicensesSrv` | `POST` |  |  |
| `getVPPUsersSrv` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `getVPPUserSrv` | `POST` | `users` | `GET` |
| `manageVPPLicensesByAdamIdSrv` | `POST` | `assets/associate` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `assets/disassociate` | `POST` |
| `registerVPPUserSrv` | `POST` | `users/create` | `POST` |
| `retireVPPUserSrv` | `POST` | `users/retire` | `POST` |
| `VPPClientConfigSrv` | `POST` | `client/config` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `client/config` | `POST` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `GET` |
| `VPPServiceConfigSrv` | `POST` | `service/config` | `GET` |
|  |  | `status` | `GET` |
|  |  | `assets/revoke` | `POST` |
|  |  | `subscriptions` | `GET` |
|  |  | `subscriptions/assignments` | `GET` |
|  |  | `subscriptions/associate` | `POST` |
|  |  | `subscriptions/disassociate` | `POST` |
|  |  | `subscriptions/admins` | `GET` |
|  |  | `subscriptions/admins/add` | `POST` |
|  |  | `subscriptions/admins/remove` | `POST` |

#### Track Assignments

Assignment tracking in version 2 is very similar to that in version 1; however, version 2 no longer supports the use of license IDs. To simplify the management process, version 2 deprecates the `getVPPLicensesSrv` endpoint. This means that you can no longer use Apple-assigned IDs to identify their license assignments.

To properly identify an assignment through [`Get Assignments`](get-assignments-9wv1e.md), version 2 uses the combination of `adamId` and `clientUserId` for user-based assignments, or `adamId` and `serialNumber` for device-based assignments. You can also use the `adamId` alone to retrieve all assignments for that `adamId`.

#### Use Pagination

In version 1, results batch through a `batchToken` if the total number of records exceeds the limit results. With batches, the initial request occurs with no `batchToken`. The response includes `batchToken` with the first batch of records if the number of records exceeds a server-controlled limit. To get the next batch of records, you need to include the batch token in the subsequent requests. [`Using paginated endpoints`](using-paginated-endpoints.md) is version 2’s solution to work with larger result sets more efficiently.

In the new API, when the number of records in a response exceeds a server-controlled limit, the server paginates the response. Endpoints that support pagination, such as [`Get Assets`](get-assets-4ski1.md) and [`Get Users`](get-users-4mwln.md), can accept a page index query parameter. Using the page index, you can access a response page directly; you don’t need to access pages sequentially. Additionally, to reduce the time it takes to retrieve the full set, you can make multiple paginated requests in parallel.

The subscription endpoints use cursor-based pagination instead. Pass the `nextCursor` value from each response as the `cursor` parameter in the next request.

#### Batch Requests

In version 1, all asset management calls occur synchronously. It’s your responsibility to batch large requests and send them in parallel to Apple. This results in sending many small simultaneous requests to Apple, which sometimes leads to resource contention and failed requests. With version 2, you can send a single, much larger request and rely on Apple to batch the request and process it asynchronously, enforcing parallelism on the server. This results in processing optimization, which fulfills large requests more quickly and more reliably.

To take advantage of batching, you can discontinue the use of small, parallel management requests and, instead, group similar [`Associate Assets`](associate-assets.md) and [`Disassociate Assets`](disassociate-assets.md) tasks into a single, larger request. You can perform thousands of assignments or unassignments in a single request. The [`Service Config`](service-config.md) response specifies the maximum number of `adamIds`, `clientUserIds,` and `serialNumbers` the version 2 management requests accept.

#### Subscribe to Notifications

[`Subscribing to notifications`](subscribing-to-notifications.md) in version 2 provides a huge improvement to the tracking of the latest events for device management services. You no longer require fetching on assignment endpoints to confirm the results of management requests. You can configure a notification host and notifications are sent to your device management service upon the completion of asset and user-management requests.

In addition to receiving notifications for events initiated by your device management service, you may also receive a notification for user-initiated events, such as asset purchases and transfers.

The subscription endpoints introduce additional notification types. Subscribe to `SUBSCRIPTION_MANAGEMENT` and `SUBSCRIPTION_COUNT` — along with the existing `ASSET_MANAGEMENT`, `ASSET_COUNT`, `USER_MANAGEMENT`, and `USER_ASSOCIATED` types — to receive notifications for all content types.

For information about subscribing to different notification types, see [`ClientConfigRequest`](clientconfigrequest.md).

#### Set Information About the Device Management Service

In version 2, when creating a [`ClientConfigRequest`](clientconfigrequest.md), you can include [`MdmInfo`](mdminfo.md) in the request. The server returns this information on all subsequent responses to identify which device management service is managing the location. It’s important to interrogate the `MdmInfo` content API responses to ensure no other device management service is attempting to manage the data in this location.

Within `MdmInfo`, you have the opportunity to include `metadata`, a free-form field to store additional information for the organization.

> **Note**:  In version 2, `metadata` replaces `clientContext` from version 1. It’s advisable to include informative plain text descriptors, particularly in the `name` field, to help identify the device management service in the case of any discrepancies. After a device management service uses version 2, the system automatically updates the `clientContext` in version 1 for that location to display “token being used in v2”.

#### Perform Occasional Syncs

Notifications remove the necessity to continually sync with Apple for asset and user counts, which occurs frequently in version 1. However, it’s a best practice to occasionally sync your data using [`Get Assets`](get-assets-4ski1.md), [`Get Users`](get-users-4mwln.md), or [`Get Assignments`](get-assignments-9wv1e.md) to avoid missing notifications, especially when a device management service doesn’t initiate a request.

#### Sanitize Device Management Information

To maintain device management hygiene, update the `mdmInfo` field using the [`Client Config`](client-config-4szk1.md) endpoint to reflect any changes. Prior to releasing a location, remove any assets assigned to a location through transferring. If a device management service fails to receive notifications, it’s preferable to sanitize the `notificationUrl` field and reset it to a reachable URL.

## See Also

- [App and book management (Legacy)](app-and-book-management-legacy.md)
  Manage apps and books for your students and employees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/upgrading-to-the-new-management-api)*