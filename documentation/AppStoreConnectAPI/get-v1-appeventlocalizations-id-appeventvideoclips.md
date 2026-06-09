# List all video clips for an app event localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of video clips for a specific app event localization.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventLocalizations/{id}/appEventVideoClips`

## Parameters

- `fields[appEventVideoClips]` ([string]): Additional fields to include for each app event video clip resource returned by the response.
- `limit` (integer): The maximum number of app event video clip resources to return.
- `fields[appEventLocalizations]` ([string]): Additional fields to include for each app event localization resource returned by the response.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Read app event localization information](get-v1-appeventlocalizations-_id_.md)
  Get information about a specific app event localization.
- [List app event video clip IDs for an app event localization](get-v1-appeventlocalizations-_id_-relationships-appeventvideoclips.md)
- [List all screenshots for an app event localization](get-v1-appeventlocalizations-_id_-appeventscreenshots.md)
  Get a list of screenshots for a specific app event localization.
- [List app event screenshot IDs for an app event localization](get-v1-appeventlocalizations-_id_-relationships-appeventscreenshots.md)
- [Modify an app event localization](patch-v1-appeventlocalizations-_id_.md)
  Update the localized metadata for a specific in-app event.
- [Create an app event localization](post-v1-appeventlocalizations.md)
  Add a new localization for an in-app event.
- [Delete an app event localization](delete-v1-appeventlocalizations-_id_.md)
  Delete localized metadata that you configured for an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventlocalizations-_id_-appeventvideoclips)*