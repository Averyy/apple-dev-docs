# Read subscription group localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the custom name for a specific locale of a subscription group configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/subscriptionGroupLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionGroupLocalizations]` ([string]): **Allowed Values**: `name`, `customAppName`, `locale`, `version`
- `fields[subscriptionGroupVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscriptionGroup`, `localizations`
- `include` ([string]): **Allowed Values**: `version`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `200` OK (`SubscriptionGroupLocalizationV2Response`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription group localization](./post-v2-subscriptiongrouplocalizations.md)
  Create a localized custom name for a subscription group configured with the v2 API.
- [Modify a subscription group localization](./patch-v2-subscriptiongrouplocalizations-_id_.md)
  Update the custom name for a specific locale of a subscription group configured with the v2 API.
- [Delete a subscription group localization](./delete-v2-subscriptiongrouplocalizations-_id_.md)
  Delete a localized custom name for a subscription group configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-subscriptiongrouplocalizations-_id_)*