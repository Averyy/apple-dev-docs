# recentSubscriptionStartDate

**Framework**: App Store Server API  
**Kind**: typealias

The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
timestamp recentSubscriptionStartDate
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The recent subscription start date is in UNIX time, in milliseconds.

Use the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) to identify the earliest start date of a subscription in a series of auto-renewable subscription purchases that the customer maintained continuously, or that has one or more gaps of less than 60 days each.

The App Store calculates the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) by finding the start date of the most recent auto-renewable subscription purchase that’s preceded by a gap in paid service of more than 60 days in the production environment, or 10 minutes in the sandbox environment. The start date includes any free trials or promotional purchases. If no such gap exists — for example, if the user has only ever purchased one subscription — the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) is the same as the subscription’s [`originalPurchaseDate`](originalpurchasedate.md).

The [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) calculation counts a grace period or a billing retry state as a gap in the paid service.

> ❗ **Important**:  Don’t use the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) date to calculate days of paid service. For more information about paid days of service, see [`Net revenue after a year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

 Don’t use the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) date to calculate days of paid service. For more information about paid days of service, see [`Net revenue after a year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

This date applies to active or expired subscriptions. For example, if a subscriber purchases an auto-renewable subscription on June 1, 2022 and lets it expire on December 31, 2022, the App Store determines the recent subscription start date as follows:

- Initially, the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) is the same as the [`originalPurchaseDate`](originalpurchasedate.md): June 1, 2022.
- If the customer purchases the subscription again on February 1, 2023, less than 60 days after the initial subscription expired, the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) remains June 1, 2022.
- If the customer purchases the subscription again on April 1, 2023, more than 60 days after the first subscription expired, the App Store updates the [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) to April 1, 2023.

## See Also

- [type originalPurchaseDate](originalpurchasedate.md)
  The purchase date of the transaction associated with the original transaction identifier.
- [type purchaseDate](purchasedate.md)
  The time that the App Store charged the customer’s account for an In-App Purchase, a restored In-App Purchase, a subscription, or a subscription renewal after a lapse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/recentsubscriptionstartdate)*