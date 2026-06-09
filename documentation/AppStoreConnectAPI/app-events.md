# App Events

**Framework**: App Store Connect API

Create, manage, and schedule in-app events for your app.

## Topics

### Endpoints
- [Read In-App Event Information](get-v1-appevents-_id_.md)
  Get information about a specific in-app event.
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
### Objects and types
- [object AppEvent](appevent.md)
  A time-limited promotional or informational event for an app, displayed to customers on the App Store product page.
- [object AppEventCreateRequest](appeventcreaterequest.md)
  The request body you use to create an app event.
- [object AppEventUpdateRequest](appeventupdaterequest.md)
  The request body you use to update an app event update request.
- [object AppEventsResponse](appeventsresponse.md)
  The response body for endpoints that list in-app events for an app.
- [object AppEventResponse](appeventresponse.md)
  The response body for endpoints that create, read, or modify an in-app event.
- [type AppEventAssetType](appeventassettype.md)
  A string that represents the type of asset for an app event.
- [object AppEventLocalizationsLinkagesResponse](appeventlocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-events)*