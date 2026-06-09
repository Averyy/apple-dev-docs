# Read in-app purchase review screenshot information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific review screenshot for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing in-app purchases](managing-in-app-purchases.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseAppStoreReviewScreenshots/{id}`

## Parameters

- `fields[inAppPurchaseAppStoreReviewScreenshots]` ([string])
- `include` ([string])
- `fields[inAppPurchases]` ([string])

## See Also

- [Create an in-app purchase review screenshot](post-v1-inapppurchaseappstorereviewscreenshots.md)
  Reserve a review screenshot for an in-app purchase.
- [Commit a review screenshot for an in-app purchase](patch-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Commit an uploaded image asset as a review screenshot for an in-app purchase.
- [Delete a review screenshot for an in-app purchase](delete-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Delete an image that you uploaded for review of an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseappstorereviewscreenshots-_id_)*