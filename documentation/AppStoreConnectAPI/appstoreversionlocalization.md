# AppStoreVersionLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Store Version Localizations resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreVersionLocalization
```

## Topics

### Objects
- [object AppStoreVersionLocalization.Attributes](appstoreversionlocalization/attributes-data.dictionary.md)
  Attributes that describe an App Store Version Localizations resource.
- [object AppStoreVersionLocalization.Relationships](appstoreversionlocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppStoreVersionLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppStoreVersionLocalization.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppStoreVersionLocalizationCreateRequest](appstoreversionlocalizationcreaterequest.md)
  The request body you use to create an App Store Version Localization.
- [object AppStoreVersionLocalizationResponse](appstoreversionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized App Store version entry.
- [object AppStoreVersionLocalizationsResponse](appstoreversionlocalizationsresponse.md)
  The response body for endpoints that list localized App Store version entries.
- [object AppStoreVersionLocalizationUpdateRequest](appstoreversionlocalizationupdaterequest.md)
  The request body you use to update an App Store Version Localization
- [object AppStoreVersionLocalizationSearchKeywordsLinkagesRequest](appstoreversionlocalizationsearchkeywordslinkagesrequest.md)
  The request body for updating the list of search keywords linked to an App Store version localization.
- [object AppStoreVersionLocalizationSearchKeywordsLinkagesResponse](appstoreversionlocalizationsearchkeywordslinkagesresponse.md)
  A response containing the resource identifiers of search keywords linked to an App Store version localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionlocalization)*