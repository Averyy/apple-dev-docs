# AppCustomProductPageLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized promotional text, keywords, and screenshots for a custom App Store product page in a specific language.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppCustomProductPageLocalization
```

## Topics

### Objects
- [object AppCustomProductPageLocalization.Attributes](appcustomproductpagelocalization/attributes-data.dictionary.md)
- [object AppCustomProductPageLocalization.Relationships](appcustomproductpagelocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppCustomProductPageLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppCustomProductPageLocalization.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppKeyword](appkeyword.md)
  A search keyword associated with an App Store listing or custom product page for discoverability.
- [object AppKeywordsResponse](appkeywordsresponse.md)
  A response containing a list of search keywords for an App Store listing.
- [object AppCustomProductPageLocalizationCreateRequest](appcustomproductpagelocalizationcreaterequest.md)
  The request body you use to create an app custom product page localization.
- [object AppCustomProductPageLocalizationInlineCreate](appcustomproductpagelocalizationinlinecreate.md)
  An inline object for specifying a language-specific localization when creating a custom product page version.
- [object AppCustomProductPageLocalizationResponse](appcustomproductpagelocalizationresponse.md)
  A response containing a single localization for a custom App Store product page.
- [object AppCustomProductPageLocalizationUpdateRequest](appcustomproductpagelocalizationupdaterequest.md)
  The request body you use to update an app custom product page localization.
- [object AppCustomProductPageLocalizationsResponse](appcustomproductpagelocalizationsresponse.md)
  A response containing a list of localizations for a custom App Store product page.
- [object AppCustomProductPageLocalizationAppPreviewSetsLinkagesResponse](appcustomproductpagelocalizationapppreviewsetslinkagesresponse.md)
  A response containing the resource identifiers of app preview sets associated with a custom product page localization.
- [object AppCustomProductPageLocalizationAppScreenshotSetsLinkagesResponse](appcustomproductpagelocalizationappscreenshotsetslinkagesresponse.md)
  A response containing the resource identifiers of screenshot sets associated with a custom product page localization.
- [object AppCustomProductPageLocalizationSearchKeywordsLinkagesRequest](appcustomproductpagelocalizationsearchkeywordslinkagesrequest.md)
  The request body you use to create a relationship between a custom product page localization and a search keyword.
- [object AppCustomProductPageLocalizationSearchKeywordsLinkagesResponse](appcustomproductpagelocalizationsearchkeywordslinkagesresponse.md)
  A response containing the resource identifiers of search keywords associated with a custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcustomproductpagelocalization)*