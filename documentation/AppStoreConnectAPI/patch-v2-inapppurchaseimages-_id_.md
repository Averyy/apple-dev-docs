# Modify an In-App Purchase image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit the asset upload for an In-App Purchase image configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
- [Working with In-App Purchase versions](./working-with-in-app-purchase-versions.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/inAppPurchaseImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseImageV2UpdateRequest`

## Responses

- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `200` OK (`InAppPurchaseImageV2Response`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an In-App Purchase image](./post-v2-inapppurchaseimages.md)
  Reserve a promotion image for an In-App Purchase configured with the v2 API and prepare its asset upload.
- [Read In-App Purchase image information](./get-v2-inapppurchaseimages-_id_.md)
  Get the metadata for an In-App Purchase image configured with the v2 API, including the asset upload state.
- [Delete an In-App Purchase image](./delete-v2-inapppurchaseimages-_id_.md)
  Delete an In-App Purchase image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-inapppurchaseimages-_id_)*