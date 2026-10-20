# List the versions of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the draft versions of an In-App Purchase configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)
- [Working with In-App Purchase versions](./working-with-in-app-purchase-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchases/{id}/versions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `filter[state]` ([string]): **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `APPROVED`, `REPLACED_WITH_NEW_VERSION`, `REJECTED`, `DEVELOPER_REJECTED`
- `fields[inAppPurchaseVersions]` ([string]): **Allowed Values**: `version`, `state`, `inAppPurchase`, `image`, `images`, `localizations`
- `fields[inAppPurchases]` ([string]): **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[inAppPurchaseImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `assetToken`, `imageAsset`, `uploadOperations`, `assetDeliveryState`
- `fields[inAppPurchaseLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `version`
- `limit` (integer): **Maximum**: `200`
- `include` ([string]): **Allowed Values**: `inAppPurchase`, `image`, `images`, `localizations`
- `limit[images]` (integer): **Maximum**: `50`
- `limit[localizations]` (integer): **Maximum**: `50`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `200` OK (`InAppPurchaseVersionsResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an In-App Purchase version](./post-v1-inapppurchaseversions.md)
  Create a draft version of an In-App Purchase, capturing its current localized metadata and review images for App Review submission.
- [Read In-App Purchase version information](./get-v1-inapppurchaseversions-_id_.md)
  Get information about a specific draft version of an In-App Purchase.
- [Read the image for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-image.md)
  Get the review image attached to a draft version of an In-App Purchase.
- [List images for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-images.md)
  List the review images attached to a draft version of an In-App Purchase.
- [List localizations for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an In-App Purchase.
- [Read the image ID for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-relationships-image.md)
  Get the related resource ID for the review image attached to a draft version of an In-App Purchase.
- [List image IDs for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-relationships-images.md)
  Get the related resource IDs for the review images attached to a draft version of an In-App Purchase.
- [List localization IDs for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of an In-App Purchase.
- [Get the resource IDs of the versions of an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of an In-App Purchase configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchases-_id_-versions)*