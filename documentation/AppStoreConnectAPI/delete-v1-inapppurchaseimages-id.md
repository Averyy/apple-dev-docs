# Delete an In-App Purchase Image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete the image asset that appears on the App Store listing that represents an in-app purchase.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `inAppPurchaseImages` resource ID from the [`List In-App Purchase Images`](get-v2-inapppurchases-_id_-images.md) response.

## See Also

- [Create an Image for an In-App Purchase](post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an in-app purchase.
- [Read In-App Purchase Image Information](get-v1-inapppurchaseimages-_id_.md)
  Read details about a specific in-app purchase image.
- [List In-App Purchase Images](get-v2-inapppurchases-_id_-images.md)
  List all images for a specific in-app purchase.
- [Read In-App Purchase Image Information](patch-v1-inapppurchaseimages-_id_.md)
  Read details about a specific in-app purchase image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-inapppurchaseimages-_id_)*