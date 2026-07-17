# Delete an in-app purchase image (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete the image asset that appears on the App Store listing that represents an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `inAppPurchaseImages` resource ID from the [`List in-app purchase images`](get-v2-inapppurchases-_id_-images.md) response.

## See Also

- [Create an image for an in-app purchase (v1)](post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an in-app purchase.
- [Read in-app purchase image information (v1)](get-v1-inapppurchaseimages-_id_.md)
  Read details about a specific in-app purchase image.
- [List in-app purchase images](get-v2-inapppurchases-_id_-images.md)
  List all images for a specific in-app purchase.
- [Commit an image for an in-app purchase (v1)](patch-v1-inapppurchaseimages-_id_.md)
  Commit an uploaded image asset for an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-inapppurchaseimages-_id_)*