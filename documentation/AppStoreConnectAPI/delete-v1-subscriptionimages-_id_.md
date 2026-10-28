# Delete a subscription image (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete the image asset that appears on the App Store listing that represents a subscription.

**Availability**:
- App Store Connect API 3.6+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Delete a subscription image`](./delete-v2-subscriptionimages-_id_.md) instead.

## Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptionImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionImages` resource ID from the [`List Subscription Images`](./get-v1-subscriptions-_id_-images.md) response.

## Responses

- `204` No Content
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
- [List subscription image ids](./get-v1-subscriptions-_id_-relationships-images.md)
  List all images IDs for a specific subscription.
- [Commit a subscription image (v1)](./patch-v1-subscriptionimages-_id_.md)
  Commit an uploaded subscription image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptionimages-_id_)*