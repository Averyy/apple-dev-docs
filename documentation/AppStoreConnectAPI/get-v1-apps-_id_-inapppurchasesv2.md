# List all In-App Purchases for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of the In-App Purchases for a specific app.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [App Store Connect API 2.0 release notes](./app-store-connect-api-2-0-release-notes.md)
- [App Store Connect API 2.2 release notes](./app-store-connect-api-2-2-release-notes.md)
- [App Store Connect API 2.4 release notes](./app-store-connect-api-2-4-release-notes.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/inAppPurchasesV2`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[inAppPurchaseAppStoreReviewScreenshots]` ([string]): Additional fields to include for each In-App Purchase App Store review screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `inAppPurchaseV2`
- `fields[inAppPurchaseContents]` ([string]): Additional fields to include for each In-App Purchase content resource returned by the response.

  **Allowed Values**: `fileName`, `fileSize`, `url`, `lastModifiedDate`, `inAppPurchaseV2`
- `fields[inAppPurchaseLocalizations]` ([string]): Additional fields to include for each In-App Purchase localization resource returned by the response.

  **Allowed Values**: `name`, `locale`, `description`, `state`, `inAppPurchaseV2`
- `fields[inAppPurchases]` ([string]): Additional fields to include for each In-App Purchase resource returned by the response.

  **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[promotedPurchases]` ([string]): Additional fields to include for each promoted purchase resource returned by the response.

  **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `filter[inAppPurchaseType]` ([string]): Filter the returned In-App Purchases by In-App Purchase type.

  **Allowed Values**: `CONSUMABLE`, `NON_CONSUMABLE`, `NON_RENEWING_SUBSCRIPTION`
- `filter[name]` ([string]): Filter the returned In-App Purchases by name.
- `filter[productId]` ([string]): Filter the returned In-App Purchases by product ID.
- `filter[state]` ([string]): Filter the returned In-App Purchases by state.

  **Allowed Values**: `MISSING_METADATA`, `WAITING_FOR_UPLOAD`, `PROCESSING_CONTENT`, `READY_TO_SUBMIT`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `DEVELOPER_ACTION_NEEDED`, `PENDING_BINARY_APPROVAL`, `APPROVED`, `DEVELOPER_REMOVED_FROM_SALE`, `REMOVED_FROM_SALE`, `REJECTED`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `inAppPurchaseLocalizations`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `limit` (integer): The maximum number of In-App Purchase resources to return.

  **Maximum**: `200`
- `limit[inAppPurchaseLocalizations]` (integer): The maximum number of related In-App Purchase localizations resources to return.

  **Maximum**: `50`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `name`, `-name`, `inAppPurchaseType`, `-inAppPurchaseType`
- `fields[inAppPurchasePriceSchedules]` ([string]): Additional fields to include for each In-App Purchase price schedule resource returned by the response.

  **Allowed Values**: `baseTerritory`, `manualPrices`, `automaticPrices`
- `fields[inAppPurchaseAvailabilities]` ([string]): Additional fields to include for each In-App Purchase availability resource returned by the response.

  **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[inAppPurchaseImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `assetToken`, `imageAsset`, `uploadOperations`, `state`, `inAppPurchase`
- `fields[inAppPurchaseOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `productionCodeCount`, `sandboxCodeCount`, `active`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[inAppPurchaseVersions]` ([string]): **Allowed Values**: `version`, `state`, `inAppPurchase`, `image`, `images`, `localizations`
- `limit[images]` (integer): **Maximum**: `50`
- `limit[offerCodes]` (integer): **Maximum**: `50`
- `limit[versions]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`InAppPurchasesV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting In-App Purchase information
- [GET /v1/apps/{id}/relationships/inAppPurchasesV2](./get-v1-apps-_id_-relationships-inapppurchasesv2.md)
- [List all In-App Purchases for an app v1](./get-v1-apps-_id_-inapppurchases.md)
  List the In-App Purchases that are available for your app.
- [List In-App Purchases ids for an app v1](./get-v1-apps-_id_-relationships-inapppurchases.md)
  Get a list of all In-App Purchases IDs for a specific app V1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-inapppurchasesv2)*