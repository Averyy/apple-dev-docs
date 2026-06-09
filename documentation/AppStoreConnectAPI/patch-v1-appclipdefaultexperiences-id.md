# Modify a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience resource ID from the [`List all default app clip experiences for an app clip`](get-v1-appclips-_id_-appclipdefaultexperiences.md) response.

## Request Body

The request body you use to update a default App Clip experience.

## See Also

- [Create a default app clip experience](post-v1-appclipdefaultexperiences.md)
  Configure a new default App Clip experience.
- [Modify the related app store version for a default app clip experience](patch-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Update the relationship between a default App Clip experience and an App Store Version.
- [Delete a default app clip experience](delete-v1-appclipdefaultexperiences-_id_.md)
  Delete a specific default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipdefaultexperiences-_id_)*