# App Store Connect API 3.7 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 3.7 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- Developers now need to provide a description for all beta localizations before submitting to beta app review for external testing with TestFlight. You can update `betaAppLocalizations` with [`Modify a Beta App Localization`](patch-v1-betaapplocalizations-_id_.md).
- Added `WIN_BACK_ELIGIBILITY` report type to [`Download Sales and Trends Reports`](get-v1-salesreports.md).
- Name is now a required field when using [`Create an App Info Localization`](post-v1-appinfolocalizations.md). To see other attributes you can create or modify, see  [`AppInfoLocalizationCreateRequest.Data.Attributes`](appinfolocalizationcreaterequest/data-data.dictionary/attributes-data.dictionary.md).
- Developers can now look up in-app purchase price point equalization using [`List all in-app purchase price point equalizations`](get-v1-inapppurchasepricepoints-_id_-equalizations.md).
- The enum `UNIVERSAL` is now added to [`BundleIdPlatform`](bundleidplatform.md). To learn more, see [`Preparing your app for distribution`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution/#Set-the-bundle-ID).
- The enums `DEVELOPER_ID_APPLICATION_G2` and `DEVELOPER_ID_KEXT_G2` are now available when using [`CertificateType`](certificatetype.md). To learn more, see [`Notarizing macOS software before distribution`](https://developer.apple.comhttps://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution) and [`macOS Code Signing Tips and Tricks`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919).
- You can now read age ratings for France by using [`Read App Info Information`](get-v1-appinfos-_id_.md).
- The [`Read an app’s alternative distribution key`](get-v1-apps-_id_-alternativedistributionkey.md) endpoint now shows multiple distribution keys when you have multiple configured.
- There is a new required attribute `defaultFormatter` when you use [`Create a leaderboard`](post-v1-gamecenterleaderboards.md), which gives all your localizations the same formatter. To learn more, see [`GameCenterLeaderboardCreateRequest.Data.Attributes`](gamecenterleaderboardcreaterequest/data-data.dictionary/attributes-data.dictionary.md).

##### Deprecations

- The attribute `previewImage` on [`AppPreview.Attributes`](apppreview/attributes-data.dictionary.md) is deprecated. Use `previewFrameImage` and [`PreviewFrameImage`](previewframeimage.md) instead.
- The attribute `assetDeliveryState` on [`AppPreview.Attributes`](apppreview/attributes-data.dictionary.md) is deprecated. Use `videoDeliveryState` and [`AppMediaVideoState`](appmediavideostate.md) instead.
- The attribute `previewImage` on [`AppEventVideoClip.Attributes`](appeventvideoclip/attributes-data.dictionary.md) is deprecated. Use `previewFrameImage` and [`PreviewFrameImage`](previewframeimage.md) instead.
- The attribute `assetDeliveryState` on [`AppEventVideoClip.Attributes`](appeventvideoclip/attributes-data.dictionary.md) is deprecated. Use `videoDeliveryState` and [`AppMediaVideoState`](appmediavideostate.md) instead.
- The attribute `appStoreState` on [`AppInfo.Attributes`](appinfo/attributes-data.dictionary.md) is deprecated. Use `state` instead.
- The attribute `appStoreState` on [`AppStoreVersion.Attributes`](appstoreversion/attributes-data.dictionary.md) is deprecated. Use `appVersionState` and [`AppVersionState`](appversionstate.md) instead.
- The relationship `groupLeaderboardSet` on [`GameCenterLeaderboardSet.Relationships`](gamecenterleaderboardset/relationships-data.dictionary.md) is deprecated.
- The relationship `groupAchievement` on [`GameCenterAchievement.Relationships`](gamecenterachievement/relationships-data.dictionary.md) is deprecated.
- The relationship `groupLeaderboard` on [`GameCenterLeaderboard.Relationships`](gamecenterleaderboard/relationships-data.dictionary.md) is deprecated.

##### Removals

- The `v1/appPreOrders` and `v1/appAvailabilities` resources are removed and replaced with `v2/appAvailabilities`. To learn more, see [`App availability`](app-availability.md).
- `WATCH_SERIES_4` and `WATCH_SERIES_3` enums are removed from [`PreviewType`](previewtype.md).
- The `subscription` include for [`Read the availability of a subscription`](get-v1-subscriptionavailabilities-_id_.md) is removed.

## See Also

- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-3-7-release-notes)*