# Create a retention message

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a retention message for an app.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [App Store Connect API 4.6 release notes](./app-store-connect-api-4-6-release-notes.md)
- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/retentionMessages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RetentionMessageCreateRequest`

The request body you use to create a retention message.

## Responses

- `201` Created (`RetentionMessageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Managing retention messages
- [Delete a retention message](./delete-v1-retentionmessages-_id_.md)
  Delete a specific retention message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-retentionmessages)*