# Create a subscription group localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a localized custom name for a subscription group configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Creating auto-renewable subscription groups](./creating-auto-renewable-subscription-groups.md)
- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)
- [Working with subscription group versions](./working-with-subscription-group-versions.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/subscriptionGroupLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionGroupLocalizationV2CreateRequest`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `201` Created (`SubscriptionGroupLocalizationV2Response`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read subscription group localization information](./get-v2-subscriptiongrouplocalizations-_id_.md)
  Get the custom name for a specific locale of a subscription group configured with the v2 API.
- [Modify a subscription group localization](./patch-v2-subscriptiongrouplocalizations-_id_.md)
  Update the custom name for a specific locale of a subscription group configured with the v2 API.
- [Delete a subscription group localization](./delete-v2-subscriptiongrouplocalizations-_id_.md)
  Delete a localized custom name for a subscription group configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-subscriptiongrouplocalizations)*