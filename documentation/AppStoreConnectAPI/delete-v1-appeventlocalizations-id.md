# Delete an app event localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete localized metadata that you configured for an in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appEventLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event localization resource ID from the [`List all localizations for an in-app event`](get-v1-appevents-_id_-localizations.md) response.

## See Also

- [Read app event localization information](get-v1-appeventlocalizations-_id_.md)
  Get information about a specific app event localization.
- [List all video clips for an app event localization](get-v1-appeventlocalizations-_id_-appeventvideoclips.md)
  Get a list of video clips for a specific app event localization.
- [List app event video clip IDs for an app event localization](get-v1-appeventlocalizations-_id_-relationships-appeventvideoclips.md)
- [List all screenshots for an app event localization](get-v1-appeventlocalizations-_id_-appeventscreenshots.md)
  Get a list of screenshots for a specific app event localization.
- [List app event screenshot IDs for an app event localization](get-v1-appeventlocalizations-_id_-relationships-appeventscreenshots.md)
- [Modify an app event localization](patch-v1-appeventlocalizations-_id_.md)
  Update the localized metadata for a specific in-app event.
- [Create an app event localization](post-v1-appeventlocalizations.md)
  Add a new localization for an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appeventlocalizations-_id_)*