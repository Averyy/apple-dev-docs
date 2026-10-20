# Get the App Store review screenshot ID for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/appStoreReviewScreenshot`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`SubscriptionAppStoreReviewScreenshotLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting the App Store review screenshot
- [Read review screenshot information for a subscription](./get-v1-subscriptions-_id_-appstorereviewscreenshot.md)
  Get information about review screenshot for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-appstorereviewscreenshot)*