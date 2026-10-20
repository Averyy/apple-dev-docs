# List all app info localizations for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of localized, app-level information for an app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/appInfoLocalizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

### Query Parameters

- `fields[appInfoLocalizations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `locale`, `name`, `subtitle`, `privacyPolicyUrl`, `privacyChoicesUrl`, `privacyPolicyText`, `appInfo`
- `fields[appInfos]` ([string]): Fields to return for included related types.

  **Allowed Values**: `appStoreState`, `state`, `appStoreAgeRating`, `australiaAgeRating`, `brazilAgeRating`, `brazilAgeRatingV2`, `franceAgeRating`, `koreaAgeRating`, `app`, `ageRatingDeclaration`, `appInfoLocalizations`, `primaryCategory`, `primarySubcategoryOne`, `primarySubcategoryTwo`, `secondaryCategory`, `secondarySubcategoryOne`, `secondarySubcategoryTwo`, `territoryAgeRatings`
- `filter[locale]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `appInfo`
- `limit` (integer): Number of included related resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppInfoLocalizationsResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading App Localization Information
- [Read app info localization information](./get-v1-appinfolocalizations-_id_.md)
  Read localized app-level information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-appinfolocalizations)*