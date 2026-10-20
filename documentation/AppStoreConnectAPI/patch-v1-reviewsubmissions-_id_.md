# Modify a Review Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Edit the details or contents of a review submission.

**Availability**:
- App Store Connect API 1.7+

## Mentions

- [App Store Connect API 4.1 release notes](./app-store-connect-api-4-1-release-notes.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)
- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)

#### Overview

> **Note**: You can optionally add the attribute platform when using [`Modify a Review Submission`](./patch-v1-reviewsubmissions-_id_.md).

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/reviewSubmissions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the review submissions resource. Obtain the app resource ID from the [`List Review Submissions for an App`](./get-v1-reviewsubmissions.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReviewSubmissionUpdateRequest`

## Responses

- `200` OK (`ReviewSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
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
- [Create a Review Submission](./post-v1-reviewsubmissions.md)
  Create a review submission for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-reviewsubmissions-_id_)*