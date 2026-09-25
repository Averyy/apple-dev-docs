# Delete an In-App Purchase image (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete the image asset that appears on the App Store listing that represents an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `inAppPurchaseImages` resource ID from the [`List In-App Purchase images`](get-v2-inapppurchases-_id_-images.md) response.

## See Also

- [Create an image for an In-App Purchase (v1)](post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an In-App Purchase.
- [Read In-App Purchase image information (v1)](get-v1-inapppurchaseimages-_id_.md)
  Read details about a specific In-App Purchase image.
- [List In-App Purchase images](get-v2-inapppurchases-_id_-images.md)
  List all images for a specific In-App Purchase.
- [Commit an image for an In-App Purchase (v1)](patch-v1-inapppurchaseimages-_id_.md)
  Commit an uploaded image asset for an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-inapppurchaseimages-_id_)*