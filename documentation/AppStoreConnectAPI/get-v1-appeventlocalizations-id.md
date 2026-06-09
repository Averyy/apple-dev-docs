# Read app event localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific app event localization.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventLocalizations/{id}`

## Parameters

- `fields[appEventLocalizations]` ([string]): Additional fields to include for each app event localization resource returned by the response.
- `fields[appEventScreenshots]` ([string]): Additional fields to include for each app event screenshot resource returned by the response.
- `fields[appEventVideoClips]` ([string]): Additional fields to include for each app event video clip resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appEventScreenshots]` (integer): The maximum number of related app event screenshots resources to return.
- `limit[appEventVideoClips]` (integer): The maximum number of related app event video clips resources to return.
- `fields[appEvents]` ([string])

## See Also

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
- [Delete an app event localization](delete-v1-appeventlocalizations-_id_.md)
  Delete localized metadata that you configured for an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventlocalizations-_id_)*