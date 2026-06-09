# Modify the related app store version for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the relationship between a default App Clip experience and an App Store Version.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Default App Clip Experiences resource.

## Request Body

The request body you use to update the relationship between a default App Clip experience and an App Store version.

## See Also

- [Create a default app clip experience](post-v1-appclipdefaultexperiences.md)
  Configure a new default App Clip experience.
- [Modify a default app clip experience](patch-v1-appclipdefaultexperiences-_id_.md)
  Update a default App Clip experience.
- [Delete a default app clip experience](delete-v1-appclipdefaultexperiences-_id_.md)
  Delete a specific default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion)*