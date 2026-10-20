# Modify a subscription localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the display name and description for a specific locale of a subscription configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/subscriptionLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionLocalizationV2UpdateRequest`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `200` OK (`SubscriptionLocalizationV2Response`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription localization](./post-v2-subscriptionlocalizations.md)
  Create a localized display name and description for an auto-renewable subscription configured with the v2 API.
- [Read subscription localization information](./get-v2-subscriptionlocalizations-_id_.md)
  Get the display name and description for a specific locale of a subscription configured with the v2 API.
- [Delete a subscription localization](./delete-v2-subscriptionlocalizations-_id_.md)
  Delete a localized display name and description for a subscription configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-subscriptionlocalizations-_id_)*