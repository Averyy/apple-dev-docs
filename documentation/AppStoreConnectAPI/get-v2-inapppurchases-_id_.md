# Read In-App Purchase information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [App Store Connect API 2.4 release notes](./app-store-connect-api-2-4-release-notes.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `include` ([string]): **Allowed Values**: `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[inAppPurchaseAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[inAppPurchaseAppStoreReviewScreenshots]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `inAppPurchaseV2`
- `fields[inAppPurchaseContents]` ([string]): **Allowed Values**: `fileName`, `fileSize`, `url`, `lastModifiedDate`, `inAppPurchaseV2`
- `fields[inAppPurchaseImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `inAppPurchase`
- `fields[inAppPurchaseLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `state`, `inAppPurchaseV2`
- `fields[inAppPurchaseOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `productionCodeCount`, `sandboxCodeCount`, `active`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[inAppPurchasePricePoints]` ([string]): **Allowed Values**: `customerPrice`, `proceeds`, `territory`, `equalizations`
- `fields[inAppPurchasePriceSchedules]` ([string]): **Allowed Values**: `baseTerritory`, `manualPrices`, `automaticPrices`
- `fields[inAppPurchaseVersions]` ([string]): **Allowed Values**: `version`, `state`, `inAppPurchase`, `image`, `images`, `localizations`
- `fields[inAppPurchases]` ([string]): **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[promotedPurchases]` ([string]): **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `limit[images]` (integer): **Maximum**: `50`
- `limit[inAppPurchaseLocalizations]` (integer): **Maximum**: `50`
- `limit[offerCodes]` (integer): **Maximum**: `50`
- `limit[pricePoints]` (integer): **Maximum**: `8000`
- `limit[versions]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`InAppPurchaseV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an In-App Purchase](./post-v2-inapppurchases.md)
  Create an In-App Purchase, including a consumable, non-consumable, or non-renewing subscription.
- [List all In-App Purchases for an app](./get-v1-apps-_id_-inapppurchasesv2.md)
  Get a list of the In-App Purchases for a specific app.
- [Modify an In-App Purchase](./patch-v2-inapppurchases-_id_.md)
  Update the reference name of a specific In-App Purchase.
- [Delete an In-App Purchase](./delete-v2-inapppurchases-_id_.md)
  Delete a specific In-App Purchase from your app.
- [List all price points for an In-App Purchase](./get-v2-inapppurchases-_id_-pricepoints.md)
  Get a list of possible price points for an In-App Purchase.
- [List price point IDs for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-pricepoints.md)
  Get a list of price point IDs for a specific In-App Purchase.
- [List All In-App Purchase Price Point Equalizations](./get-v1-inapppurchasepricepoints-_id_-equalizations.md)
  Get a list of In-App Purchase price points and their equivalent in a specified currency.
- [List equalization IDs for an In-App Purchase price point](./get-v1-inapppurchasepricepoints-_id_-relationships-equalizations.md)
- [Read promoted purchase information for an In-App Purchase](./get-v2-inapppurchases-_id_-promotedpurchase.md)
  Get details about the promoted purchase of an In-App Purchase.
- [Read the promoted purchase ID for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-promotedpurchase.md)
  Get the promoted purchase ID for a specific In-App Purchase.
- [List all localizations for an In-App Purchase](./get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific In-App Purchase.
- [List localization IDs for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-inapppurchaselocalizations.md)
  Get a list of localization IDs for a specific In-App Purchase.
- [Read review screenshot information for an In-App Purchase](./get-v2-inapppurchases-_id_-appstorereviewscreenshot.md)
  Get information about a review screenshot for a specific In-App Purchase.
- [Read the App Store review screenshot ID for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-appstorereviewscreenshot.md)
  Get the App Store review screenshot ID for a specific In-App Purchase.
- [Create a review submission for an In-App Purchase](./post-v1-inapppurchasesubmissions.md)
  Create an In-App Purchase submission for review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchases-_id_)*