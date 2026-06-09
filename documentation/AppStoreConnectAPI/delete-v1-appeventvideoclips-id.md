# Delete an app event video clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific video clip from an in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appEventVideoClips/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event video clip resource ID from the [`List all video clips for an app event localization`](get-v1-appeventlocalizations-_id_-appeventvideoclips.md) response.

## See Also

- [Read app event video clip information](get-v1-appeventvideoclips-_id_.md)
  Get information about a specific video clip for an in-app event.
- [Modify an app event video clip](patch-v1-appeventvideoclips-_id_.md)
  Commit an uploaded video clip asset for an in-app event.
- [Create an app event video clip](post-v1-appeventvideoclips.md)
  Reserve a video clip asset for an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appeventvideoclips-_id_)*