# AppEvent

**Framework**: App Store Connect API  
**Kind**: dictionary

A time-limited promotional or informational event for an app, displayed to customers on the App Store product page.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEvent
```

## Topics

### Objects
- [object AppEvent.Attributes](appevent/attributes-data.dictionary.md)
  The attributes that describe an In-App event.
- [object AppEvent.Relationships](appevent/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppEvent.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppEvent.Relationships)
- `type` (string) *(required)*

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appevent)*