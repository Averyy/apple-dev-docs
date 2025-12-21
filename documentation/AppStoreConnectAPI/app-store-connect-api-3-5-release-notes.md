# App Store Connect API 3.5 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 3.5 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- Developers can optionally provide a single deep-link URL for a custom project page by adding a `deepLink` attribute to [`AppCustomProductPageVersionCreateRequest.Data.Attributes`](appcustomproductpageversioncreaterequest/data-data.dictionary/attributes-data.dictionary.md). For more information, see [`Configure multiple product page versions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions).
- `ELAPSED_TIME_CENTISECOND` is now available in [`GameCenterLeaderboardFormatter`](gamecenterleaderboardformatter.md).
- Developers can now more easily debug slow-launch issues for their app with the new `LAUNCHES diagnosticType` for [`List All Diagnostic Signatures for a Build`](get-v1-builds-_id_-diagnosticsignatures.md).
- Trending insights for disk writes signatures are now available and show the impact of signature trends across app versions. [`List All Diagnostic Signatures for a Build`](get-v1-builds-_id_-diagnosticsignatures.md) now includes the `DiagnosticInsightDirection`, `DiagnosticInsightType`, and an impact breakdown by app version.
- A new attribute `BetaTesterState` is available for [`BetaTester.Attributes`](betatester/attributes-data.dictionary.md). For more information, see [`View and manage tester information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-a-beta-version/view-and-manage-tester-information).

##### Removals

- The `IMAGE_MANAGER` role is now removed from [`UserRole`](userrole.md).
- The attribute `priceTier` is now removed from [`List All Price Points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-3-5-release-notes)*