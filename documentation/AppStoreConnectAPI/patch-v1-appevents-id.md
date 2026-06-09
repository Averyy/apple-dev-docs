# Modify an in-app event

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the metadata for a specific in-app event.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appEvents/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event resource ID from the [`List all in-app events for an app`](get-v1-apps-_id_-appevents.md) response.

## See Also

- [Read In-App Event Information](get-v1-appevents-_id_.md)
  Get information about a specific in-app event.
- [List all localizations for an in-app event](get-v1-appevents-_id_-localizations.md)
  Get a list of all localizations for a specific in-app event.
- [List localization IDs for an app event](get-v1-appevents-_id_-relationships-localizations.md)
- [List all in-app events for an app](get-v1-apps-_id_-appevents.md)
  Get a list of in-app events for a specific app.
- [Create an in-app event](post-v1-appevents.md)
  Create a new in-app event for your app.
- [Delete an app event](delete-v1-appevents-_id_.md)
  Delete an in-app event and its related metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appevents-_id_)*