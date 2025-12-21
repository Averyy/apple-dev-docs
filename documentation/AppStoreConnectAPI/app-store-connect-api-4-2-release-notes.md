# App Store Connect API 4.2 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.2 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- You can now submit Game Center content directly to review without including an app version by using [`Review submissions`](review-submissions.md). Use [`Create a review submission item`](post-v1-reviewsubmissionitems.md) to submit achievement versions, leaderboard versions, leaderboard set versions, activity versions, and challenge versions for independent review.
- Game Center resources now support versioning for achievements, leaderboards, and leaderboard sets. To learn more, see [`Game Center achievements`](game-center-achievements.md), [`Game Center leaderboards`](game-center-leaderboards.md), and [`Game Center leaderboard sets`](game-center-leaderboard-sets.md).
- Added support for In-App Purchase offer codes for consumable, non-consumable, and non-renewing subscriptions. Create and manage promotional offer codes using [`Create an in-app purchase offer code`](post-v1-inapppurchaseoffercodes.md), [`Create an in-app purchase offer code custom code`](post-v1-inapppurchaseoffercodecustomcodes.md), and [`Create an in-app purchase offer code one-time use code`](post-v1-inapppurchaseoffercodeonetimeusecodes.md). To learn more, see [`In-App Purchase Offer Codes`](in-app-purchase-offers.md).
- The `appDevices` attribute is now available on the [`BetaTester.Attributes`](betatester/attributes-data.dictionary.md) resource, enabling you to view the device models used by beta testers for your app’s TestFlight testing.
- Background asset versions now include a `stateDetails` attribute that provides additional context about the asset state, including errors, warnings, and informational messages for failed imports. Access this information using [`Read background assets information`](get-v1-backgroundassetversions-_id_.md).
- There is a new string `PAY_TO_PARK` available for `mapAction` when creating or modifying an App Clip advanced experience. To learn more, see [`AppClipAdvancedExperience.Attributes.Place`](appclipadvancedexperience/attributes-data.dictionary/place-data.dictionary.md).
- You can now map your Android apps to your iOS apps using the [`Android to iOS App Mapping`](android-to-ios-app-mapping.md) resource. This mapping enables data and app migration between Android and iOS devices during device setup. Use [`Create an Android to iOS app mapping detail`](post-v1-androidtoiosappmappingdetails.md) to create mappings with your Android app’s package name and signing certificate fingerprints.
- [`Webhook notifications`](webhook-notifications.md) now includes events for alternative app distribution. To learn more see, [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md) and [`Understanding webhook events`](webhook-events.md).
- Alternative distribution packages now include a `sourceFileChecksum` attribute, allowing alternative marketplaces to verify builds with developers. Use [`Read alternative distribution package information`](get-v1-alternativedistributionpackages-_id_.md) to access the checksum of the developer-submitted package.

##### Deprecations

- The `kidsAgeBand` attribute is now deprecated from [`AppInfo.Attributes`](appinfo/attributes-data.dictionary.md). Use [`Modify an Age Rating Declaration`](patch-v1-ageratingdeclarations-_id_.md) instead.
- The alternative distribution [`Notifications`](notifications.md) are deprecated. Use [`Webhook notifications`](webhook-notifications.md) instead. To learn more, see [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md) and [`Understanding webhook events`](webhook-events.md)

##### Removals

- The attribute `challengeEnabled` is now removed from [`Enable Game Center for an app`](post-v1-gamecenterdetails.md) and [`Modify a Game Center detail for an app`](patch-v1-gamecenterdetails-_id_.md). To create a challenge on an existing Game Center detail, use [`Create a challenge`](post-v1-gamecenterchallenges.md).

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-2-release-notes)*