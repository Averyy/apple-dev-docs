# App Store Connect API 3.6 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 3.6 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- Win-back offers can now be configured using [`Win-back offers`](win-back-offers.md). These are offers to bring back churned or expired customers to a subscription.  To learn more, see [`Creating and configuring win-back offers`](creating-and-configuring-win-back-offers.md).
- Developers can now use [`Subscription images`](subscription-images.md) and [`In-app purchase images`](in-app-purchase-images.md) endpoints to manage images for promoting subscriptions and in-app purchases.
- Age ratings for Australia and Korea can be read using [`Read App Info Information`](get-v1-appinfos-_id_.md).
- There are two new attributes available for age rating declarations. Use [`Modify an Age Rating Declaration`](patch-v1-ageratingdeclarations-_id_.md) to set the attributes `lootbox` and `koreaAgeRatingOverride`, to learn more, see [`AgeRatingDeclarationUpdateRequest.Data.Attributes`](ageratingdeclarationupdaterequest/data-data.dictionary/attributes-data.dictionary.md).
- The `INSTALLS` report type now has a detailed and summary monthly option for [`Download Sales and Trends Reports`](get-v1-salesreports.md).
- The [`TerritoryAvailability.Attributes`](territoryavailability/attributes-data.dictionary.md) resource now has two additional `contentStatuses` possible values, `ICP_NUMBER_MISSING` and `ICP_NUMBER_INVALID`. To learn more, see the “Availability in China mainland” section in [`App Store Connect Help`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-information).
- Developers can now upload screenshots for Apple Watch Series 10, to learn more about possible values, see [`ScreenshotDisplayType`](screenshotdisplaytype.md).
- Developers can now add an app encryption declaration for a given app using [`Create an app encryption declarations`](post-v1-appencryptiondeclarations.md).

##### Improvements

- The OpenAPI specification ([`downloadable here`](https://developer.apple.comhttps://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip)) values has improved `operationId` names and the Apple managed [`Swift OpenAPI generator`](https://developer.apple.comhttps://github.com/apple/swift-openapi-generator) now produces more readable names for the App Store Connect API operations.
- [`SubscriptionStatusUrlVersion`](subscriptionstatusurlversion.md) normalized to all caps values such as `V1` and `V2`.
- The [`List Apps`](get-v1-apps.md) resources now has more optional filters, including `reviewSubmissions.state`, `reviewSubmissions.platform`. The optional field `appAvailabilityV2` is also now available.
- The [`Read App Store Version Information`](get-v1-appstoreversions-_id_.md) endpoint now includes `gameCenterAppVersions` fields.
- The [`List All Price Points for a Subscription`](get-v1-subscriptions-_id_-pricepoints.md) endpoint now requires a `territory` filter.
- The `purchaseRequirement` attribute for [`AppEvent.Attributes`](appevent/attributes-data.dictionary.md) now correctly shows as a `string` type.

##### Deprecations

- The `app` relationship to [`Create an app encryption declarations`](post-v1-appencryptiondeclarations.md) has been deprecated.
- The [`Promoted Purchase Images`](promoted-purchase-images.md) endpoints have been deprecated and replaced with [`Subscription images`](subscription-images.md) and [`In-app purchase images`](in-app-purchase-images.md).

##### Removals

- The duration `ONE_DAY` has been removed from from [`SubscriptionOfferDuration`](subscriptionofferduration.md).

## See Also

- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-3-6-release-notes)*