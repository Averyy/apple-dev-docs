# Create a retention message localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a localization of the header and body text for a retention message version.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [App Store Connect API 4.6 release notes](./app-store-connect-api-4-6-release-notes.md)
- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/retentionMessageLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RetentionMessageLocalizationCreateRequest`

The request body you use to create a retention message localization.

## Responses

- `201` Created (`RetentionMessageLocalizationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Managing retention message localizations
- [Modify a retention message localization](./patch-v1-retentionmessagelocalizations-_id_.md)
  Update the header and body text of a specific retention message localization.
- [Delete a retention message localization](./delete-v1-retentionmessagelocalizations-_id_.md)
  Delete a specific retention message localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-retentionmessagelocalizations)*