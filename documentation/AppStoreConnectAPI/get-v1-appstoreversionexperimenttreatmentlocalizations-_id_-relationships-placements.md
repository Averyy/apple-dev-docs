# List the placement IDs for an App Store version experiment treatment localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of placement resource IDs for a specific App Store version experiment treatment localization.

**Availability**:
- App Store Connect API 4.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatmentLocalizations/{id}/relationships/placements`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `limit` (integer): The maximum number of app asset library placement resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppStoreVersionExperimentTreatmentLocalizationPlacementsLinkagesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read app store version experiment treatment localization information](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Get information about a specific App Store version experiment treatment localization.
- [List all screenshot sets for an experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-appscreenshotsets.md)
  Get a list of screenshot sets for a specific App Store version experiment treatment localization.
- [List all preview sets for an experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-apppreviewsets.md)
  Get a list of preview sets for a specific App Store version experiment treatment localization.
- [List preview set IDs for an App Store version experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-appscreenshotsets.md)
- [Create an app store version experiment treatment localization](./post-v1-appstoreversionexperimenttreatmentlocalizations.md)
  Add a new localization for an App Store version experiment treatment.
- [Delete a treatment localization for an app store version experiment](./delete-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Delete localized metatdata that you configured for an App Store Version experiment treatment.
- [List related placements](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-placements.md)
  List the placements for an App Store version experiment treatment localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-placements)*