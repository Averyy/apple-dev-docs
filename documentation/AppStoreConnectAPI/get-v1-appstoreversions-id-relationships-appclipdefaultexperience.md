# Get the default app clip experiences resource id for an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the ID of an app’s related default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/relationships/appClipDefaultExperience`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the App Store Versions resource.

## See Also

- [Get the default app clip experience for an app store version](get-v1-appstoreversions-_id_-appclipdefaultexperience.md)
  Get the default App Clip experience for an App Store version of your app.
- [Modify the default app clip experience of an app store version](patch-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Update the relationship between an App Store version and a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-relationships-appclipdefaultexperience)*