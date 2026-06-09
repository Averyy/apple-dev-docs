# Read app store version experiment treatment information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific App Store version experiment treatment.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/{id}`

## Parameters

- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatments]` ([string]): Additional fields to include for each App Store version experiment treatment resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appStoreVersionExperimentTreatmentLocalizations]` (integer): The maximum number of related App Store version experiment treatment localization resources to return.
- `fields[appStoreVersionExperiments]` ([string])

## See Also

- [List all treatments for an app store experiment](get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an app store version experiment](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [List all localizations for an app store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md)
  Get a list of all localizations for a specific App Store version experiment treatment.
- [List localization IDs for an App Store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-relationships-appstoreversionexperimenttreatmentlocalizations.md)
- [Modify an app store version experiment treatment](patch-v1-appstoreversionexperimenttreatments-_id_.md)
  Update the name and app icon name for a specific App Store version experiment.
- [Create an app store version experiment treatment](post-v1-appstoreversionexperimenttreatments.md)
  Add a new treatment to an App Store version experiment.
- [Delete a treatment for an app store version experiment](delete-v1-appstoreversionexperimenttreatments-_id_.md)
  Delete metadata that you configured for an App Store Version experiment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionexperimenttreatments-_id_)*