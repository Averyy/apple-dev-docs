# Read app clip card image information for a localized default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the image that appears on the App Clip card, specific to a locale, for a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}/appClipHeaderImage`

## Parameters

- `fields[appClipHeaderImages]` ([string]): Additional fields to include for each app clip header image resource returned by the response.
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each default App Clip experience localization resource returned by the response.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Read localization information of a default app clip experience](get-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Get localized metadata that appears on the App Clip card of a specific default App Clip experience.
- [Get the header image ID for an App Clip default experience localization](get-v1-appclipdefaultexperiencelocalizations-_id_-relationships-appclipheaderimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiencelocalizations-_id_-appclipheaderimage)*