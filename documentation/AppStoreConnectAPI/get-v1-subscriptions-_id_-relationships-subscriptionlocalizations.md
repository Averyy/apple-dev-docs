# List localization IDs for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.4.1

> **Deprecated**: This relationship is deprecated. Use [`List localization IDs for a subscription version`](./get-v1-subscriptionversions-_id_-relationships-localizations.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/subscriptionLocalizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionSubscriptionLocalizationsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List all localizations for an auto-renewable subscription](./get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [Read subscription localization information (v1)](./get-v1-subscriptionlocalizations-_id_.md)
  Get the specific localized metadata for an auto-renewable subscription.
- [Create a subscription localization (v1)](./post-v1-subscriptionlocalizations.md)
  Create a localized display name and description for an auto-renewable subscription.
- [Modify a subscription localization (v1)](./patch-v1-subscriptionlocalizations-_id_.md)
  Update a specific localized subscription display name and description for an auto-renewable subscription.
- [Delete a subscription localization (v1)](./delete-v1-subscriptionlocalizations-_id_.md)
  Delete localized metadata that you configured for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-subscriptionlocalizations)*