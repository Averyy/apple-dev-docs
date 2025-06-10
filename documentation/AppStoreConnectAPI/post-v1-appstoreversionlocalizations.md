# Create an App Store Version Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add localized version-level information for a new locale.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to add localized version information for a new locale. Be sure to use [`Create an App Info Localization`](post-v1-appinfolocalizations.md) to add the same locale to the version as well.

> ❗ **Important**:  If the app store version and the app info don’t have the same set of localizations, you will receive an erorr when you submit the version to the App Store.

##### Add Localized App Store Version Information in Us English

## See Also

- [Modify an App Store Version Localization](patch-v1-appstoreversionlocalizations-_id_.md)
  Modify localized version-level information for a particular language.
- [Delete an App Store Version Localization](delete-v1-appstoreversionlocalizations-_id_.md)
  Delete a language from your version metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstoreversionlocalizations)*