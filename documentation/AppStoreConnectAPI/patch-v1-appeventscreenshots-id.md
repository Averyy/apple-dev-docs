# Update an app event screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appEventScreenshots/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event screenshot resource ID from the [`List all screenshots for an app event localization`](get-v1-appeventlocalizations-_id_-appeventscreenshots.md) response.

## See Also

- [List the Images for an In-App Event](get-v1-appeventscreenshots-_id_.md)
- [Create an app event screenshot](post-v1-appeventscreenshots.md)
- [Delete an app event screenshot](delete-v1-appeventscreenshots-_id_.md)
  Delete a specific screenshot from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appeventscreenshots-_id_)*