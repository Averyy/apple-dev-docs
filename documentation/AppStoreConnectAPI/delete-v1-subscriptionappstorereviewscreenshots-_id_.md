# Delete a review screenshot for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an image that you uploaded for review of an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptionAppStoreReviewScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read subscription review screenshot information](./get-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Get the information about a review screenshot for an auto-renewable subscription.
- [Create a review screenshot for an auto-renewable subscription](./post-v1-subscriptionappstorereviewscreenshots.md)
  Reserve a review screenshot for an auto-renewable subscription.
- [Commit a review screenshot for an auto-renewable subscription](./patch-v1-subscriptionappstorereviewscreenshots-_id_.md)
  Commit an uploaded image asset as a review screenshot for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptionappstorereviewscreenshots-_id_)*