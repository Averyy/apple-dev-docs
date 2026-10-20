# Read app info localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read localized app-level information.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfoLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app info localization resource ID from the [`List all app info localizations for an app info`](./get-v1-appinfos-_id_-appinfolocalizations.md) response.

### Query Parameters

- `fields[appInfoLocalizations]` ([string]): Additional fields to include for each app info localization resource returned by the response.

  **Allowed Values**: `locale`, `name`, `subtitle`, `privacyPolicyUrl`, `privacyChoicesUrl`, `privacyPolicyText`, `appInfo`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appInfo`
- `fields[appInfos]` ([string]): **Allowed Values**: `appStoreState`, `state`, `appStoreAgeRating`, `australiaAgeRating`, `brazilAgeRating`, `brazilAgeRatingV2`, `franceAgeRating`, `koreaAgeRating`, `app`, `ageRatingDeclaration`, `appInfoLocalizations`, `primaryCategory`, `primarySubcategoryOne`, `primarySubcategoryTwo`, `secondaryCategory`, `secondarySubcategoryOne`, `secondarySubcategoryTwo`, `territoryAgeRatings`

## Responses

- `200` OK (`AppInfoLocalizationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading App Localization Information
- [List all app info localizations for an app info](./get-v1-appinfos-_id_-appinfolocalizations.md)
  Get a list of localized, app-level information for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfolocalizations-_id_)*