# Create a subscription group localization (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a localized display name and optional custom app name for a subscription group.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Create a subscription group localization`](./post-v2-subscriptiongrouplocalizations.md) instead.

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionGroupLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionGroupLocalizationCreateRequest`

## Responses

- `201` Created (`SubscriptionGroupLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read subscription group localization information (v1)](./get-v1-subscriptiongrouplocalizations-_id_.md)
  Get the specific localized subscription group display name and optional custom app name for a subscription group.
- [Modify a subscription group localization (v1)](./patch-v1-subscriptiongrouplocalizations-_id_.md)
  Update a specific localized display name and optional custom app name for a subscription group.
- [Delete a subscription group localization (v1)](./delete-v1-subscriptiongrouplocalizations-_id_.md)
  Delete localized metadata that you configured for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptiongrouplocalizations)*