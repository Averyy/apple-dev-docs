# Create a subscription image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve a promotion image for an auto-renewable subscription configured with the v2 API and prepare its asset upload.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Submitting subscriptions and subscription groups for App Review](./submitting-subscriptions-and-subscription-groups-for-app-review.md)
- [Working with subscription versions](./working-with-subscription-versions.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/subscriptionImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionImageV2CreateRequest`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `201` Created (`SubscriptionImageV2Response`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read subscription image information](./get-v2-subscriptionimages-_id_.md)
  Get the metadata for a subscription image configured with the v2 API, including the asset upload state.
- [Modify a subscription image](./patch-v2-subscriptionimages-_id_.md)
  Commit the asset upload for a subscription image configured with the v2 API.
- [Delete a subscription image](./delete-v2-subscriptionimages-_id_.md)
  Delete a subscription image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-subscriptionimages)*