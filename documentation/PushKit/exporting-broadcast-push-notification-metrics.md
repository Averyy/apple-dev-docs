# Exporting broadcast push notification metrics

**Framework**: PushKit

Discover how many people subscribe to your broadcast channels, and how many messages they receive.

#### Overview

Use the CloudKit Console to export Apple Push Notification service (APNs) broadcast notification metrics for your application and channels. To download the broadcast push notification metrics report, create a data export token, request data from iCloud Web Services, and download the results when the request completes. For more information about CloudKit and CloudKit Console, see [`Build apps using CloudKit`](https://developer.apple.comhttps://developer.apple.com/icloud/cloudkit/).

> **Note**:  If you have questions about the data made available in this API, including how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option: Developer Tools & Resources > CloudKit Console > Data Export [`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

#### Create a Data Export Token

To access log data for your apps, create a data export token by following these steps:

1. Navigate to [`CloudKit Console settings`](https://developer.apple.comhttps://icloud.developer.apple.com/dashboard/notifications/teams?settings=account) and log in.
2. Click Tokens.
3. Click Create Data Export Token.
4. Give the token a name and an optional description.
5. Choose the bundle identifier of the app for which you want to download data.
6. Choose the appropriate dataset: - To download data aggregated across all channels for your app, choose Broadcast Push Notification Application Metrics.
- To download data for a specific channel for your app, choose Broadcast Push Notification Channel Metrics.
7. Set an expiration date for the token, up to a maximum of six months in the future.
8. Click Create Data Export Token.
9. Securely store the token that you created in step 8.

> **Note**:  If you navigate back to the CloudKit console later, you cannot see the data export token value.

The token you create is restricted to your developer account, and only gives you access to the APNs dataset for the specified app.

#### Create a Data Export Request

Make an HTTPS `POST` request to the appropriate data export request endpoint:

- **Application metrics**: Use `https://api.icloud.apple.com/v1/dataExports/apns/teams/{teamId}/appId/{appId}/datasetName/broadcastapplicationmetric/request`
- **Channel metrics**: Use `https://api.icloud.apple.com/v1/dataExports/apns/teams/{teamId}/appId/{appId}/datasetName/broadcastchannelmetrics/request`

Substitute these values:

- **`{teamId}`**: Your Apple Developer team identifier
- **`{appId}`**: Your app’s bundle identifier

Supply your data export token in the `X-Apple-CloudKit-Management-Token` header, and provide a JSON object in the body which contains these keys:

- **`startDate`**: The earliest date for which to include data, in the format `yyyy-MM-dd`, at most 30 days in the past.
- **`endDate`**: The latest date for which to include data, in the format `yyyy-MM-dd`. This date must be later than `startDate`, and at least one day in the past.
- **`dataDownloadUrlExpiresInMinutes`**: The number of minutes after you receive the download for which the download URL needs to remain valid, between `20` and `60`.

For channel metrics requests, you also need to include a `channelId` key, with a value that’s the base64-encoded bytes, that identifies the channel.

On success, the server responds with a JSON object that contains these fields:

- **`statusUrl`**: A URL you use to check the status of your request.
- **`requestedAt`**: The time at which you requested the data export, in ISO8601 format.

**Example request**:

```None
curl -X POST \
-H "Content-Type: application/json" \
-H "X-Apple-CloudKit-Management-Token: {data-export-token}" \
-d \
'{
    "startDate": "2024-11-03",
    "endDate": "2024-11-10",
    "dataDownloadUrlExpiresInMinutes": 60,
    "channelId": "dHN0LXNyY2gtY2hubA==",
}' \
https://api.icloud.apple.com/v1/dataExports/apns/teams/{teamId}/appId/{appId}/datasetName/broadcastchannelmetrics/request 
```

**Response**:

```None
{
    "statusUrl": "https://example.com/statusURL",
    "requestedAt": "2024-11-11 18:01:00Z"
}
```

The data export request endpoint might return the following HTTP status codes that represent errors:

- **`400`**: The request is badly formed.
- **`401`**: The data export token is invalid.
- **`404`**: The channel identifier isn’t found.
- **`500`**: An internal error occurred.

You can request a download that covers the same date range as a previous download. If you make a repeat request within 24 hours, the server returns the same status URL as the original request. If you make a repeat request after 24 hours, the server creates a new request with a new status URL, and any events within the requested time range logged after the original request is made are in the new report.

> **Note**:  The status URLs for all requests are available for 6 months after you make the request. Use the latest URLs for checking status and downloading reports.

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
- **`401`**: The data export token is invalid.
- **`500`**: An internal error occurred.

#### Download the Exported Data

Make an HTTPS GET request to URL in the status object’s `downloadDetails.dataUrl` field to receive a CSV file that contains your exported data:

curl –compressed -X GET “https://example.com/download/data.csv” -o export.csv

The CSV file contains these fields:

- **`Date (UTC)`**: The date at which APNs reported the metrics.
- **`Broadcasts Published`**: An integer that’s the number of broadcast push notifications published to APNs. For channels that don’t have enough subscribers to deanonymize people, the value is `-1` instead.
- **`Broadcasts Delivered`**: An integer that’s the number of broadcast push notifications delivered to devices from APNs. For channels that don’t have enough subscribers to deanonymize people, the value is `-1` instead.
- **`Total Subscriptions`**: An integer that’s a snapshot count of devices subscribed. APNs records subscription snapshots throughout the day and reports the highest value for each day. For channels that don’t have enough subscribers to deanonymize people, the value is `-1` instead.
- **`Unique Subscribers`**: An integer that’s a snapshot count of unique devices subscribed to any channel for your app. APNs records subscription snapshots throughout the day and reports the highest value for each day. This value is only included in the application metrics report.

Apple servers retain the exported data for six months. To re-download the data, make another GET request to the status URL and download the data from the new download URL.

## See Also

- [Exporting delivery metrics logs](exporting-delivery-metrics-logs.md)
  Download and analyze push-notification metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/exporting-broadcast-push-notification-metrics)*