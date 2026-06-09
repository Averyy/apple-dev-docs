# Get the app store versions resource id for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get IDs for App Store Versions related to a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Default App Clip Experiences resource.

## See Also

- [Read default app clip experience information](get-v1-appclipdefaultexperiences-_id_.md)
  Get a specific default App Clip experience.
- [Read the app store review detail for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md)
  Get App Store Review details for a specific default App Clip experience.
- [Get the App Store review detail ID for an App Clip default experience](get-v1-appclipdefaultexperiences-_id_-relationships-appclipappstorereviewdetail.md)
- [Read localization information for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md)
  Get localized metadata that appears on the App Clip card for a specific default App Clip experience.
- [List localization IDs for an App Clip default experience](get-v1-appclipdefaultexperiences-_id_-relationships-appclipdefaultexperiencelocalizations.md)
- [Read app store version information for a default app clip experience](get-v1-appclipdefaultexperiences-_id_-releasewithappstoreversion.md)
  Get App Store Version information for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion)*