# List all in-app events for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of in-app events for a specific app.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appEvents`

## Parameters

- `fields[appEventLocalizations]` ([string]): Additional fields to include for each app event localization resource returned by the response.
- `fields[appEvents]` ([string]): Additional fields to include for each app event resource returned by the response.
- `filter[eventState]` ([string]): Filter the returned app events by event state.
- `filter[id]` ([string]): Filter the returned app events by ID.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app event resources to return.
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.

## See Also

- [List app event IDs for an app](get-v1-apps-_id_-relationships-appevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appevents)*