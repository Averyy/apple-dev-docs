# Delete an app event screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific screenshot from an in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appEventScreenshots/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event screenshot resource ID from the [`List all screenshots for an app event localization`](get-v1-appeventlocalizations-_id_-appeventscreenshots.md) response.

## See Also

- [List the Images for an In-App Event](get-v1-appeventscreenshots-_id_.md)
- [Update an app event screenshot](patch-v1-appeventscreenshots-_id_.md)
- [Create an app event screenshot](post-v1-appeventscreenshots.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appeventscreenshots-_id_)*