# List all default app clip experiences for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all default App Clip experiences for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/appClipDefaultExperiences`

## Parameters

- `exists[releaseWithAppStoreVersion]` (boolean): Filter the returned default App Clip experiences to include only those that have (true) or don’t have (false) a related App Store version.
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each default App Clip experience localization resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of default App Clip experience resources to return.
- `limit[appClipDefaultExperienceLocalizations]` (integer): The maximum number of related default App Clip experience localizations resources to return.
- `fields[appClips]` ([string]): Additional fields to include for each app clip resource returned by the response.
- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each app clip App Store review detail resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.

## See Also

- [List all advanced app clip experiences for an app clip](get-v1-appclips-_id_-appclipadvancedexperiences.md)
  Get all advanced App Clip experiences for an App Clip.
- [List App Clip advanced experience IDs for an App Clip](get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [List default experience IDs for an App Clip](get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-appclipdefaultexperiences)*