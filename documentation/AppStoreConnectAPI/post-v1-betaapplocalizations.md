# Create a beta app localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create localized descriptive information for an app.

**Availability**:
- App Store Connect API 1.0+

## Overview

> ❗ **Important**:  A description is required for all `betaAppLocalizations` before you can submit to beta app review.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaAppLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaAppLocalizationCreateRequest`

## Responses

- `201` Created (`BetaAppLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Localizations
- [Modify a beta app localization](./patch-v1-betaapplocalizations-_id_.md)
  Update the localized information for a specific beta app and locale.
- [Delete a beta app localization](./delete-v1-betaapplocalizations-_id_.md)
  Delete a beta app localization associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betaapplocalizations)*