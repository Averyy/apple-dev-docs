# Create a retention message version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a version of a retention message to submit to App Review.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/retentionMessageVersions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RetentionMessageVersionCreateRequest`

The request body you use to create a retention message version.

## Responses

- `201` Created (`RetentionMessageVersionResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-retentionmessageversions)*