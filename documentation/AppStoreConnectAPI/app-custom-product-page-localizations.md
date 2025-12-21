# App Custom Product Page Localizations

**Framework**: App Store Connect API

Create and update version-specific, localized metadata for custom product pages.

#### Overview

Use `appCustomProductPageLocalizations` to manage app preview sets and app screenshot sets for different languages for your custom product page.

You can update the Promotional Text for your custom product page localization at any time.

## Topics

### Managing localizations
- [List custom product pages localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Read custom product page localization information](get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [Create a custom product page localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify custom product page localization information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [Delete an app custom product page localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.
### Getting preview set information
- [List app preview sets for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-apppreviewsets.md)
  List the app preview sets for a specific custom product page localization.
- [List app preview set Ids for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-apppreviewsets.md)
  List the app preview set IDs for a specific custom product page localization.
### Getting screenshot information
- [List app screenshot sets for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-appscreenshotsets.md)
  List the app screenshot sets for a specific custom product page localization.
- [List app screenshot sets Ids for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-appscreenshotsets.md)
  List the app screenshot set IDs for a specific custom product page localization.
### Managing search keywords
- [List app preview sets for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-searchkeywords.md)
  List the app preview sets for a specific custom product page localization.
- [List all search keywords for a customer product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a customer product page localization.
- [Add a search keyword to a custom product page localization](post-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Assign one or more search keywords to a specific custom product page localization.
- [Remove a search keyword from a custom product page localization](delete-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Unassign a search keyword from a specific custom product page localization.
### Objects
- [object AppKeyword](appkeyword.md)
  The data structure that represents an app keyword resource.
- [object AppKeywordsResponse](appkeywordsresponse.md)
  A response that contains a list of app keywords response resources.
- [object AppCustomProductPageLocalization](appcustomproductpagelocalization.md)
  The data structure that represents an app custom product page localization resource.
- [object AppCustomProductPageLocalizationCreateRequest](appcustomproductpagelocalizationcreaterequest.md)
  The request body you use to create an app custom product page localization.
- [object AppCustomProductPageLocalizationInlineCreate](appcustomproductpagelocalizationinlinecreate.md)
  The data structure that represents an app custom product page localization inline creates resource.
- [object AppCustomProductPageLocalizationResponse](appcustomproductpagelocalizationresponse.md)
  A response that contains a single app custom product page resource.
- [object AppCustomProductPageLocalizationUpdateRequest](appcustomproductpagelocalizationupdaterequest.md)
  The request body you use to update an app custom product page localization.
- [object AppCustomProductPageLocalizationsResponse](appcustomproductpagelocalizationsresponse.md)
  A response that contains a list of alternative distribution package variant resources.
- [object AppCustomProductPageLocalizationAppPreviewSetsLinkagesResponse](appcustomproductpagelocalizationapppreviewsetslinkagesresponse.md)
  A response that contains a list of IDs of related resources.
- [object AppCustomProductPageLocalizationAppScreenshotSetsLinkagesResponse](appcustomproductpagelocalizationappscreenshotsetslinkagesresponse.md)
  A response that contains a list of IDs of related resources.
- [object AppCustomProductPageLocalizationSearchKeywordsLinkagesRequest](appcustomproductpagelocalizationsearchkeywordslinkagesrequest.md)
  The request body you use to create a relationship between a custom product page localization and a search keyword.
- [object AppCustomProductPageLocalizationSearchKeywordsLinkagesResponse](appcustomproductpagelocalizationsearchkeywordslinkagesresponse.md)
  A response that contains a list of IDs of related resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-custom-product-page-localizations)*