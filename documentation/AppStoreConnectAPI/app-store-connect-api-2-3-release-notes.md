# App Store Connect API 2.3 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

##### New Features

- Getting an app’s price points and [`List All Price Points for an In-App Purchase`](get-v2-inapppurchases-_id_-pricepoints.md) now support 900 price points.
- [`List app price point equalizations`](get-v3-apppricepoints-_id_-equalizations.md) allows for setting equalized prices.
- Getting and managing an app’s price schedules   and [`In-App purchase price schedules`](in-app-purchase-price-schedules.md) support automatic prices, manual prices, and base territory configuration.
- Getting and managing an app’s availability, [`In-app purchase availability`](in-app-purchase-availability.md) and [`Subscription availability`](subscription-availability.md) supports configuring availabilty for apps, in-app purchases, and subscriptions.

##### Deprecations

- The `List all price points for an app V1` endpoint is now deprecated and replaced with [`List all price points for an app`](get-v1-apps-_id_-apppricepoints.md).
- The `List all prices for an app` endpoint is now deprecated and replaced with [`Read price schedule information for an app`](get-v1-apps-_id_-apppriceschedule.md).
- The `List all available territories for an app` endpoint is now deprecated and replaced with `GET-v1-appAvailabilities-{id}`.
- The `AppPricePointV2` object deprecated and replaced with [`AppPricePointV3`](apppricepointv3.md).
- The `List all price points for an app V1` endpoint is now deprecated and replaced with `List app price tiers`.
- The `Read app price tier information` endpoint is now deprecated and replaced with `Read App Price Point Information`.

> ❗ **Important**:  If you use [`Add a scheduled price change to an app`](post-v1-apppriceschedules.md) to add a scheduled price change to your App, you can’t use `AppPriceInlineCreate` to change your App’s price.

##### Note to Developers

On May 9, 2023, pricing for your existing apps and in-app purchases (excluding auto-renewable subscriptions) will be updated across all 175 storefronts to be equalized to your base country or region using publicly available exchange rate information. If you don’t specify a base country or region, Apple will use your current price in the United States as the basis to provide comparable prices in other countries or regions. Learn more about [`app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) or[` in-app purchase pricing`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

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
- [App Store Connect API 2.2 release notes](app-store-connect-api-2-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.1 release notes](app-store-connect-api-2-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.0 release notes](app-store-connect-api-2-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 1.8 release notes](app-store-connect-api-1-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-2-3-release-notes)*