# Read app store version experiment treatment localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific App Store version experiment treatment localization.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatmentLocalizations/{id}`

## Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.
- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appPreviewSets]` (integer): The maximum number of related app preview set resources to return.
- `limit[appScreenshotSets]` (integer): The maximum number of related app screenshot set resources to return.
- `fields[appStoreVersionExperimentTreatments]` ([string])

## See Also

- [List all screenshot sets for an experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-appscreenshotsets.md)
  Get a list of screenshot sets for a specific App Store version experiment treatment localization.
- [List all preview sets for an experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-apppreviewsets.md)
  Get a list of preview sets for a specific App Store version experiment treatment localization.
- [List preview set IDs for an App Store version experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-appscreenshotsets.md)
- [Create an app store version experiment treatment localization](post-v1-appstoreversionexperimenttreatmentlocalizations.md)
  Add a new localization for an App Store version experiment treatment.
- [Delete a treatment localization for an app store version experiment](delete-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Delete localized metatdata that you configured for an App Store Version experiment treatment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionexperimenttreatmentlocalizations-_id_)*