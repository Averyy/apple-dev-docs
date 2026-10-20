# Get the build ID for a beta build localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaBuildLocalizations/{id}/relationships/build`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`BetaBuildLocalizationBuildLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [List beta build localizations](./get-v1-betabuildlocalizations.md)
  Find and list beta build localizations currently associated with apps.
- [Read beta build localization information](./get-v1-betabuildlocalizations-_id_.md)
  Get a specific beta build localization resource.
- [Read the build information of a beta build localization](./get-v1-betabuildlocalizations-_id_-build.md)
  Get the build information for a specific beta build localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betabuildlocalizations-_id_-relationships-build)*