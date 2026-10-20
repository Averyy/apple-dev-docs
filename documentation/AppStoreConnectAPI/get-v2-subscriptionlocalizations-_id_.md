# Read subscription localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the display name and description for a specific locale of a subscription configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/subscriptionLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `description`, `version`
- `fields[subscriptionVersions]` ([string]): **Allowed Values**: `version`, `state`, `subscription`, `image`, `images`, `localizations`
- `include` ([string]): **Allowed Values**: `version`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `200` OK (`SubscriptionLocalizationV2Response`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription localization](./post-v2-subscriptionlocalizations.md)
  Create a localized display name and description for an auto-renewable subscription configured with the v2 API.
- [Modify a subscription localization](./patch-v2-subscriptionlocalizations-_id_.md)
  Update the display name and description for a specific locale of a subscription configured with the v2 API.
- [Delete a subscription localization](./delete-v2-subscriptionlocalizations-_id_.md)
  Delete a localized display name and description for a subscription configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-subscriptionlocalizations-_id_)*