# Delete a default app clip experience localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete localized metadata that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience localization resource ID from the [`Read localization information for a default app clip experience`](get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md) response.

## See Also

- [Create the localized metadata for a default app clip experience](post-v1-appclipdefaultexperiencelocalizations.md)
  Provide localized metadata that appears on the App Clip card of a default App Clip experience.
- [Modify the localization for a default app clip experience](patch-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Update localized metadata for a specific default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appclipdefaultexperiencelocalizations-_id_)*