# Exporting file provider metrics data

**Framework**: File Provider

Download and analyze usage, consistency, and error data.

#### Overview

Use CloudKit Console to create a data export token that you use to export file provider metrics for your apps. Request data from iCloud web services, and download the data when the request is complete. For more information on CloudKit and CloudKit Console, see [`Build apps using CloudKit`](https://developer.apple.comhttps://developer.apple.com/icloud/cloudkit/).

You can download three different reports that provide file provider metrics:

> **Note**:  If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option: Developer Tools & Resources > CloudKit Console > Data Export [`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

 If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option:

Developer Tools & Resources > CloudKit Console > Data Export

[`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

##### Create a Data Export Token

To access log data for your apps, create a data export token by following these steps:

1. Navigate to [`CloudKit Console settings`](https://developer.apple.comhttps://icloud.developer.apple.com/dashboard/notifications/teams?settings=account) and log in.
2. Click Tokens.
3. Click Create Data Export Token.
4. Give the token a name, and an optional description.
5. Choose the bundle identifier for the app for which you want to download data.
6. Choose the data set you want to download.
7. Set an expiration date for the token, up to a maximum of 6 months in the future.
8. Click Create Data Export Token.
9. Securely store the token you create in step 8.

> **Note**:  If you navigate back to the CloudKit Console later, you can’t see the data export token’s value again.

 If you navigate back to the CloudKit Console later, you can’t see the data export token’s value again.

The token you create is restricted to your developer account, and only gives you access to the data set you requested for the specified app.

##### Create a Data Export Request

Make an HTTPS `POST` request to the data export request endpoint:

- `https://api.icloud.apple.com/v1/dataExports/fpfs/teams/{teamId}/appId/{appId}/datasetName/{dataset}/request`

Substitute these values:

Supply your data export token in the `X-Apple-CloudKit-Management-Token` header, and provide a JSON object in the body with these fields:

The server responds with a JSON object that contains these fields:

```shell
% curl -X POST \
-H "Content-Type: application/json" \
-H "X-Apple-CloudKit-Management-Token: {data-export-token}" \
-d \
'{
"startDate": "2024-01-01",
"endDate": "2024-01-26",
"dataDownloadUrlExpiresInMinutes": 60
}' https://api.icloud.apple.com/v1/dataExports/fpfs/teams/{teamId}/appId/{appId}/datasetName/{dataset}/request 

{
"statusUrl": "https://example.com/statusURL",
"requestedAt": "2024-02-14T18:32:30.947451Z"
}
```

The data export request endpoint might return the following HTTP status codes that represent errors:

You can request a download that covers the same date range as a previous download. If you make a repeat request within 24 hours, the server returns the same status URL as the original request.  If you make a repeat request after 24 hours, the server creates a new request with a new status URL, and any events within the requested time range that are logged after the original request was made are included in the new report.

> **Note**:  The status URLs for all requests are available for 6 months after you make the request. Make sure you use the latest URLs for checking status and downloading reports.

 The status URLs for all requests are available for 6 months after you make the request. Make sure you use the latest URLs for checking status and downloading reports.

##### Check the Status of Your Data Export

Make an HTTPS `GET` request to the status URL, passing your data export token in the `X-Apple-CloudKit-Management-Token` header.

The server responds with a JSON object that contains these fields:

Apple servers retain the exported data for 6 months. To re-download the data, make another `GET` request to the status URL and download the data from the new download URL.

```shell
% curl -X GET -H "X-Apple-CloudKit-Management-Token: {data-export-token}" https://example.com/statusURL
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

##### Download the Exported Data

Make an HTTPS `GET` request to URL in the status object’s `downloadDetails.dataUrl` field to receive a CSV file that contains your exported data:

```shell
curl --compressed -X GET "https://example.com/download/data.csv" -o export.csv
```

##### Analyze the Csv File

The CSV file for all types of report contains these common fields:

##### Understand Usage Report Fields

The usage report contains these fields:

##### Understand Dynamic Error Fields

The dynamic errors report contains these fields:

##### Understand Consistency Report Fields

The consistency report contains these fields:

Additionally, the consistency report includes a randomly chosen instance of an error that the consistency checker encountered. It contains the following fields:

##### Understand the Character Set Bit Masks

The bits in the `name_characters_sets` bitfield are set to `1` when the following conditions are true, with bit `0` being the least significant bit:

##### Understand the Disconnection States

The `disconnection_state` field in the usage report enumerates the reason that file provider is disconnected. The possible values are:

##### Understand the Transfer Operation Types and Operation Reasons

The `db_transfer_operation_type` field in the consistency report’s erroneous item breakdown enumerates the operation type that encountered an error. The possible values are:

The `reason` field in usage reports is a bitfield that enumerates the reasons the system performed the reported operation. The meaning of each bit in the bitfield, where bit `0` is the least-significant bit and bit `36` is the most-significant bit, are:


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/exporting-file-provider-metrics-data)*