# Create a beta build localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create localized What’s New text for a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaBuildLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaBuildLocalizationCreateRequest`

## Responses

- `201` Created (`BetaBuildLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Beta Build Localizations
- [Modify a beta build localization](./patch-v1-betabuildlocalizations-_id_.md)
  Update the localized What’s New text for a specific beta build and locale.
- [Delete a beta build localization](./delete-v1-betabuildlocalizations-_id_.md)
  Delete a specific beta build localization associated with a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betabuildlocalizations)*