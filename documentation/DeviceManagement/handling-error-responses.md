# Handling Error Responses

**Framework**: Device Management

Investigate service request errors and troubleshoot solutions.

#### Overview

When tasks for a service request result in a failure, you receive information about the failure either synchronously in the service response, or asynchronously in status endpoint responses or background notifications. The error information resides in the `ErrorResponse` objects. An [`ErrorResponse`](errorresponse.md) object contains two fields: an `errorNumber` field and an `errorMessage` field. In some cases, the `ErrorResponse` object also contains an `errorInfo` field with metadata about the failure for diagnostic purposes. Any `errorMessage` value uniquely maps to an `errorNumber` value, but not the other way around.

##### Handle Synchronous Error Responses

When a service request results in a synchronous failure, the response is itself an [`ErrorResponse`](errorresponse.md) object containing an `errorMessage` and `errorNumber`.

> ❗ **Important**:  Synchronous failures result in no asynchronous processing.

In addition to the response body, the HTTP status code provides information about the nature of the failure.

```javascript
{
    "errorNumber": 9726,
    "errorMessage": "This request contains an unsupported HTTP method for the requested endpoint."
}
```

##### Handle Retry After Headers

For HTTP 5xx server error responses, a `Retry-After` header indicates how long the client must wait before making additional requests.

The header for a 2-minute wait resembles the following:

```javascript
Retry-After: 120
```

If notifications for an event are missing, use [`Event Status`](events-status.md) to verify that the event’s state is not pending. Then trigger a sync with either [`Get Assets`](get-assets-44p83.md) or [`Get Users`](get-users-5boi1.md) to sync the changes since the request.

##### Handle Error Responses in Status

If a task for a submitted service request fails while processing in the background, the status endpoint for that task provides information about the failure. The status endpoint includes a `failures` field with a value that is an array of `ErrorResponse` objects.

```javascript
{
    "eventStatus": "FAILED",
    "eventType": "ASSOCIATE",
    "failures": [
        {
            "errorInfo": {
                "clientUserIds": [
                    "user102",
                    "user101"
                ]
            },
            "errorNumber": 9609,
            "errorMessage": "Unable to find registered user."
        }
    ],
    "numCompleted": 0,
    "numRequested": 2,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

##### Handle Error Responses in Notifications

If a task for a submitted service request fails while processing in the background, and if the MDM client that submits the request can receive notifications, the notification contains an [`ErrorResponse`](errorresponse.md) object with information about the failure and affected entities. A notification can have at most one `ErrorResponse` object in it (potentially affecting multiple entities).

```javascript
{
    "notification": {
        "assignments": [
            {
                "adamId": "1234",
                "pricingParam": "STDQ",
                "serialNumber": "device1"
            },
            {
                "adamId": "1234",
                "pricingParam": "STDQ",
                "clientUserId": "user1"
            }
        ],
        "error": {
            "errorMessage": "There aren't enough assets available to complete this association.",
            "errorNumber": 9709
        },
        "eventId": "f743928c-cc93-4a17-a53f-50c552ce1e06",
        "result": "FAILURE",
        "type": "ASSOCIATE"
    },
    "notificationId": "eba66-1bc1-4285-aa0a-7256293c5ca7",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

Error Codes for Synchronous Failures

| Error number | Error message | HTTP status code |
| --- | --- | --- |
| 9601 | Login required. | 401 |
| 9602 | Invalid argument. | 400 |
| 9603 | Internal error. | 500 |
| 9609 | Unable to find the registered user. | 400 |
| 9621 | The token has expired. You need to generate a new token online using your organization’s account at either `school.apple.com` or `business.apple.com`. | 401 |
| 9625 | The server has revoked the `cToken`. | 401 |
| 9634 | This service is no longer available. | 410 |
| 9646 | There are too many requests for the current Organization and the request has been rejected, either due to high server volume or an MDM issue. Use an incremental/exponential backoff strategy to retry the request until successful. | 429 |
| 9650 | The provided page index must be greater than `0`, and less than the total number of pages. | 400 |
| 9700 | This request exceeds the maximum `assets` limit. Change the request to stay within the specified limit. | 400 |
| 9701 | This request exceeds the maximum `clientUserIds` limit. Change the request to stay within the specified limit. | 400 |
| 9702 | This request exceeds the maximum `serialNumbers` limit. Change the request to stay within the specified limit. | 400 |
| 9703 | This request contains duplicate `assets`. Change the request to send unique assets. | 400 |
| 9704 | This request contains duplicate `clientUserIds`. Change the request to send unique client IDs. | 400 |
| 9705 | This request contains duplicate `serialNumbers`. Change the request to send unique serial numbers. | 400 |
| 9706 | The asset in the request isn’t revocable. Change the request to send revocable assets. | 400 |
| 9707 | The asset in the request isn’t device-assignable. Change the request to send device-assignable assets. | 400 |
| 9708 | Unable to find `eventId`. | 400 |
| 9710 | Both the notification URL and the authentication token are necessary. | 400 |
| 9711 | Either the notification URL or the authentication token exceeds its maximum length. Change the request to stay within the specified limit. | 400 |
| 9712 | The provided notification URL must be a valid URL and use HTTPS as the protocol. | 400 |
| 9713 | The MDM metadata exceeds the maximum length. Change the request to stay within the specified limit. | 400 |
| 9714 | The number of users exceeds the maximum. Change the request to stay within the specified limit. | 400 |
| 9715 | This request contains duplicate users. Change the request to send unique users. | 400 |
| 9717 | This request contains an invalid email address. Change the request to send valid email addresses. | 400 |
| 9718 | This request doesn’t contain an asset, which is a required argument. Change the request to provide an asset. | 400 |
| 9719 | Either `clientUserIds` or `serialNumbers` are required arguments. Change the request to provide assignable users and devices. | 400 |
| 9720 | Users are a required argument. Change the request to provide a user. | 400 |
| 9721 | This request contains an invalid version ID. Change the request to send the version ID from the read APIs. | 400 |
| 9722 | This request contains an invalid authorization header. Change the request to send an authorization header that matches the format `'Bearer {cToken}'`. | 401 |
| 9723 | You must provide an MDM name, ID, and metadata when setting the MDM information. | 400 |
| 9724 | The MDM ID exceeds the maximum length. Change the request to stay within the specified limit. | 400 |
| 9725 | The MDM name exceeds the maximum length. Change the request to stay within the specified limit. | 400 |
| 9726 | This request contains an unsupported HTTP method for the requested endpoint. | 405 |
| 9727 | This request contains an unsupported `Content-Type` for the requested endpoint. | 415 |
| 9728 | The provided notification URL is unreachable. | 400 |

Error Codes for Asynchronous Failures

The server may return these error codes in either [`StatusResponse`](statusresponse.md) or in background notifications.

| Error number | Error message |
| --- | --- |
| 9603 | Internal error. |
| 9609 | Unable to find registered user. |
| 9709 | There aren’t enough assets available to complete this association. |
| 9716 | A registered user already exists with the specified `clientUserId`. |

> ❗ **Important**:  The server may add additional error codes in the future.

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
  Associate app and book purchases with users or devices.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/handling-error-responses)*