# recentSubscriptionStartDate

**Framework**: StoreKit  
**Kind**: property

The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var recentSubscriptionStartDate: Date { get }
```

#### Discussion

> ❗ **Important**:  Don’t use the [`recentSubscriptionStartDate`](product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate.md) date to calculate days of paid service. For more information about paid days of service, see [`Net revenue after a year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

 Don’t use the [`recentSubscriptionStartDate`](product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate.md) date to calculate days of paid service. For more information about paid days of service, see [`Net revenue after a year`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

## See Also

- [var renewalDate: Date?](product/subscriptioninfo/renewalinfo/renewaldate.md)
  The UNIX time, in milliseconds, that the most recent auto-renewable subscription purchase expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate)*