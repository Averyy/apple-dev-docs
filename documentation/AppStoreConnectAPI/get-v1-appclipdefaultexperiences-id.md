# Read default app clip experience information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}`

## Parameters

- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each app clip App Store review detail resource returned by the response.
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each default App Clip experience localization resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appClipDefaultExperienceLocalizations]` (integer): The maximum number of related default App Clip experience localizations resources to return.
- `fields[appClips]` ([string])

## See Also

- [Read the app store review detail for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md)
  Get App Store Review details for a specific default App Clip experience.
- [Get the App Store review detail ID for an App Clip default experience](get-v1-appclipdefaultexperiences-_id_-relationships-appclipappstorereviewdetail.md)
- [Read localization information for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md)
  Get localized metadata that appears on the App Clip card for a specific default App Clip experience.
- [List localization IDs for an App Clip default experience](get-v1-appclipdefaultexperiences-_id_-relationships-appclipdefaultexperiencelocalizations.md)
- [Read app store version information for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-releasewithappstoreversion.md)
  Get App Store Version information for a default App Clip experience.
- [Get the app store versions resource id for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Get IDs for App Store Versions related to a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiences-_id_)*