# App Store Connect API 2.4 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

##### New Features

- Added support for product page optimization tests that run without being interrupted by new app version releases with the new [`App Store version experiments`](app-store-version-experiments.md).
- A new [`Actors`](actors.md) resource provides details on which team member submitted and last interacted with an App Store submission.
- Added the ability to look up territory availability from an in-app purchase with [`Read Information About the Availability of an In-App Purchase`](get-v2-inapppurchases-_id_-inapppurchaseavailability.md) or from a subscription with [`Read Information About the Availability of a Subscription`](get-v1-subscriptions-_id_-subscriptionavailability.md).
- Updated the limit for return values to 8000 for [`List All Price Points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md) and [`List All Price Points for a Subscription`](get-v1-subscriptions-_id_-pricepoints.md).

##### Deprecations

- The [`Read App Store experiment information v1`](get-v1-appstoreversionexperiments-_id_.md) endpoint is now deprecated and replaced with [`Read App Store Experiment Information`](get-v2-appstoreversionexperiments-_id_.md).
- The [`Create an App Store experiment v1`](post-v1-appstoreversionexperiments.md) endpoint is now deprecated and replaced with [`Create an App Store Experiment`](post-v2-appstoreversionexperiments.md).
- The [`Modify an App Store experiment v1`](patch-v1-appstoreversionexperiments-_id_.md) endpoint is now deprecated and replaced with [`Modify an App Store Experiment`](patch-v2-appstoreversionexperiments-_id_.md).
- The [`Delete an App Store Version Experiment v1`](delete-v1-appstoreversionexperiments-_id_.md) endpoint is now deprecated and replaced with [`Delete an App Store Experiment`](delete-v2-appstoreversionexperiments-_id_.md).
- The [`List All Experiments for an App Store Version v1`](get-v1-appstoreversions-_id_-appstoreversionexperiments.md) endpoint is now deprecated and replaced with [`List All Experiments for an App Store Version`](get-v1-appstoreversions-_id_-appstoreversionexperimentsv2.md).
- The `pricePoints` include for [`List All In-App Purchases for an App`](get-v1-apps-_id_-inapppurchasesv2.md) is no longer available.
- The `pricePoints` include for [`Read In-App Purchase Information`](get-v2-inapppurchases-_id_.md) is now deprecated and replaced with [`List All Price Points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md).

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
- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.1 release notes](app-store-connect-api-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.0 release notes](app-store-connect-api-3-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.2 release notes](app-store-connect-api-2-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.1 release notes](app-store-connect-api-2-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-2-4-release-notes)*