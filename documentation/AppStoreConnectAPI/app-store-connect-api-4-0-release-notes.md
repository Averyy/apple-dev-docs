# App Store Connect API 4.0 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.0 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- Use the new `webhooks` endpoints to setup and configure notifications for events that happen with your apps, including App version state events and TestFlight feedback events. For more information about webhook notifications, see [`Webhook notifications`](webhook-notifications.md).
- The [`Accessibility declarations`](accessibility-declarations.md) resources are now available to automate creating, updating, and reading accessibility declarations for your app per device family. You can also now use [`Modify an App`](patch-v1-apps-_id_.md) to update the `accessibilityURL` for your app. For more information about accessibility declarations, see [`Configuring accessibility declarations for your app`](configuring-accessibility-declarations.md).
- Get TestFlight feedback screenshots and crash logs from beta testers for your apps. For more information about beta-tester feedback, see [`Beta feedback crash submissions`](beta-feedback-crash-submissions.md) and [`Beta feedback screenshot submissions`](beta-feedback-screenshot-submissions.md).
- You can now read the customer review summary for your apps by using [`Read customer review summarizations`](get-v1-apps-_id_-customerreviewsummarizations.md).
- You can now manage background assets for your app that you can upload and download separately from the Apple hosted app. For more information about these assets, see [`Uploading and versioning Apple hosted background assets`](managing-apple-hosted-background-assets.md).
- Activities for Game Center resources are now available; for more information, see [`Game Center activities`](game-center-activities.md).
- You can now setup and configure Game Center challenges. For more information on these challenges, see [`Game Center challenges`](game-center-challenges.md).

##### Improvements

- XcodeMetrics now includes `recommendedMetricGoal`. Use [`Get Power and Performance Metrics for an App`](get-v1-apps-_id_-perfpowermetrics.md) to view the available recommendations for your app metrics.
- There are new enums available for `mapAction` when creating or modifying an App Clip advanced experience. To learn more, see [`AppClipAdvancedExperience.Attributes.Place`](appclipadvancedexperience/attributes-data.dictionary/place-data.dictionary.md).
- [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md) now shows all media types that support upload to App Store Connect API.
- The attribute `streamlinedPurchasingEnabled` has a default value of `true` for the object [`App.Attributes`](app/attributes-data.dictionary.md).
- The attribute `APPLE_VISION_PRO` is now documented for [`Device.Attributes`](device/attributes-data.dictionary.md).

##### Deprecations

- The attribute `challengeEnabled` is now deprecated from [`Enable Game Center for an app`](post-v1-gamecenterdetails.md) and [`Modify a Game Center detail for an app`](patch-v1-gamecenterdetails-_id_.md). Use `challenges` instead.
- [`Create a leaderboard set member localization`](post-v1-gamecenterleaderboardsetmemberlocalizations.md) and [`Modify a leaderboard set member localization`](patch-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md) are deprecated.

##### Removals

- Create an App Store version submission is now removed. Use [`Create a review submission`](post-v1-reviewsubmissions.md) instead.
- The `gamblingAndContests` and `seventeenPlus` properties are now removed from [`Read age rating declaration`](get-v1-appinfos-_id_-ageratingdeclaration.md) and [`Modify an Age Rating Declaration`](patch-v1-ageratingdeclarations-_id_.md). Use the `contests` or `gambling` properties instead.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-0-release-notes)*