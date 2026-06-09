# Read app event video clip information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific video clip for an in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventVideoClips/{id}`

## Parameters

- `fields[appEventVideoClips]` ([string]): Additional fields to include for each app event video clip resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appEventLocalizations]` ([string])

## See Also

- [Modify an app event video clip](patch-v1-appeventvideoclips-_id_.md)
  Commit an uploaded video clip asset for an in-app event.
- [Create an app event video clip](post-v1-appeventvideoclips.md)
  Reserve a video clip asset for an in-app event.
- [Delete an app event video clip](delete-v1-appeventvideoclips-_id_.md)
  Delete a specific video clip from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventvideoclips-_id_)*