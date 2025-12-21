# App Store Connect API 4.1 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.1 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- You can now use [`Build uploads`](build-uploads.md) to upload and manage build uploads for your apps.
- You can now use the [`App tags`](app-tags.md) resource to review the Apple created app tags for your app and opt out of certain app tags. To learn more, see [`Manage app tags`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags).
- Background assets has three new webhook event types for background assets, `BACKGROUND_ASSET_VERSION_INTERNAL_BETA_RELEASE_CREATED`, `BACKGROUND_ASSET_VERSION_EXTERNAL_BETA_RELEASE_STATE_UPDATED`, and `BACKGROUND_ASSET_VERSION_APP_STORE_RELEASE_STATE_UPDATED`. To learn more, see [`Understanding webhook events`](webhook-events.md).
- [`Webhook notifications`](webhook-notifications.md) now includes events for build uploads and build beta details. To learn more see, [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md) and [`Understanding webhook events`](webhook-events.md).
- You can now use composite or sequential checksum on upload of asset packs. Checksums are not required for upload. For more information about these assets, see [`Uploading and versioning Apple hosted background assets`](managing-apple-hosted-background-assets.md).
- You can now use the resource `backgroundAssetVersionExternalBetaReleases` to manage asset packs for external betas, and `backgroundAssetVersionAppStoreReleases` to manage asset packs for App store releases. To learn more, see [`Background assets`](background-assets.md).
- You can now read age ratings per territory by using [`List territory age ratings for an app info`](get-v1-appinfos-_id_-territoryageratings.md).

##### Improvements

- The attribute `platform` is no longer required when using [`Create a review submission`](post-v1-reviewsubmissions.md). You can optionally add the attribute `platform` when using [`Modify a review submission`](patch-v1-reviewsubmissions-_id_.md).
- The attribute `streamlinedPurchasingEnabled` has a default value of `true` for the object [`App.Attributes`](app/attributes-data.dictionary.md).
- The attribute `APPLE_VISION_PRO` is now documented for [`Device.Attributes`](device/attributes-data.dictionary.md).
- The attributes `baDownloadAllowance` and `baMaxInstallSize` are now documented for [`BuildBundle.Attributes`](buildbundle/attributes-data.dictionary.md).
- The attributes `usesNonExemptEncryption` and `computedMinVisionOsVersion` are now documented for [`Build.Attributes`](build/attributes-data.dictionary.md).
- The filter `buildAudienceType` is now available for [`List Prerelease Versions`](get-v1-prereleaseversions.md).
- The attribute `masked` is now available for [`BuildIcon.Attributes`](buildicon/attributes-data.dictionary.md). This boolean value that returns true if an icon has Liquid Glass treatment applied.

##### Deprecations

- The attributes for [`AgeRatingDeclaration.Attributes`](ageratingdeclaration/attributes-data.dictionary.md), `INFREQUENT_OR_MILD` and `FREQUENT_OR_INTENSE` are deprecated. When you [`Modify an Age Rating Declaration`](patch-v1-ageratingdeclarations-_id_.md), use the values use `INFREQUENT` or `FREQUENT` to update the age rating declarations for your app.
- The `sourceFileChecksum` attribute is deprecated for [`Commit an uploaded asset pack to a background asset version`](patch-v1-backgroundassetuploadfiles-_id_.md). Use `sourceFileChecksums` with the new [`Checksums`](checksums.md) type instead.

##### Removals

- The `allowedDurations` properties is now removed from [`Create a challenge`](post-v1-gamecenterchallenges.md) and [`Modify a challenge`](patch-v1-gamecenterchallenges-_id_.md).

## See Also

- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-1-release-notes)*