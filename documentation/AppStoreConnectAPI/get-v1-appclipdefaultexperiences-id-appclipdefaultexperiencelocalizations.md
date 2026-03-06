# Read Localization Information for a Default App Clip Experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get localized metadata that appears on the App Clip card for a specific default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}/appClipDefaultExperienceLocalizations`

## Parameters

- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each Default App Clip Experience Localizations resource returned by the response.
- `filter[locale]` ([string]): Filter the returned default App Clip experience localizations using the experience’s locale.
- `limit` (integer): The number of Default App Clip Experience Localizations resources to return.
- `include` ([string])
- `fields[appClipDefaultExperiences]` ([string])
- `fields[appClipHeaderImages]` ([string])

## See Also

- [Read Default App Clip Experience Information](get-v1-appclipdefaultexperiences-_id_.md)
  Get a specific default App Clip experience.
- [Read the App Store Review Detail for a Default App Clip Experience](get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md)
  Get App Store Review details for a specific default App Clip experience.
- [GET /v1/appClipDefaultExperiences/{id}/relationships/appClipAppStoreReviewDetail](get-v1-appclipdefaultexperiences-_id_-relationships-appclipappstorereviewdetail.md)
- [GET /v1/appClipDefaultExperiences/{id}/relationships/appClipDefaultExperienceLocalizations](get-v1-appclipdefaultexperiences-_id_-relationships-appclipdefaultexperiencelocalizations.md)
- [Read App Store Version Information for a Default App Clip Experience](get-v1-appclipdefaultexperiences-_id_-releasewithappstoreversion.md)
  Get App Store Version information for a default App Clip experience.
- [Get the App Store Versions Resource ID for a Default App Clip Experience](get-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Get IDs for App Store Versions related to a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations)*