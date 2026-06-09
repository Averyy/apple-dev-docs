# Delete a treatment for an app store version experiment

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete metadata that you configured for an App Store Version experiment.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatments/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version experiment treatment resource ID from the [`List all treatments for an app store experiment v1`](get-v1-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md) response.

## See Also

- [List all treatments for an app store experiment](get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an app store version experiment](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [Read app store version experiment treatment information](get-v1-appstoreversionexperimenttreatments-_id_.md)
  Get information about a specific App Store version experiment treatment.
- [List all localizations for an app store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md)
  Get a list of all localizations for a specific App Store version experiment treatment.
- [List localization IDs for an App Store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-relationships-appstoreversionexperimenttreatmentlocalizations.md)
- [Modify an app store version experiment treatment](patch-v1-appstoreversionexperimenttreatments-_id_.md)
  Update the name and app icon name for a specific App Store version experiment.
- [Create an app store version experiment treatment](post-v1-appstoreversionexperimenttreatments.md)
  Add a new treatment to an App Store version experiment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversionexperimenttreatments-_id_)*