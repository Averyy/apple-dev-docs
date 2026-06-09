# List the Images for an In-App Event

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventScreenshots/{id}`

## Parameters

- `fields[appEventScreenshots]` ([string]): Additional fields to include for each app event screenshot resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appEventLocalizations]` ([string])

## See Also

- [Update an app event screenshot](patch-v1-appeventscreenshots-_id_.md)
- [Create an app event screenshot](post-v1-appeventscreenshots.md)
- [Delete an app event screenshot](delete-v1-appeventscreenshots-_id_.md)
  Delete a specific screenshot from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventscreenshots-_id_)*