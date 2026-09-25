# Read In-App Purchase image information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read details about a specific In-App Purchase image.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

- `fields[inAppPurchaseImages]` ([string])
- `fields[inAppPurchases]` ([string])
- `include` ([string])

## See Also

- [Create an image for an In-App Purchase (v1)](post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an In-App Purchase.
- [List In-App Purchase images](get-v2-inapppurchases-_id_-images.md)
  List all images for a specific In-App Purchase.
- [Commit an image for an In-App Purchase (v1)](patch-v1-inapppurchaseimages-_id_.md)
  Commit an uploaded image asset for an In-App Purchase.
- [Delete an In-App Purchase image (v1)](delete-v1-inapppurchaseimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseimages-_id_)*