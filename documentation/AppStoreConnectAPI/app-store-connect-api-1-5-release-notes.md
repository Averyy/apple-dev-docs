# App Store Connect API 1.5 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 1.5 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- [`Xcode Cloud Workflows and Builds`](xcode-cloud-workflows-and-builds.md) can now automate reading Xcode Cloud data, managing workflows, and starting builds.
- [`App Store Version Release Requests`](app-store-version-release-requests.md) now support manually releasing an App Store-approved version of your app to the App Store.
- The [`BetaGroup.Attributes`](betagroup/attributes-data.dictionary.md) adds an `isInternalGroup` property to support creating internal beta tester groups for TestFlight, in [`Beta Groups`](beta-groups.md).
- The [`AppInfoLocalization.Attributes`](appinfolocalization/attributes-data.dictionary.md) in [`App Metadata`](app-metadata.md) adds a `privacyChoicesURL` property.
- The API now supports JSON web tokens that can last longer than 20 minutes for resources that meet the required criteria. For more information, see [`Generating Tokens for API Requests`](generating-tokens-for-api-requests.md).

##### Deprecations

- The `Advertising Identifier (IDFA) Declarations` resource and all its associated endpoints and objects are now deprecated, including: `Create an IDFA Declaration`, `Modify an IDFA Declaration`, `Delete an IDFA Declaration`, `Read the IDFA Declaration Information of an App Store Version`, `IdfaDeclaration`, `IdfaDeclarationCreateRequest`, `IdfaDeclarationUpdateRequest`, and `IdfaDeclarationResponse`.

## See Also

- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.5 release notes](app-store-connect-api-3-5-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.4 release notes](app-store-connect-api-3-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.1 release notes](app-store-connect-api-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.0 release notes](app-store-connect-api-3-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.4 release notes](app-store-connect-api-2-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.2 release notes](app-store-connect-api-2-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.1 release notes](app-store-connect-api-2-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.0 release notes](app-store-connect-api-2-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 1.8 release notes](app-store-connect-api-1-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-1-5-release-notes)*