# Delete a subscription group localization (v1)

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete localized metadata that you configured for a subscription group.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use [`Delete a subscription group localization`](./delete-v2-subscriptiongrouplocalizations-_id_.md) instead.

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptionGroupLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription group localization (v1)](./post-v1-subscriptiongrouplocalizations.md)
  Create a localized display name and optional custom app name for a subscription group.
- [Read subscription group localization information (v1)](./get-v1-subscriptiongrouplocalizations-_id_.md)
  Get the specific localized subscription group display name and optional custom app name for a subscription group.
- [Modify a subscription group localization (v1)](./patch-v1-subscriptiongrouplocalizations-_id_.md)
  Update a specific localized display name and optional custom app name for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptiongrouplocalizations-_id_)*