# AppStoreVersionLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized App Store version entries.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreVersionLocalizationsResponse
```

## Properties

- `data` ([AppStoreVersionLocalization]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppStoreVersionLocalization](appstoreversionlocalization.md)
  The data structure that represent an App Store Version Localizations resource.
- [object AppStoreVersionLocalizationCreateRequest](appstoreversionlocalizationcreaterequest.md)
  The request body you use to create an App Store Version Localization.
- [object AppStoreVersionLocalizationResponse](appstoreversionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized App Store version entry.
- [object AppStoreVersionLocalizationUpdateRequest](appstoreversionlocalizationupdaterequest.md)
  The request body you use to update an App Store Version Localization
- [object AppStoreVersionLocalizationSearchKeywordsLinkagesRequest](appstoreversionlocalizationsearchkeywordslinkagesrequest.md)
  The request body for updating the list of search keywords linked to an App Store version localization.
- [object AppStoreVersionLocalizationSearchKeywordsLinkagesResponse](appstoreversionlocalizationsearchkeywordslinkagesresponse.md)
  A response containing the resource identifiers of search keywords linked to an App Store version localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionlocalizationsresponse)*