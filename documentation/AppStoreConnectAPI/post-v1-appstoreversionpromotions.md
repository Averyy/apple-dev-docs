# Create an app store version promotion

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Promote a specific App Store version.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appStoreVersionPromotions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreVersionPromotionCreateRequest`

## Responses

- `201` Created (`AppStoreVersionPromotionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstoreversionpromotions)*