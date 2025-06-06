# App Store Connect API 3.8 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 3.8 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- The [`Merchant ID`](merchantids.md) resource is now available to automate tasks related to Apple Pay and Apple Wallet. Apple Pay certificates now have enum values on the `certificates` resource.
- [`Modify a certificate`](patch-v1-certificates-_id_.md) is now available. Use this endpoint to modify the activation status of your Payment Processing certificate. To learn more, see [`Managing merchant IDs and Payment Processing certificates`](managing-payment-processing-certificates.md).
- Create public links that accept testers with specific device and OS combinations using the `betaRecruitmentCriteria` resource. To learn more, see [`Beta recruitment criteria`](beta-recruitment-criteria.md).
- Use the new `nominations` resource to share your new content, app enhancement, or app launch with Apple. To learn more see, [`Getting featured on the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/getting-featured/).
- Three new content statuses, `TRADER_STATUS_NOT_PROVIDED`, `TRADER_STATUS_VERIFICATION_FAILED`, and `TRADER_STATUS_VERIFICATION_STATUS_MISSING` are available for [`TerritoryAvailability.Attributes`](territoryavailability/attributes-data.dictionary.md). To learn more, see [`Manage European Union Digital Services Act trader requirements`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements).

##### Improvements

- The field `iosBuildsAvailableForAppleVision` is now in the [`Beta Groups`](beta-groups.md) resource.

##### Deprecations

- The attribute `brazilAgeRatings` for [`AppInfo.Attributes`](appinfo/attributes-data.dictionary.md) is deprecated. Use `brazilAgeRatingV2` instead.

##### Removals

- The `PromotedPurchaseImages` resources is now removed and replaced with [`Subscription images`](subscription-images.md) and [`In-app purchase images`](in-app-purchase-images.md).
- The enum `ELAPSED_TIME_MILLISECOND` is now removed from [`GameCenterLeaderboardFormatter`](gamecenterleaderboardformatter.md).

## See Also

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
- [App Store Connect API 1.7 release notes](app-store-connect-api-1-7-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-3-8-release-notes)*