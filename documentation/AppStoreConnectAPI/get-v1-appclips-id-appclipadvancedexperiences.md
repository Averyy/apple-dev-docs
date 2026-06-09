# List all advanced app clip experiences for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all advanced App Clip experiences for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/appClipAdvancedExperiences`

## Parameters

- `fields[appClipAdvancedExperienceLocalizations]` ([string]): Additional fields to include for each advanced App Clip experience localization resource returned by the response.
- `fields[appClipAdvancedExperiences]` ([string]): Additional fields to include for each advanced App Clip experience resource returned by the response.
- `filter[action]` ([string]): Filter the returned advanced App Clip experiences using the verb that appears on the App Clip card.
- `filter[placeStatus]` ([string]): Filter the returned advanced App Clip experiences using the status of the associated place in Apple Maps.
- `filter[status]` ([string]): Filter the returned advanced App Clip experiences using their status.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of advanced App Clip experience resources to return.
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.
- `fields[appClips]` ([string]): Additional fields to include for each app clip resource returned by the response.
- `fields[appClipAdvancedExperienceImages]` ([string]): Additional fields to include for each advanced App Clip experience image resource returned by the response.

## See Also

- [List all default app clip experiences for an app clip](get-v1-appclips-_id_-appclipdefaultexperiences.md)
  Get all default App Clip experiences for an App Clip.
- [List App Clip advanced experience IDs for an App Clip](get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [List default experience IDs for an App Clip](get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-appclipadvancedexperiences)*