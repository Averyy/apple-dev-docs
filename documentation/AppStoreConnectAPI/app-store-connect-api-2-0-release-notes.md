# App Store Connect API 2.0 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 2.0 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- Added support for creating, managing, and submitting for review your in-app purchases and auto-renewable subscriptions, using the resources now available in the [`In-App Purchase`](in-app-purchase.md) and [`Auto-Renewable Subscriptions`](auto-renewable-subscriptions.md) collections. The [`Promoted Purchases`](promoted-purchases.md) resources can now manage promoted in-app purchases and auto-renewable subscriptions, including their visibility and images. The resources in the [`In-App Purchase and Subscription App Store Review Submissions`](in-app-purchase-and-subscription-app-store-review-submissions.md) collection manage submissions for review.
- The [`Customer Reviews`](customer-reviews.md) and [`Customer Review Responses`](customer-review-responses.md) resources support retrieving customer reviews for your app that appear on the App Store, and managing your responses to the customer reviews.
- [`Power and Performance Metrics and Logs`](power-and-performance-metrics-and-logs.md) adds a new `HANGS` diagnostic type filter for [`List All Diagnostic Signatures for a Build`](get-v1-builds-_id_-diagnosticsignatures.md), updates the schema for responses in [`xcodeMetrics`](xcodemetrics.md), and adds support for long-lived tokens as described in [`Generating Tokens for API Requests`](generating-tokens-for-api-requests.md).

##### Deprecations

- The [`List All In-App Purchases for an App V1`](get-v1-apps-_id_-inapppurchases.md) endpoint is now deprecated and replaced with the [`List All In-App Purchases for an App`](get-v1-apps-_id_-inapppurchasesv2.md) endpoint.

##### Removals

- App Store Connect APIs for declaring IDFA usage are now removed. In your app, APIs that offer IDFA functionality are still available but require obtaining the user’s permission using [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency). You may also need to provide information about IDFA usage in your app’s privacy details on the App Store. For more information, see [`User Privacy and Data Use`](https://developer.apple.comhttps://developer.apple.com/app-store/user-privacy-and-data-use/) and [`App Privacy Details`](https://developer.apple.comhttps://developer.apple.com/app-store/app-privacy-details/).

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
- [App Store Connect API 1.8 release notes](app-store-connect-api-1-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 1.7 release notes](app-store-connect-api-1-7-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-2-0-release-notes)*