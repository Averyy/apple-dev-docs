# Create a review screenshot for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve a review screenshot for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionAppStoreReviewScreenshots`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionAppStoreReviewScreenshotCreateRequest`

## Responses

- `201` Created (`SubscriptionAppStoreReviewScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read subscription review screenshot information](./get-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Get the information about a review screenshot for an auto-renewable subscription.
- [Commit a review screenshot for an auto-renewable subscription](./patch-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Commit an uploaded image asset as a review screenshot for an auto-renewable subscription.
- [Delete a review screenshot for an auto-renewable subscription](./delete-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Delete an image that you uploaded for review of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionappstorereviewscreenshots)*