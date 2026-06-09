# AppEventsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list in-app events for an app.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventsResponse
```

## Properties

- `data` ([AppEvent]) *(required)*
- `included` ([AppEventLocalization])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppEvent](appevent.md)
  A time-limited promotional or informational event for an app, displayed to customers on the App Store product page.
- [object AppEventCreateRequest](appeventcreaterequest.md)
  The request body you use to create an app event.
- [object AppEventUpdateRequest](appeventupdaterequest.md)
  The request body you use to update an app event update request.
- [object AppEventResponse](appeventresponse.md)
  The response body for endpoints that create, read, or modify an in-app event.
- [type AppEventAssetType](appeventassettype.md)
  A string that represents the type of asset for an app event.
- [object AppEventLocalizationsLinkagesResponse](appeventlocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventsresponse)*