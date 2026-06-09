# App tags

**Framework**: App Store Connect API

Read or modify Apple created app tags.

#### Overview

Use the app tag resource to read the tags that Apple applied to your app and remove tags that are not representative of your app. To learn more, see [`Manage app tags`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags).

## Topics

### Reading app tag information
- [List App Tags](get-v1-apps-_id_-apptags.md)
  List all app tags for a specific app.
- [List app tags IDs](get-v1-apps-_id_-relationships-apptags.md)
  List all app tag IDs for a specific app.
- [List territory IDs for an app tag](get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.
- [List Territories for an App Tag](get-v1-apptags-_id_-territories.md)
  List territory availability for a specific app tag.
### Modifying app tag information
- [Modify App Tags](patch-v1-apptags-_id_.md)
  Opt out of app tags for a specific app.
### Objects
- [object AppAppTagsLinkagesResponse](appapptagslinkagesresponse.md)
  A response containing the resource identifiers of tags associated with an app.
- [object AppTag](apptag.md)
  A label used to categorize an app for internal organization or to control which App Store territories feature it.
- [object AppTagResponse](apptagresponse.md)
  A response containing a single app tag.
- [object AppTagsResponse](apptagsresponse.md)
  A response containing a list of tags associated with apps.
- [object AppTagTerritoriesLinkagesResponse](apptagterritorieslinkagesresponse.md)
  A response containing the resource identifiers of territories associated with an app tag.
- [object AppTagUpdateRequest](apptagupdaterequest.md)
  The request body you use to update an app tag update request.

## See Also

- [App Infos](app-infos.md)
  Manage or read the app metadata that applies across all versions of your app.
- [App Info Localizations](app-info-localizations.md)
  Manage the app metadata that is localized and appears on the App Store.
- [App Store Versions](app-store-versions.md)
  Manage versions of your app that are available in App Store.
- [App Store Version Localizations](app-store-version-localizations.md)
  Create and maintain version-specific App Store metadata that’s localized.
- [Routing App Coverages](routing-app-coverages.md)
  Manage geographic coverage files for apps that use location to provide routing information.
- [Accessibility declarations](accessibility-declarations.md)
  Manage accessibility metadata for your apps per device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-tags)*