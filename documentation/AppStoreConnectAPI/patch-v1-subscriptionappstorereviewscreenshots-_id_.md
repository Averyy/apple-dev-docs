# Commit a review screenshot for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit an uploaded image asset as a review screenshot for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionAppStoreReviewScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionAppStoreReviewScreenshotUpdateRequest`

## Responses

- `200` OK (`SubscriptionAppStoreReviewScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read subscription review screenshot information](./get-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Get the information about a review screenshot for an auto-renewable subscription.
- [Create a review screenshot for an auto-renewable subscription](./post-v1-subscriptionappstorereviewscreenshots.md)
  Reserve a review screenshot for an auto-renewable subscription.
- [Delete a review screenshot for an auto-renewable subscription](./delete-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Delete an image that you uploaded for review of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionappstorereviewscreenshots-_id_)*