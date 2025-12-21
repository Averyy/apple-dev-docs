# App Store Version Localizations

**Framework**: App Store Connect API

Create and maintain version-specific App Store metadata that’s localized.

#### Overview

Use `appStoreVersionLocalizations` to create and maintain your App Store metadata in different languages. This resource includes the following attributes:

- Locale
- Description
- Keywords
- Marketing URL
- Promotional Text
- Support URL
- What’s New Text

You can update the Promotional Text for your version at any time. Update other attributes when your app is in an editable state. For information about required, localized, and editable metadata, see [`Required, localized, and editable properties`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/required-localizable-and-editable-properties).

## Topics

### Getting Version Localizations
- [List All App Store Version Localizations for an App Store Version](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md)
  Get a list of localized, version-level information about an app, for all locales.
- [Read App Store Version Localization Information](get-v1-appstoreversionlocalizations-_id_.md)
  Read localized version-level information.
### Creating, Modifying, and Deleting Version Localizations
- [Create an App Store Version Localization](post-v1-appstoreversionlocalizations.md)
  Add localized version-level information for a new locale.
- [Modify an App Store Version Localization](patch-v1-appstoreversionlocalizations-_id_.md)
  Modify localized version-level information for a particular language.
- [Delete an App Store Version Localization](delete-v1-appstoreversionlocalizations-_id_.md)
  Delete a language from your version metadata.
### Getting Information from a Localization
- [List All App Preview Sets for an App Store Version Localization](get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md)
  List all app preview sets for a specific localization.
- [List All App Screenshot Sets for an App Store Version Localization](get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md)
  List all screenshot sets for a specific localization.
- [GET /v1/appStoreVersionLocalizations/{id}/relationships/appPreviewSets](get-v1-appstoreversionlocalizations-_id_-relationships-apppreviewsets.md)
- [GET /v1/appStoreVersionLocalizations/{id}/relationships/appScreenshotSets](get-v1-appstoreversionlocalizations-_id_-relationships-appscreenshotsets.md)
### Search Keywords
- [GET /v1/appStoreVersionLocalizations/{id}/searchKeywords](get-v1-appstoreversionlocalizations-_id_-searchkeywords.md)
- [GET /v1/appStoreVersionLocalizations/{id}/relationships/searchKeywords](get-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
- [POST /v1/appStoreVersionLocalizations/{id}/relationships/searchKeywords](post-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
- [DELETE /v1/appStoreVersionLocalizations/{id}/relationships/searchKeywords](delete-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
### Objects
- [object AppStoreVersionLocalization](appstoreversionlocalization.md)
  The data structure that represent an App Store Version Localizations resource.
- [object AppStoreVersionLocalizationCreateRequest](appstoreversionlocalizationcreaterequest.md)
  The request body you use to create an App Store Version Localization.
- [object AppStoreVersionLocalizationResponse](appstoreversionlocalizationresponse.md)
  A response that contains a single App Store Version Localizations resource.
- [object AppStoreVersionLocalizationsResponse](appstoreversionlocalizationsresponse.md)
  A response that contains a list of App Store Version Localization resources.
- [object AppStoreVersionLocalizationUpdateRequest](appstoreversionlocalizationupdaterequest.md)
  The request body you use to update an App Store Version Localization
- [object AppStoreVersionLocalizationSearchKeywordsLinkagesRequest](appstoreversionlocalizationsearchkeywordslinkagesrequest.md)
- [object AppStoreVersionLocalizationSearchKeywordsLinkagesResponse](appstoreversionlocalizationsearchkeywordslinkagesresponse.md)

## See Also

- [App Infos](app-infos.md)
  Manage or read the app metadata that applies across all versions of your app.
- [App Info Localizations](app-info-localizations.md)
  Manage the app metadata that is localized and appears on the App Store.
- [App Store Versions](app-store-versions.md)
  Manage versions of your app that are available in App Store.
- [App tags](app-tags.md)
  Read or modify Apple created app tags.
- [Routing App Coverages](routing-app-coverages.md)
  Manage geographic coverage files for apps that use location to provide routing information.
- [Accessibility declarations](accessibility-declarations.md)
  Manage accessibility metadata for your apps per device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-version-localizations)*