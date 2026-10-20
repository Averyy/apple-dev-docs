# Register a new bundle id

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Register a new bundle ID for app development.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/bundleIds`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BundleIdCreateRequest`

## Responses

- `201` Created (`BundleIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-bundleids)*