# Read in-app purchase image information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read details about a specific in-app purchase image.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

- `fields[inAppPurchaseImages]` ([string])
- `fields[inAppPurchases]` ([string])
- `include` ([string])

## See Also

- [Create an image for an in-app purchase (v1)](post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an in-app purchase.
- [List in-app purchase images](get-v2-inapppurchases-_id_-images.md)
  List all images for a specific in-app purchase.
- [Commit an image for an in-app purchase (v1)](patch-v1-inapppurchaseimages-_id_.md)
  Commit an uploaded image asset for an in-app purchase.
- [Delete an in-app purchase image (v1)](delete-v1-inapppurchaseimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseimages-_id_)*