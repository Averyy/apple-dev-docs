# Read In-App Purchase localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the display name and description for a specific locale of an In-App Purchase configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchaseLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[inAppPurchaseLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `version`
- `fields[inAppPurchaseVersions]` ([string]): **Allowed Values**: `version`, `state`, `inAppPurchase`, `image`, `images`, `localizations`
- `include` ([string]): **Allowed Values**: `version`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `200` OK (`InAppPurchaseLocalizationV2Response`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List localizations for an In-App Purchase version](./get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an In-App Purchase.
- [Create an In-App Purchase localization](./post-v2-inapppurchaselocalizations.md)
  Create a localized display name and description for an In-App Purchase configured with the v2 API.
- [Modify an In-App Purchase localization](./patch-v2-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an In-App Purchase configured with the v2 API.
- [Delete an In-App Purchase localization](./delete-v2-inapppurchaselocalizations-_id_.md)
  Delete a localized display name and description for an In-App Purchase configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchaselocalizations-_id_)*