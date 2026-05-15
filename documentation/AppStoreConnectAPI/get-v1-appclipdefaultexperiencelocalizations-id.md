# Read Localization Information of a Default App Clip Experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get localized metadata that appears on the App Clip card of a specific default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}`

## Parameters

- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each Default App Clip Experience Localizations resource returned by the response.
- `fields[appClipHeaderImages]` ([string]): Additional fields to include for each Default App Clip Experience Localizations resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appClipDefaultExperiences]` ([string])

## See Also

- [Read App Clip Card Image Information for a Localized Default App Clip Experience](get-v1-appclipdefaultexperiencelocalizations-_id_-appclipheaderimage.md)
  Get the image that appears on the App Clip card, specific to a locale, for a default App Clip experience.
- [GET /v1/appClipDefaultExperienceLocalizations/{id}/relationships/appClipHeaderImage](get-v1-appclipdefaultexperiencelocalizations-_id_-relationships-appclipheaderimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiencelocalizations-_id_)*