# Read In-App Purchase Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read details about a specific in-app purchase image.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseImages/{id}`

## Parameters

- `fields[inAppPurchaseImages]` ([string])
- `fields[inAppPurchases]` ([string])
- `include` ([string])

## See Also

- [Create an Image for an In-App Purchase](post-v1-inapppurchaseimages.md)
  Reserve an image asset to appear in the App Store, representing an in-app purchase.
- [List In-App Purchase Images](get-v2-inapppurchases-_id_-images.md)
  The data structure that represents a get-v2-in-app purchases-{id}-images resource.
- [Commit an image for an in-app purchase](patch-v1-inapppurchaseimages-_id_.md)
  Commit an uploaded image asset for an in-app purchase.
- [Delete an In-App Purchase Image](delete-v1-inapppurchaseimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseimages-_id_)*