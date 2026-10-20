# Commit a review screenshot for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an uploaded image asset as a review screenshot for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Submitting subscriptions and subscription groups for App Review](submitting-subscriptions-and-subscription-groups-for-app-review.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionAppStoreReviewScreenshots/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read subscription review screenshot information](get-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Get the information about a review screenshot for an auto-renewable subscription.
- [Create a review screenshot for an auto-renewable subscription](post-v1-subscriptionappstorereviewscreenshots.md)
  Reserve a review screenshot for an auto-renewable subscription.
- [Delete a review screenshot for an auto-renewable subscription](delete-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Delete an image that you uploaded for review of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionappstorereviewscreenshots-_id_)*