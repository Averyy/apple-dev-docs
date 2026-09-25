# Read In-App Purchase review screenshot information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific review screenshot for an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing In-App Purchases](managing-in-app-purchases.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseAppStoreReviewScreenshots/{id}`

## Parameters

- `fields[inAppPurchaseAppStoreReviewScreenshots]` ([string])
- `include` ([string])
- `fields[inAppPurchases]` ([string])

## See Also

- [Create an In-App Purchase review screenshot](post-v1-inapppurchaseappstorereviewscreenshots.md)
  Reserve a review screenshot for an In-App Purchase.
- [Commit a review screenshot for an In-App Purchase](patch-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Commit an uploaded image asset as a review screenshot for an In-App Purchase.
- [Delete a review screenshot for an In-App Purchase](delete-v1-inapppurchaseappstorereviewscreenshots-_id_.md)
  Delete an image that you uploaded for review of an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseappstorereviewscreenshots-_id_)*