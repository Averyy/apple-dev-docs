# Exporting delivery metrics logs

**Framework**: PushKit

Download and analyze push-notification metrics.

#### Overview

Use the CloudKit Console to export Apple Push Notification service (APNs) delivery metrics logs for your apps. To download the push notification metrics report, create a data export token, request data from iCloud Web Services, and download the results when the request completes. For more information about CloudKit and CloudKit Console, see [`Build apps using CloudKit`](https://developer.apple.comhttps://developer.apple.com/icloud/cloudkit/).

The push-notification metrics report includes aggregated, rounded metrics on notification states as your notifications pass through APNs. It shows multiple notification statuses, such as `delivered`, `stored`, and `discarded`. It also provides insights into various statistics for notifications, including a detailed breakdown based on push type.

> **Note**:  If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option: Developer Tools & Resources > CloudKit Console > Data Export [`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

#### Create a Data Export Token

To access log data for your apps, create a data export token by following these steps:

1. Navigate to [`CloudKit Console settings`](https://developer.apple.comhttps://icloud.developer.apple.com/dashboard/notifications/teams?settings=account) and log in.
2. Click Tokens.
3. Click Create Data Export Token.
4. Give the token a name and an optional description.
5. Choose the bundle identifier for the app for which you want to download data.
6. Choose the Delivery Metrics dataset.
7. Set an expiration date for the token, up to a maximum of six months in the future.
8. Click Create Data Export Token.
9. Securely store the token that you created in step 8.

> **Note**:  If you navigate back to the CloudKit console later, you won’t be able to see the data export token’s value again.

The token you create is restricted to your developer account, and only gives you access to the APNs data set for the specified app.

#### Create a Data Export Request

Make an HTTPS `POST` request to the data export request endpoint at:

- `https://api.icloud.apple.com/v1/dataExports/apns/teams/{teamId}/appId/{appId}/datasetName/deliverymetrics/request`

Substitute these values:

- **`{teamId}`**: Your Apple Developer team identifier.
- **`{appId}`**: Your app’s bundle identifier.

Supply your data export token in the `X-Apple-CloudKit-Management-Token` header, and provide a JSON object in the body with these fields:

- **`startDate`**: The earliest date for which to include data, in the format `yyyy-MM-dd`, at most 30 days in the past.
- **`endDate`**: The latest date for which to include data, in the format `yyyy-MM-dd`. This date must be later than `startDate`, and at least one day in the past.
- **`dataDownloadUrlExpiresInMinutes`**: The number of minutes after you receive the download for which the download URL needs to remain valid, between `20` and `60`.

The server responds with a JSON object that contains these fields:

- **`statusUrl`**: A URL you use to check the status of your request.
- **`requestedAt`**: The time at which you requested the data export, in ISO8601 format.

**Example request**:

```None
curl -X POST \
-H "Content-Type: application/json" \
-H "X-Apple-CloudKit-Management-Token: {data-export-token}" \
-d \
'{
    "startDate": "2024-01-01",
    "endDate": "2024-01-26",
    "dataDownloadUrlExpiresInMinutes": 60
}' \
https://api.icloud.apple.com/v1/dataExports/apns/teams/{teamId}/appId/{appId}/datasetName/deliverymetrics/request 
```

**Response**:

```None
{
    "statusUrl": "https://example.com/statusURL",
    "requestedAt": "2024-01-28 10:01:00Z"
}
```

The data export request endpoint might return the following HTTP status codes that represent errors:

- **`400`**: The request is badly formed.
- **`401`**: The data export token is invalid.
- **`500`**: An internal error occurred.

You can request a download that covers the same date range as a previous download. If you make a repeat request within 24 hours, the server returns the same status URL as the original request. If you make a repeat request after 24 hours, the server creates a new request with a new status URL, and any events within the requested time range that are logged after the original request was made are included in the new report.

> **Note**:  The status URLs for all requests are available for 6 months after you make the request. Make sure you use the latest URLs for checking status and downloading reports.

#### Check the Status of Your Data Export

Make an HTTPS `GET` request to the status URL, passing your data export token in the `X-Apple-CloudKit-Management-Token` header. The server responds with a JSON object that contains these fields:

- **`status`**: One of `PROCESSING`, `FAILED`, `EXPIRED`, or `SUCCESS`.
- **`requestedAt`**: The time at which you requested the data export, in ISO8601 format.
- **`downloadDetails`**: If the status is `PROCESSING`, `EXPIRED`, or `FAILED`, this key isn’t set. If the status is `SUCCESS`, it’s a JSON object that contains these fields: - **`dataURL`**: The URL you use to get the exported data.
- **`expiresAt`**: The time at which the data URL expires.

**Example Request**:

```None
curl -X GET -H "X-Apple-CloudKit-Management-Token: {data-export-token}" \
https://example.com/statusURL
```

**Response**:

```None
{
    "requestedAt": "2024-02-14T18:32:30.947Z",
    "status": "SUCCESS",
    "downloadDetails": {
        "dataUrl": "https://example.com/download/data.csv",
        "expiresAt": "2024-02-14T18:53:14.762922Z"
    }
}
```

The data export status endpoint might return the following HTTP status codes that represent errors:

- **`400`**: The request is badly formed.
- **`404`**: The data export token is invalid.
- **`500`**: An internal error occurred.

#### Download the Exported Data

Make an HTTPS `GET` request to URL in the status object’s `downloadDetails.dataUrl` field to receive a CSV file that contains your exported data:

```None
curl --compressed -X GET "https://example.com/download/data.csv" -o export.csv
```

The CSV file contains these fields:

- **Push Type**: A string that identifies the type of your push notification’s payload.
- **Status**: A string that identifies the current state of the push notifications.
- **Date (UTC)**: The date at which APNs reported the metrics.
- **Count**: An integer that counts the total number of push notifications of this type in this state.

Apple’s servers retain the exported data for six months. To re-download the data, make another `GET` request to the status URL and download the data from the new download URL.

## See Also

- [Exporting broadcast push notification metrics](exporting-broadcast-push-notification-metrics.md)
  Discover how many people subscribe to your broadcast channels, and how many messages they receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/exporting-delivery-metrics-logs)*