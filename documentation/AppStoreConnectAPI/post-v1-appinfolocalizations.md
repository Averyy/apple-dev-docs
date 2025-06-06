# Create an App Info Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add app-level localized information for a new locale.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

#### Discussion

Use this endpoint to add localized app information for a new locale. Be sure to use [`Create an App Store Version Localization`](post-v1-appstoreversionlocalizations.md) to add the same locale to the version as well.

> ❗ **Important**:  If the app store version and the app info don’t have the same set of localizations, you will receive an erorr when you submit the version to the App Store.

 If the app store version and the app info don’t have the same set of localizations, you will receive an erorr when you submit the version to the App Store.

##### Add Localized App Information in Us English

## See Also

- [Modify an App Info Localization](patch-v1-appinfolocalizations-_id_.md)
  Modify localized app-level information for a particular language.
- [Delete an App Info Localization](delete-v1-appinfolocalizations-_id_.md)
  Delete an app information localization that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appinfolocalizations)*