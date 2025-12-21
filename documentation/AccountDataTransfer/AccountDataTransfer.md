# Account Data Transfer

**Framework**: Account Data Transfer  
**Kind**: module

Download App Store information, app install, and push notification activity on behalf of people who use your app.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

Use the Account Data Transfer web API to request and download information about the people who use your app. The data available relates to someone’s use of Apple’s App Store, including information such as previous transactions and downloads. It also contains information related to app install and push notification activity.

#### Understand Scopes

A scope identifies a subset of data that your apps and website can access from a single Apple Account, with approval from the individual whose data you request. Only select the applicable scopes for your apps and website.

##### User Information Scope

The developer portal selects the `data-transfer-user-profile` scope automatically when you request access to another scope.

##### App Store Information Scopes

> **Note**: If you’ve previously requested access to App Store information using the `appstore-user-profile` scope along with older scope names, the system accepts these scopes and automatically approves them for both EU and UK scopes. You don’t need to make a new token request.

##### App Install and Push Notification Activity Scopes

#### Request Permission for the Specific Scopes

To get permission for your App ID or Services ID to request App Store information and app install and push notification scopes for users in the EU, the UK, or Japan, follow the instructions at [`Request access to the Account Data Transfer API`](https://developer.apple.comhttps://developer.apple.com/contact/request/account-data-transfer-api/).

> **Note**:  This API returns account data about users in the EU, UK, and Japan. If you’re an app developer and need to transfer data related to App Store information, app install, or push notification activity for your app instead, use the [`App Data Transfer`](https://developer.apple.com/documentation/AppDataTransfer) API. If you request access to the Account Data Transfer API, and Apple grants your request, you don’t need to supply the `consent_mode` query parameter when you request an authorization token for the App Data Transfer API. If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option: Developer Tools & Resources > Account Data Transfer API > Data Request [`Learn more`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

##### Understand the Difference Between Scope Types

When making requests, it’s important to understand the scopes you can combine in a single request, and the scopes you need to request separately, as well as which are one-time requests and which can be either one-time or recurring requests. The following table describes the relationships between the available scopes:.

| Scope | Additional scopes you can add to the same request | Request frequency |
| --- | --- | --- |
| `app-install-activity-account-data-for-EU-users` | `appstore-info-account-data-for-EU-users` | One-time and recurring |
| `app-install-activity-account-data-for-UK-users` | `appstore-info-account-data-for-UK-users` | One-time and recurring |
| `appstore-info-account-data-for-EU-users` | `app-install-activity-account-data-for-EU-users` | One-time and recurring |
| `appstore-info-account-data-for-UK-users` | `app-install-activity-account-data-for-UK-users` | One-time and recurring |
| `appstore-info-account-data-for-JP-users` | `app-install-activity-account-data-for-JP-users` | One-time and recurring |
| `app-install-activity-account-data-for-JP-users` | `appstore-info-account-data-for-JP-users` | One-time and recurring |

#### Set Required Http Headers for the Requested Scopes

##### Set the Request Frequency

When making an HTTP `POST` request to the [`Submit request`](submit-request.md) endpoint, requesting the App Store or app install activity scope, you can request a one time or recurring request, depending on the specified scopes:

To make a one-time request, set the `mode` key to `ONE_TIME`. To make recurring requests, for app install or push notification activity, use one of the following values:

> **Note**: If you already have a recurring request pending and make another recurring request, the system returns an error, along with the ID of the existing request.

##### Save the Server Request Id and Check Delay Value

The Apple server returns a request ID, which you use when you get the request status, request download URLs, or cancel the request. For recurring requests, the Apple server returns a request ID, along with the parent ID that identifies the series of recurring requests.

The response from the server also contains a `statusCheckDelay`, which is the number of seconds you need to wait before checking the status of the request. You can cancel a request before this time by making a `POST` request to the [`Cancel request`](cancel-request.md) endpoint.

If you submit a `DAILY_30` recurring request and don’t resubmit the recurring instance each subsequent day, the recurring request expires 40 days after submission of the initial request.

If you submit a `WEEKLY_180` recurring request and don’t resubmit the recurring instance each subsequent week, the recurring request expires 190 days after submission of the initial request.

#### Find the Request Status

The data corresponding to the request you submitted isn’t available immediately. After the status-check delay expires, make a `GET` request to [`Get one-time request status`](get-one-time-request-status.md) or [`Get recurring request status`](get-recurring-request-status.md). Use the endpoint that corresponds to the scope of the requested report and include the request identifier in the path.

If the job status is `completed` or `completed_with_error`, the data associated with the request is ready to download.

#### Transfer Data

Get the download URLs for a completed request by making a `GET` request to [`Get one-time request download URLs`](get-one-time-request-download-urls.md) or [`Get recurring request download URLs`](get-recurring-request-download-urls.md), including the request identifier in the path.

The response contains a list of URLs to which you make `GET` requests, to retrieve the person’s data.

Download URLs are available for 3 days after the download request completes. The URLs you receive are valid for 15 minutes after you request them.

For information on the content and terms used in the files you download, see [`Data and Privacy`](https://developer.apple.comhttps://privacy.apple.com/file-guides/transfer/accountdata).

#### Resubmit Recurring Requests

For app install or push notification requests, add the next instance of a recurring request to the queue by making a `POST` request to the [`Resubmit request`](resubmit-request.md) endpoint. Include the parent request identifier and the request identifier of the most recent instance in your request.

The server’s response contains the request identifier of the new request, and a delay to wait before you can check the new request’s status.

## Topics

### Request creation
- [Submit request](submit-request.md)
  Starts preparing someone’s data for download.
- [object JobSubmission](jobsubmission.md)
  An object that describes a submission that requests someone’s data.
- [object CreatedJob](createdjob.md)
  An object that represents a newly created download request.
- [Resubmit request](resubmit-request.md)
  Enqueue the next instance of a recurring request.
- [object ResubmissionRequest](resubmissionrequest.md)
  An object that describes a request to resubmit a recurring download request.
- [object ResubmissionResponse](resubmissionresponse.md)
  An object that represents a resubmitted recurring download request.
### Status
- [Get one-time request status](get-one-time-request-status.md)
  Find the status of a one-time download request.
- [Get recurring request status](get-recurring-request-status.md)
  Get the status of an instance of a recurring download request.
- [object RequestStatus](requeststatus.md)
  An object that represents the status of a download request.
### Downloads
- [Get one-time request download URLs](get-one-time-request-download-urls.md)
  Get URLs to retrieve someone’s data.
- [Get recurring request download URLs](get-recurring-request-download-urls.md)
  Get URLs to download a snapshot of someone’s data from a recurring series.
- [object DownloadLinks](downloadlinks.md)
  An object that contains URLs to download someone’s account data.
- [object DownloadError](downloaderror.md)
  An object that describes an error the server encounters preparing download URLs for a request.
### Cancellation
- [Cancel request](cancel-request.md)
  Tells the server to stop processing an active request.
- [object CancellationRequest](cancellationrequest.md)
  An object that identifies a one-time request, or an individual instance of a recurring request, to cancel.
- [object CancellationResponse](cancellationresponse.md)
  An object that describes the outcome of canceling a download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccountDataTransfer)*