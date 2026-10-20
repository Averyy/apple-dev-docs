# Send notification of an available build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Send a notification to all assigned beta testers that a build is available for testing.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/buildBetaNotifications`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BuildBetaNotificationCreateRequest`

## Responses

- `201` Created (`BuildBetaNotificationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-buildbetanotifications)*