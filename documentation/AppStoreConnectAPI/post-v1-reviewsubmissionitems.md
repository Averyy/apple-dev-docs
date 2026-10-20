# Create a Review Submission Item

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a new review submission item.

**Availability**:
- App Store Connect API 1.7+

## Mentions

- [App Store Connect API 4.2 release notes](./app-store-connect-api-4-2-release-notes.md)
- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)
- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/reviewSubmissionItems`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReviewSubmissionItemCreateRequest`

## Responses

- `201` Created (`ReviewSubmissionItemResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Update a review submission item](./patch-v1-reviewsubmissionitems-_id_.md)
  Update a specific review submission item.
- [Remove a review submission item](./delete-v1-reviewsubmissionitems-_id_.md)
  Remove a specific item from a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-reviewsubmissionitems)*