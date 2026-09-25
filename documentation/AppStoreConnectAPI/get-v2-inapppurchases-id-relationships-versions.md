# Get the resource IDs of the versions of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the related resource IDs for the draft versions of an In-App Purchase configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchases/{id}/relationships/versions`

## Parameters

- `limit` (integer)

## See Also

- [Create an In-App Purchase version](post-v1-inapppurchaseversions.md)
  Create a draft version of an In-App Purchase, capturing its current localized metadata and review images for App Review submission.
- [Read In-App Purchase version information](get-v1-inapppurchaseversions-_id_.md)
  Get information about a specific draft version of an In-App Purchase.
- [Read the image for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-image.md)
  Get the review image attached to a draft version of an In-App Purchase.
- [List images for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-images.md)
  List the review images attached to a draft version of an In-App Purchase.
- [List localizations for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an In-App Purchase.
- [Read the image ID for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-relationships-image.md)
  Get the related resource ID for the review image attached to a draft version of an In-App Purchase.
- [List image IDs for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-relationships-images.md)
  Get the related resource IDs for the review images attached to a draft version of an In-App Purchase.
- [List localization IDs for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of an In-App Purchase.
- [List the versions of an In-App Purchase](get-v2-inapppurchases-_id_-versions.md)
  List the draft versions of an In-App Purchase configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchases-_id_-relationships-versions)*