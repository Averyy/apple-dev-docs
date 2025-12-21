# App Store Connect API 3.3 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 3.3 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- Developers who receive the entitlement can now configure and set up marketplace apps. For more information see: [`Creating an alternative app marketplace`](https://developer.apple.com/documentation/appdistribution/creating-an-alternative-app-marketplace) and [`Update on apps distributed in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/dma-and-apps-in-the-eu/).
- You can now set the attribute `reviewType` when calling [`Modify an App Store Version`](patch-v1-appstoreversions-_id_.md) for iOS apps, to specify app destination.
- You can now generate and read information about alternative distribution packages for distribution to EU users through an alternative marketplace. For more information see, [`Creating alternative distribution packages`](creating-alternative-distribution-packages.md).
- You can now configure marketplace search [`Add a marketplace search detail URL`](post-v1-marketplacesearchdetails.md).
- You can now configure notifications for changes to apps distributed through an alternative marketplace. To learn more see [`Add a marketplace webhook configuration`](post-v1-marketplacewebhooks.md).
- [`AppStoreAgeRating`](appstoreagerating.md) type now has the enum `Unrated`. This is only available when using `reviewType` `NOTARIZATION.`

##### Deprecations

- The `appStoreState` attribute is now deprecated and replaced with `appVersionState` in the object [`AppStoreVersion.Attributes`](appstoreversion/attributes-data.dictionary.md).
- The `appStoreState` attribute is now deprecated and replaced with `state` in the object [`AppInfo.Attributes`](appinfo/attributes-data.dictionary.md).

## See Also

- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-3-3-release-notes)*