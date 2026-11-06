# Modify a retention message localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the header and body text of a specific retention message localization.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/retentionMessageLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message localization resource ID from the [`List localizations for a retention message version`](./get-v1-retentionmessageversions-_id_-localizations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `RetentionMessageLocalizationUpdateRequest`

The request body you use to modify a retention message localization.

## Responses

- `200` OK (`RetentionMessageLocalizationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Managing retention message localizations
- [Create a retention message localization](./post-v1-retentionmessagelocalizations.md)
  Create a localization of the header and body text for a retention message version.
- [Delete a retention message localization](./delete-v1-retentionmessagelocalizations-_id_.md)
  Delete a specific retention message localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-retentionmessagelocalizations-_id_)*