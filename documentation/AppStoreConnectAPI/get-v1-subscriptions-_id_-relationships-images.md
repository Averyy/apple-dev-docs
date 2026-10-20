# List subscription image ids

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all images IDs for a specific subscription.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.4.1

> **Deprecated**: This relationship is deprecated. Use [`List image IDs for a subscription version`](./get-v1-subscriptionversions-_id_-relationships-images.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/images`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionImagesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an image for a subscription (v1)](./post-v1-subscriptionimages.md)
  Reserve an image asset to appear in the App Store, representing a subscription.
- [Read subscription image information (v1)](./get-v1-subscriptionimages-_id_.md)
  Read details about a specific subscription image.
- [List Subscription Images](./get-v1-subscriptions-_id_-images.md)
  List all images for a specific subscription.
- [Commit a subscription image (v1)](./patch-v1-subscriptionimages-_id_.md)
  Commit an uploaded subscription image.
- [Delete a subscription image (v1)](./delete-v1-subscriptionimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-images)*