# Create a subscription localization (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a localized display name and description for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Create a subscription localization`](./post-v2-subscriptionlocalizations.md) instead.

## Mentions

- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)

## Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionLocalizationCreateRequest`

## Responses

- `201` Created (`SubscriptionLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List all localizations for an auto-renewable subscription](./get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [List localization IDs for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-subscriptionlocalizations.md)
- [Read subscription localization information (v1)](./get-v1-subscriptionlocalizations-_id_.md)
  Get the specific localized metadata for an auto-renewable subscription.
- [Modify a subscription localization (v1)](./patch-v1-subscriptionlocalizations-_id_.md)
  Update a specific localized subscription display name and description for an auto-renewable subscription.
- [Delete a subscription localization (v1)](./delete-v1-subscriptionlocalizations-_id_.md)
  Delete localized metadata that you configured for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionlocalizations)*