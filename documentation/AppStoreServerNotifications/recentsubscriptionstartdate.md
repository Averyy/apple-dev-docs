# recentSubscriptionStartDate

**Framework**: App Store Server Notifications  
**Kind**: typealias

The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.

**Availability**:
- App Store Server Notifications 2.5+

## Declaration

```swift
timestamp recentSubscriptionStartDate
```

#### Discussion

For more information about the recent subscription start date, see [`recentSubscriptionStartDate`](https://developer.apple.com/documentation/AppStoreServerAPI/recentSubscriptionStartDate).

> ❗ **Important**:  Don’t use the [`recentSubscriptionStartDate`](recentsubscriptionstartdate.md) date to calculate days of paid service. For more information about paid days of service, see [`Net revenue after a year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

 Don’t use the [`recentSubscriptionStartDate`](recentsubscriptionstartdate.md) date to calculate days of paid service. For more information about paid days of service, see [`Net revenue after a year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

## See Also

- [type originalPurchaseDate](originalpurchasedate.md)
  The purchase date of the transaction associated with the original transaction identifier.
- [type purchaseDate](purchasedate.md)
  The time that the App Store charged the customer’s account for a purchase, a restored product, a subscription, or a subscription renewal after a lapse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/recentsubscriptionstartdate)*