# Delete a Default App Clip Experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Default App Clip Experiences resource.

## See Also

- [Create a Default App Clip Experience](post-v1-appclipdefaultexperiences.md)
  Configure a new default App Clip experience.
- [Modify a Default App Clip Experience](patch-v1-appclipdefaultexperiences-_id_.md)
  Update a default App Clip experience.
- [Modify the Related App Store Version for a Default App Clip Experience](patch-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Update the relationship between a default App Clip experience and an App Store Version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appclipdefaultexperiences-_id_)*