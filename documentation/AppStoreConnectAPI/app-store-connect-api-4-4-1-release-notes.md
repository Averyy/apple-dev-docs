# App Store Connect API 4.4.1 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.4.1 provides resources that enable you to automate actions you take in App Store Connect.

#### Added

- Manage in-app purchase metadata as discrete versions. Use [`Create an in-app purchase version`](post-v1-inapppurchaseversions.md) to create a new version, [`Read in-app purchase version information`](get-v1-inapppurchaseversions-_id_.md) to read a version, and [`List the versions of an in-app purchase`](get-v2-inapppurchases-_id_-versions.md) to list all versions for an in-app purchase. Each version exposes its own localizations and review screenshot through [`List localizations for an in-app purchase version`](get-v1-inapppurchaseversions-_id_-localizations.md) and [`Read the image for an in-app purchase version`](get-v1-inapppurchaseversions-_id_-image.md).
- Manage subscription metadata as discrete versions. Use [`Create a subscription version`](post-v1-subscriptionversions.md) to create a new version, [`Read subscription version information`](get-v1-subscriptionversions-_id_.md) to read a version, and [`List versions for a subscription`](get-v1-subscriptions-_id_-versions.md) to list all versions for a subscription. Each version exposes its own localizations and promotional images through [`List localizations for a subscription version`](get-v1-subscriptionversions-_id_-localizations.md) and [`List images for a subscription version`](get-v1-subscriptionversions-_id_-images.md).
- Manage subscription group metadata as discrete versions. Use [`Create a subscription group version`](post-v1-subscriptiongroupversions.md) to create a new version, [`Read subscription group version information`](get-v1-subscriptiongroupversions-_id_.md) to read a version, and [`List the versions of a subscription group`](get-v1-subscriptiongroups-_id_-versions.md) to list all versions for a subscription group. Each version exposes its own localizations through [`List the localizations of a subscription group version`](get-v1-subscriptiongroupversions-_id_-localizations.md).
- Submit an in-app purchase version, subscription version, or subscription group version to App Review. Use [`Create a Review Submission Item`](post-v1-reviewsubmissionitems.md) with an `inAppPurchaseVersion`, `subscriptionVersion`, or `subscriptionGroupVersion` relationship to add the version to a review submission.
- Use [`Create an in-app purchase localization`](post-v2-inapppurchaselocalizations.md), [`Modify an in-app purchase localization`](patch-v2-inapppurchaselocalizations-_id_.md), and [`Delete an in-app purchase localization`](delete-v2-inapppurchaselocalizations-_id_.md) to manage in-app purchase localizations, and [`Create an in-app purchase image`](post-v2-inapppurchaseimages.md), [`Modify an in-app purchase image`](patch-v2-inapppurchaseimages-_id_.md), and [`Delete an in-app purchase image`](delete-v2-inapppurchaseimages-_id_.md) to manage review screenshots. These v2 endpoints are scoped to an [`InAppPurchaseVersion`](inapppurchaseversion.md).
- Use [`Create a subscription localization`](post-v2-subscriptionlocalizations.md), [`Modify a subscription localization`](patch-v2-subscriptionlocalizations-_id_.md), and [`Delete a subscription localization`](delete-v2-subscriptionlocalizations-_id_.md) to manage subscription localizations, and [`Create a subscription image`](post-v2-subscriptionimages.md), [`Modify a subscription image`](patch-v2-subscriptionimages-_id_.md), and [`Delete a subscription image`](delete-v2-subscriptionimages-_id_.md) to manage promotional images. These v2 endpoints are scoped to a [`SubscriptionVersion`](subscriptionversion.md).
- Use [`Create a subscription group localization`](post-v2-subscriptiongrouplocalizations.md), [`Modify a subscription group localization`](patch-v2-subscriptiongrouplocalizations-_id_.md), and [`Delete a subscription group localization`](delete-v2-subscriptiongrouplocalizations-_id_.md) to manage subscription group localizations, including localized custom app names. These v2 endpoints are scoped to a [`SubscriptionGroupVersion`](subscriptiongroupversion.md).
- Use [`List adjusted equalizations for a subscription price point`](get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md) to read the price points that App Store Connect uses to equalize a subscription’s price across territories when the base price point changes. Filter the endpoint with `filter[upfrontPricePointId]` and `filter[planType]` to identify a specific adjusted equalization.
- Added the `socialMedia` and `socialMediaAgeRestricted` Boolean attributes to [`AgeRatingDeclaration`](ageratingdeclaration.md) and [`AgeRatingDeclarationUpdateRequest`](ageratingdeclarationupdaterequest.md), so you can declare whether your app includes social media features and whether those features are age-restricted.

#### Deprecated

- The [`In-app purchase localizations (v1)`](in-app-purchase-localizations-v1.md) resource is deprecated. Use [`In-App Purchase Localizations`](in-app-purchase-localizations.md) instead, which scopes localizations to an [`InAppPurchaseVersion`](inapppurchaseversion.md).
- The [`In-app purchase images (v1)`](in-app-purchase-images-v1.md) resource is deprecated. Use [`In-app purchase images`](in-app-purchase-images.md) instead, which scopes review screenshots to an [`InAppPurchaseVersion`](inapppurchaseversion.md).
- The [`In-App Purchase Submissions`](in-app-purchase-submissions.md) resource is deprecated. Use [`Review submissions`](review-submissions.md) instead to submit an in-app purchase version for App Review.
- The [`Subscription localizations (v1)`](subscription-localizations-v1.md) resource is deprecated. Use [`Subscription Localizations`](subscription-localizations.md) instead, which scopes localizations to a [`SubscriptionVersion`](subscriptionversion.md).
- The [`Subscription images (v1)`](subscription-images-v1.md) resource is deprecated. Use [`Subscription images`](subscription-images.md) instead, which scopes promotional images to a [`SubscriptionVersion`](subscriptionversion.md).
- The [`Subscription group localizations (v1)`](subscription-group-localizations-v1.md) resource is deprecated. Use [`Subscription Group Localizations`](subscription-group-localizations.md) instead, which scopes localizations to a [`SubscriptionGroupVersion`](subscriptiongroupversion.md).
- The [`Subscription and Subscription Group Submissions`](subscription-and-subscription-group-submissions.md) resource is deprecated. Use [`Review submissions`](review-submissions.md) instead to submit a subscription version or subscription group version for App Review.

## See Also

- [App Store Connect API 4.4 release notes](app-store-connect-api-4-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-4-1-release-notes)*