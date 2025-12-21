# App Info Localizations

**Framework**: App Store Connect API

Manage the app metadata that is localized and appears on the App Store.

#### Overview

`appInfoLocalizations` represent your app’s localized metadata that is displayed in the App Store. You can create, read, update, and remove the localized metadata. It includes the following attributes for each localization:

- Locale
- Name
- Subtitle
- Privacy policy URL
- Privacy policy text (for tvOS apps)

You can update localized metadata when your app is in an editable state. For more information about the metadata, see [`Localize App Store information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-store-information). For a list of supported languages, see [`App Store localizations`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-store-localizations).

> **Note**:  The languages you add to an `appInfoLocalizations` resource only affect your app’s metadata. To add languages to your app’s binary, see [`What is localization`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/deve2bc11fab).

## Topics

### Essentials
- [Managing metadata in your app by using locale shortcodes](managing-metadata-in-your-app-by-using-locale-shortcodes.md)
  Optimize your app’s user experience by adding localized metadata with App Store Connect API.
### Reading App Localization Information
- [List All App Info Localizations for an App Info](get-v1-appinfos-_id_-appinfolocalizations.md)
  Get a list of localized, app-level information for an app.
- [Read App Info Localization Information](get-v1-appinfolocalizations-_id_.md)
  Read localized app-level information.
### Creating, Modifying, and Deleting Localized App Information
- [Create an App Info Localization](post-v1-appinfolocalizations.md)
  Add app-level localized information for a new locale.
- [Modify an App Info Localization](patch-v1-appinfolocalizations-_id_.md)
  Modify localized app-level information for a particular language.
- [Delete an App Info Localization](delete-v1-appinfolocalizations-_id_.md)
  Delete an app information localization that is associated with an app.
### Objects
- [object AppInfoLocalization](appinfolocalization.md)
  The data structure that represent an App Info Localizations resource.
- [object AppInfoLocalizationCreateRequest](appinfolocalizationcreaterequest.md)
  The request body you use to create an App Info Localization.
- [object AppInfoLocalizationResponse](appinfolocalizationresponse.md)
  A response that contains a single App Info Localizations resource.
- [object AppInfoLocalizationUpdateRequest](appinfolocalizationupdaterequest.md)
  The request body you use to update an App Info Localization.
- [object AppInfoLocalizationsResponse](appinfolocalizationsresponse.md)
  A response that contains a list of AppInfoLocalizations resources.

## See Also

- [App Infos](app-infos.md)
  Manage or read the app metadata that applies across all versions of your app.
- [App Store Versions](app-store-versions.md)
  Manage versions of your app that are available in App Store.
- [App Store Version Localizations](app-store-version-localizations.md)
  Create and maintain version-specific App Store metadata that’s localized.
- [App tags](app-tags.md)
  Read or modify Apple created app tags.
- [Routing App Coverages](routing-app-coverages.md)
  Manage geographic coverage files for apps that use location to provide routing information.
- [Accessibility declarations](accessibility-declarations.md)
  Manage accessibility metadata for your apps per device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-info-localizations)*