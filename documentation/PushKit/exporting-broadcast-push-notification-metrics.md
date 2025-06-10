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

Substitute these values:

Supply your data export token in the `X-Apple-CloudKit-Management-Token` header, and provide a JSON object in the body which contains these keys:

For channel metrics requests, you also need to include a `channelId` key, with a value that’s the base64-encoded bytes, that identifies the channel.

On success, the server responds with a JSON object that contains these fields:

The data export request endpoint might return the following HTTP status codes that represent errors:

You can request a download that covers the same date range as a previous download. If you make a repeat request within 24 hours, the server returns the same status URL as the original request. If you make a repeat request after 24 hours, the server creates a new request with a new status URL, and any events within the requested time range logged after the original request is made are in the new report.

> **Note**:  The status URLs for all requests are available for 6 months after you make the request. Use the latest URLs for checking status and downloading reports.

Make an HTTPS `GET` request to the status URL, passing your data export token in the `X-Apple-CloudKit-Management-Token` header. The server responds with a JSON object that contains these fields:

The data export status endpoint might return the following HTTP status codes that represent errors:

#### Download the Exported Data

Make an HTTPS GET request to URL in the status object’s `downloadDetails.dataUrl` field to receive a CSV file that contains your exported data:

curl –compressed -X GET “https://example.com/download/data.csv” -o export.csv

The CSV file contains these fields:

Apple servers retain the exported data for six months. To re-download the data, make another GET request to the status URL and download the data from the new download URL.

## See Also

- [Exporting delivery metrics logs](exporting-delivery-metrics-logs.md)
  Download and analyze push-notification metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/exporting-broadcast-push-notification-metrics)*