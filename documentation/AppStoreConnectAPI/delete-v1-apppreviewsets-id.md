# Delete an app preview set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app preview set and all of its previews.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview set resource ID from the [`List all app preview sets for an app store version localization`](get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md) response.

## See Also

- [Create an app preview set](post-v1-apppreviewsets.md)
  Add a new app preview set to an App Store version localization for a specific app preview type and display size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-apppreviewsets-_id_)*