# Delete a treatment localization for an app store version experiment

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete localized metatdata that you configured for an App Store Version experiment treatment.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatmentLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version experiment treatment localization resource ID from the [`List all localizations for an app store version experiment treatment`](./get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
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
- [List related placements](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-placements.md)
  List the placements for an App Store version experiment treatment localization.
- [List the placement IDs for an App Store version experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific App Store version experiment treatment localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversionexperimenttreatmentlocalizations-_id_)*