# Read subscription group localization information (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the specific localized subscription group display name and optional custom app name for a subscription group.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Read subscription group localization information`](./get-v2-subscriptiongrouplocalizations-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionGroupLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionGroupLocalizations]` ([string]): **Allowed Values**: `name`, `customAppName`, `locale`, `state`, `subscriptionGroup`
- `include` ([string]): **Allowed Values**: `subscriptionGroup`
- `fields[subscriptionGroups]` ([string]): **Allowed Values**: `referenceName`, `subscriptions`, `subscriptionGroupLocalizations`, `versions`

## Responses

- `200` OK (`SubscriptionGroupLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription group localization (v1)](./post-v1-subscriptiongrouplocalizations.md)
  Create a localized display name and optional custom app name for a subscription group.
- [Modify a subscription group localization (v1)](./patch-v1-subscriptiongrouplocalizations-_id_.md)
  Update a specific localized display name and optional custom app name for a subscription group.
- [Delete a subscription group localization (v1)](./delete-v1-subscriptiongrouplocalizations-_id_.md)
  Delete localized metadata that you configured for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongrouplocalizations-_id_)*