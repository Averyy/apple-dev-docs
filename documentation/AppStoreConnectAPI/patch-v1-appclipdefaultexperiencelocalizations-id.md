# Modify the localization for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update localized metadata for a specific default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience localization resource ID from the [`Read localization information for a default app clip experience`](get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md) response.

## Request Body

The request body you use to update a default App Clip experience localization.

## See Also

- [Create the localized metadata for a default app clip experience](post-v1-appclipdefaultexperiencelocalizations.md)
  Provide localized metadata that appears on the App Clip card of a default App Clip experience.
- [Delete a default app clip experience localization](delete-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Delete localized metadata that appears on the App Clip card of a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipdefaultexperiencelocalizations-_id_)*