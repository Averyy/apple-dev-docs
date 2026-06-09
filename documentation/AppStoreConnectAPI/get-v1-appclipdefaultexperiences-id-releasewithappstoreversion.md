# Read app store version information for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get App Store Version information for a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}/releaseWithAppStoreVersion`

## Parameters

- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appStoreVersionLocalizations]` (integer): The maximum number of related App Store version localizations resources to return.
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.
- `limit[appStoreVersionExperiments]` (integer): The maximum number of related App Store version experiments resources to return.
- `fields[appStoreVersionSubmissions]` ([string]): Additional fields to include for each App Store version submission resource returned by the response.
- `fields[appStoreReviewDetails]` ([string]): Additional fields to include for each App Store review detail resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[routingAppCoverages]` ([string]): Additional fields to include for each routing app coverage resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.
- `fields[appStoreVersionPhasedReleases]` ([string]): Additional fields to include for each App Store version phased release resource returned by the response.
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.
- `limit[appStoreVersionExperimentsV2]` (integer): The maximum number of related App Store version experiments (v2) resources to return.
- `fields[alternativeDistributionPackages]` ([string]): Additional fields to include for each alternative distribution package resource returned by the response.
- `fields[gameCenterAppVersions]` ([string])

## See Also

- [Read default app clip experience information](get-v1-appclipdefaultexperiences-_id_.md)
  Get a specific default App Clip experience.
- [Read the app store review detail for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md)
  Get App Store Review details for a specific default App Clip experience.
- [Get the App Store review detail ID for an App Clip default experience](get-v1-appclipdefaultexperiences-_id_-relationships-appclipappstorereviewdetail.md)
- [Read localization information for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md)
  Get localized metadata that appears on the App Clip card for a specific default App Clip experience.
- [List localization IDs for an App Clip default experience](get-v1-appclipdefaultexperiences-_id_-relationships-appclipdefaultexperiencelocalizations.md)
- [Get the app store versions resource id for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Get IDs for App Store Versions related to a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiences-_id_-releasewithappstoreversion)*