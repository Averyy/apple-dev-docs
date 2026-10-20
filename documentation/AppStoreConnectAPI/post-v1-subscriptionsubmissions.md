# Create a review submission for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a review submission for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use the review submissions workflow at [Review submissions](./review-submissions.md) instead.

## Mentions

- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionSubmissions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionSubmissionCreateRequest`

## Responses

- `201` Created (`SubscriptionSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a review submission for a subscription group](./post-v1-subscriptiongroupsubmissions.md)
  Create a subscription group submission for review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionsubmissions)*