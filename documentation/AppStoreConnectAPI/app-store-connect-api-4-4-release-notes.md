# App Store Connect API 4.4 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.4 provides resources that enable you to automate actions you take in App Store Connect.

#### Added

- Use [`Subscription plan availability`](subscription-plan-availability.md) to configure monthly subscriptions with a 12-month commitment.
- Added `STORAGE` to [`MetricCategory`](metriccategory.md). Track your app’s storage footprint over time to catch regressions in data usage and binary size.
- Added the `ANIMATION` [`MetricCategory`](metriccategory.md), which displays information about the hitch rate of your app over time. The hitch rate tracks animation interruptions across all animated interactions in your app, including scrolling, transitions, and other continuous motion. To learn more, see [`Understanding user interface responsiveness`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/understanding-user-interface-responsiveness).
- Metric goals are now available for Battery Usage, Disk Writes, Hang Rate, Hitches, Memory, and Storage metrics, so you can prioritize performance engineering across more areas. Similar-app goals now cover Hang Rate, On-screen Battery Usage, Disk Writes, and Storage. Launch Time similar-app goals are more accurate, establishing new baselines. To learn more, see [`MetricCategory`](metriccategory.md).
- Added a `ZERO_ZERO` value to [`AppStoreAgeRating`](appstoreagerating.md), representing Vietnam’s 00+ age-rating classification.

#### Changed

- Background Assets now supports multiple locales, so your app can deliver only the assets that match a customer’s locale preference. Use [`List all background assets for an app`](get-v1-apps-_id_-backgroundassets.md) with the `filter[versions.locale]` parameter to read the uploaded locales.

#### Deprecated

- The user role permission `ACCESS_TO_REPORTS` for App Store Connect API is deprecated. See [`UserRole`](userrole.md) for available alternatives.
- The [`Subscription availability`](subscription-availability.md) resource is deprecated. Use [`Subscription plan availability`](subscription-plan-availability.md) instead.
- The `goalKeys` property of [`xcodeMetrics.ProductData.MetricCategories.Metrics`](xcodemetrics/productdata-data.dictionary/metriccategories-data.dictionary/metrics-data.dictionary.md) is deprecated.

#### Removed

- Removed the `GET /v1/appStoreVersions/{id}/relationships/ageRatingDeclaration` and `GET /v1/appStoreVersions/{id}/ageRatingDeclaration` endpoints. Use [`Read the age-rating declaration`](get-v1-appinfos-_id_-ageratingdeclaration.md) instead.

## See Also

- [App Store Connect API 4.3.1 release notes](app-store-connect-api-4-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-4-release-notes)*