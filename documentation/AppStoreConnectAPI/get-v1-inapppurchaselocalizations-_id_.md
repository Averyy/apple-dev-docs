# Read In-App Purchase localization information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the display name and description for a specific locale for an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Read In-App Purchase localization information`](./get-v2-inapppurchaselocalizations-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[inAppPurchaseLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `state`, `inAppPurchaseV2`
- `include` ([string]): **Allowed Values**: `inAppPurchaseV2`
- `fields[inAppPurchases]` ([string]): **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`

## Responses

- `200` OK (`InAppPurchaseLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List all localizations for an In-App Purchase](./get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific In-App Purchase.
- [Create an In-App Purchase localization (v1)](./post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an In-App Purchase.
- [Modify an In-App Purchase localization (v1)](./patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an In-App Purchase.
- [Delete an In-App Purchase localization (v1)](./delete-v1-inapppurchaselocalizations-_id_.md)
  Delete the metadata for a single In-App Purchase localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaselocalizations-_id_)*