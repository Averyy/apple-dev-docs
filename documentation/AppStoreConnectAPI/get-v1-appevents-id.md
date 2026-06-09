# Read In-App Event Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEvents/{id}`

## Parameters

- `fields[appEventLocalizations]` ([string]): Additional fields to include for each app event localization resource returned by the response.
- `fields[appEvents]` ([string]): Additional fields to include for each app event resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.

## See Also

- [List all localizations for an in-app event](get-v1-appevents-_id_-localizations.md)
  Get a list of all localizations for a specific in-app event.
- [List localization IDs for an app event](get-v1-appevents-_id_-relationships-localizations.md)
- [List all in-app events for an app](get-v1-apps-_id_-appevents.md)
  Get a list of in-app events for a specific app.
- [Modify an in-app event](patch-v1-appevents-_id_.md)
  Update the metadata for a specific in-app event.
- [Create an in-app event](post-v1-appevents.md)
  Create a new in-app event for your app.
- [Delete an app event](delete-v1-appevents-_id_.md)
  Delete an in-app event and its related metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appevents-_id_)*