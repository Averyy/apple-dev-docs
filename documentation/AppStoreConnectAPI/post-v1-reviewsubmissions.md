# Create a Review Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a review submission for a specific app.

**Availability**:
- App Store Connect API 1.7+

## Mentions

- [App Store Connect API 4.0 release notes](./app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.1 release notes](./app-store-connect-api-4-1-release-notes.md)
- [Configuring Game center activities](./configuring-game-center-activities.md)
- [Configuring Game Center challenges](./configuring-game-center-challenges.md)
- [Uploading and versioning Apple hosted background assets](./managing-apple-hosted-background-assets.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)
- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)
- [Understanding webhook events](./webhook-events.md)

#### Overview

> **Note**: The attribute `platform` is no longer required when using [`Create a Review Submission`](./post-v1-reviewsubmissions.md). You can optionally add the attribute platform when using [`Modify a Review Submission`](./patch-v1-reviewsubmissions-_id_.md).

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/reviewSubmissions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReviewSubmissionCreateRequest`

## Responses

- `201` Created (`ReviewSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List Review Submissions for an App](./get-v1-reviewsubmissions.md)
  List recent and current review submissions for a specific app.
- [Read Review Submission Information](./get-v1-reviewsubmissions-_id_.md)
  Read information about a specific review submisison.
- [List the Items in a Review Submission](./get-v1-reviewsubmissions-_id_-items.md)
  List all the items in a specific review submission.
- [List item IDs](./get-v1-reviewsubmissions-_id_-relationships-items.md)
  Get the list of item IDs for a specific review submission.
- [List review submission IDs](./get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.
- [Modify a Review Submission](./patch-v1-reviewsubmissions-_id_.md)
  Edit the details or contents of a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-reviewsubmissions)*